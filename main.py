import os
import base64
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from openai import OpenAI

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Initialize OpenAI client
client = OpenAI(
    api_key=""
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    image.save(filepath)

    ingredients = detect_ingredients(filepath)

    # Fallback if no ingredients detected
    if len(ingredients) == 0:
        return jsonify({"error": "No ingredients detected. Please try a different image or type your ingredients."}), 200

    recipe = generate_recipe(ingredients)

    return jsonify({"ingredients": ingredients, "recipe": recipe})

def detect_ingredients(image_path):
    # Encode image as base64 (for OpenAI vision API)
    with open(image_path, "rb") as f:
        b64_image = base64.b64encode(f.read()).decode("utf-8")
    data_url = f"data:image/jpeg;base64,{b64_image}"

    # Compose a prompt to extract food ingredients from the image only
    vision_prompt = (
        "List the main food ingredients you can see in this photo. "
        "Only provide a comma-separated list of common food ingredient names, nothing else."
    )

    response = client.chat.completions.create(
        model="gpt-4o",  # Or "gpt-4-vision-preview"
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
    # Parse comma-separated list
    ingredients = [i.strip().lower() for i in ingredient_text.split(",") if i.strip()]
    # Deduplicate and limit to 5
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