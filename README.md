# Automated Blog Content and Image Generation Tool

This project consists of an automated system for generating blog content and downloading relevant images using the Pexels API. The system leverages AI-driven content creation to produce engaging blog posts and automatically sources related images to complement the text.

## Modules

- `main.py`: The primary script that orchestrates the blog creation process. It uses other modules to generate content and images.
- `content_creation.py`: Handles the generation of blog content using OpenAI's GPT model.
- `image.py`: Manages the downloading of images from Pexels based on queries derived from the blog content.

## Features

- **Automated Blog Content Creation**: Leverages OpenAI's GPT model to generate engaging and relevant blog content.
- **Dynamic Image Sourcing**: Automatically downloads images from Pexels that match the blog's content.
- **Unique Image Download**: Ensures that the same image is not downloaded multiple times, even if repeated queries are made.
- **Customizable Blog Structure**: Facilitates the creation of blogs with custom headlines, topics, and calls to action.

## Requirements

- Python 3.x
- `python-docx` library for creating Word documents.
- `requests` library for handling HTTP requests.
- `pexels_api` Python wrapper for interacting with the Pexels API.
- `python-dotenv` for managing environment variables.
- OpenAI and Pexels API keys.

## Setup

1. **Install Dependencies**: Run `pip install python-docx requests pexels_api python-dotenv` to install the required Python libraries.
2. **API Keys**: Ensure that you have valid API keys from OpenAI and Pexels. Place them in a `.env` file in your project directory.
3. **Environment Variables**: Use `python-dotenv` to load API keys from your `.env` file.

## Usage

1. Run `main.py` to start the blog creation process.
2. Follow the prompts to input product information and desired blog structure.
3. The script generates the blog content and downloads relevant images, saving them in the specified directory.
4. The final blog content is saved in a Word document.
