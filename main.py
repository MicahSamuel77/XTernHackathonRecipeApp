import os
import base64
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from openai import OpenAI

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Initialize OpenAI client
client = OpenAI()

@app.route('/measurement.html')
def measurement():
    return render_template('measurement.html')

@app.route('/temperature.html')
def temperature():
    return render_template('temperature.html')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if user typed manual ingredients
    manual_ingredients = request.form.get('manual_ingredients', '').strip()
    all_ingredients = []

    if manual_ingredients:
        # Use typed ingredients
        ingredients_list = [i.strip().lower() for i in manual_ingredients.split(',') if i.strip()]
        all_ingredients.extend(ingredients_list)
    else:
        # Process images only if no manual ingredients provided
        if 'images' not in request.files:
            return jsonify({"error": "No images uploaded and no manual ingredients provided"}), 400

        images = request.files.getlist('images')
        if not images or all(image.filename == '' for image in images):
            return jsonify({"error": "No images found and no manual ingredients provided"}), 400

        for image in images:
            if image.filename == '':
                continue
            filename = secure_filename(image.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            image.save(filepath)

            ingredients = detect_ingredients(filepath)
            all_ingredients.extend(ingredients)

    unique_ingredients = list(dict.fromkeys(all_ingredients))[:5]

    if len(unique_ingredients) == 0:
        return jsonify({"error": "No ingredients detected or provided. Try typing or uploading different images."}), 200

    recipe = generate_recipe(unique_ingredients)

    return jsonify({"ingredients": unique_ingredients, "recipe": recipe})

def detect_ingredients(image_path):
    with open(image_path, "rb") as f:
        b64_image = base64.b64encode(f.read()).decode("utf-8")
    data_url = f"data:image/jpeg;base64,{b64_image}"

    vision_prompt = (
        "List the main food ingredients you can see in this photo. "
        "Only provide a comma-separated list of common food ingredient names, nothing else."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": vision_prompt},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ]
            }
        ],
        max_tokens=100,
    )

    ingredient_text = response.choices[0].message.content.strip()
    ingredients = [i.strip().lower() for i in ingredient_text.split(",") if i.strip()]
    return list(dict.fromkeys(ingredients))[:5]

def generate_recipe(ingredients):
    prompt = (
        f"Create an Indiana-style, elderly-friendly recipe using the following ingredients: {', '.join(ingredients)}.\n"
        "Keep the instructions very simple, use short steps, and no rare ingredients."
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
