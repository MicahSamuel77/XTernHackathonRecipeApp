# HoosierHelper - AI Recipe Assistant

HoosierHelper is an intelligent cooking companion that transforms your available ingredients into delicious recipe suggestions. Simply upload photos of your ingredients, and our AI-powered system will identify what you have and suggest recipes you can make right now.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [Known Issues](#known-issues)
- [License](#license)
- [Support](#support)
- [Acknowledgments](#acknowledgments)

## Features

<!-- Features will be added here -->

---

## Technology Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Python
- **AI Integration**: OpenAI Vision API
- **Recipe Generation**: OpenAI GPT API
- **Image Processing**: OpenAI Vision Model
- **Styling**: Custom CSS with responsive design
- **File Handling**: HTML5 File API

---

## Installation

### Prerequisites

- Python installed on your system
- OpenAI API key
- Internet connection for API calls

### Setup

1. Clone the repository using the following link:  
   https://github.com/MicahSamuel77/XTernHackathonRecipeApp

2. Configure your OpenAI API key in main.py
'''python
client = OpenAI(
    api_key="API_KEY_HERE"
)
'''

4. Run the app using Python and access it through your web browser.

---

## Usage

### Basic Workflow

1. **Upload Ingredients**: Use the web interface to upload ingredient photos.
2. **AI Recognition**: The system uses OpenAI's Vision model to identify ingredients.
3. **Recipe Generation**: The AI agent generates recipe ideas based on ingredients.
4. **Browse Results**: View personalized recipe suggestions.

### Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- Multiple images supported

---

## API Integration

### OpenAI Vision API

Used for ingredient recognition from uploaded images.

### Recipe Generation API

Processes identified ingredients to create recipe suggestions.

---

## Contributing

We welcome contributions to HoosierHelper! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes and commit them
4. Push to your branch
5. Submit a pull request

### Code Style

- Use consistent indentation (spaces or tabs)
- Follow Python best practices (PEP 8)
- Comment complex logic
- Ensure responsive design compatibility

### Testing

- Test image upload functionality
- Verify API integrations work correctly
- Check responsive design on multiple devices
- Validate accessibility features

---

## Roadmap

- [ ] User account system
- [ ] Recipe favorites and history
- [ ] Dietary restriction filters
- [ ] Nutritional information display
- [ ] Shopping list generation
- [ ] Mobile app development

---

## Known Issues

- Large image files may take longer to process
- API rate limits may affect heavy usage
- Some exotic ingredients may not be recognized accurately

---

## Support

For support, feature requests, or bug reports:

- Email: support@hoosierhelper.com
- Issues: [GitHub Issues](https://github.com/MicahSamuel77/XTernHackathonRecipeApp/issues)

---

## Acknowledgments

- OpenAI for providing the Vision and GPT APIs
- Contributors and beta testers
- Indiana University community for inspiration

---

**Made with ❤️ for Hoosiers everywhere**
