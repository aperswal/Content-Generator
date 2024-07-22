# AI SEO Blog Generator

## Overview

The AI SEO Blog Generator is a powerful tool that leverages artificial intelligence to create SEO-optimized blog posts quickly and efficiently. This project uses OpenAI's GPT model for content generation and the Pexels API for sourcing relevant images, producing engaging and visually appealing blog posts.

## Features

- **AI-Driven Content Creation**: Utilizes OpenAI's GPT model to generate SEO-optimized blog content.
- **Advanced Copywriting Techniques**: Incorporates AIDA and PAS frameworks, storytelling, and other persuasive writing principles.
- **Keyword Optimization**: Strategically uses provided keywords based on search volume and competition.
- **Dynamic Image Sourcing**: Automatically fetches and incorporates relevant images from Pexels.
- **Robust Image Handling**: Implements retry mechanisms and fallbacks for image sourcing.
- **Customizable Blog Structure**: Allows for flexible blog post creation with customizable sections and word counts.
- **Purpose-Driven Content**: Tailors content to specific marketing goals or purposes.

## Project Structure

```
project_root/
│
├── templates/
│   ├── index.html
├── web_interface.py
├── main.py
├── Content_Creation.py
├── Image.py
├── requirements.txt
└── README.md
```

## Setup and Deployment

### Prerequisites
- Python 3.x

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/aperswal/content-generator.git
   cd content-generator
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with necessary API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   PEXELS_API_KEY=your_pexels_api_key
   ```

## Usage

1. Navigate to the deployed website URL.
2. Enter the blog topic, purpose, and keywords in the provided form.
3. Specify the number of sections and words per section.
4. Click "Generate Blog Post" to start the process.
5. Monitor the progress bar for status updates.
6. Download the generated blog post when complete.

## Contributing

Contributions to improve the AI SEO Blog Generator are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- OpenAI for providing the GPT model
- Pexels for the image API
