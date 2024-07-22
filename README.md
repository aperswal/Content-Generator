<<<<<<< HEAD
# ContentGen

## Go to Master Branch

###Website at https://github.com/aperswal/contentgen-website
=======
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
- **AWS Amplify Integration**: Ready for deployment on AWS Amplify for scalable, serverless operation.

## Project Structure

```
project_root/
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── amplify/
│   └── backend/
│       └── function/
│           └── blogGenerator/
│               ├── src/
│               │   ├── index.py
│               │   ├── main.py
│               │   ├── Content_Creation.py
│               │   └── Image.py
│               └── requirements.txt
│
├── amplify.yml
└── README.md
```

## Setup and Deployment

### Prerequisites

- Node.js and npm
- AWS Account
- AWS Amplify CLI
- Python 3.x

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-seo-blog-generator.git
   cd ai-seo-blog-generator
   ```

2. Install dependencies:
   ```
   pip install -r amplify/backend/function/blogGenerator/src/requirements.txt
   ```

3. Set up your `.env` file with necessary API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   PEXELS_API_KEY=your_pexels_api_key
   ```

### AWS Amplify Deployment

1. Install and configure the AWS Amplify CLI.

2. Initialize the Amplify project:
   ```
   amplify init
   ```

3. Add API and Lambda function:
   ```
   amplify add api
   ```

4. Add storage (DynamoDB and S3):
   ```
   amplify add storage
   ```

5. Deploy backend resources:
   ```
   amplify push
   ```

6. Set up frontend hosting:
   ```
   amplify add hosting
   ```

7. Publish the application:
   ```
   amplify publish
   ```

8. Update the API Gateway URL in `frontend/script.js` with the provided URL after deployment.

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
- AWS for the Amplify platform and serverless technologies
>>>>>>> 0b09e2f (improved tremendously)
