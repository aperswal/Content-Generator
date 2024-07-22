from flask import Flask, render_template, request, send_file, jsonify
from main import generate_blog_post
import threading
import time
import os
import json

app = Flask(__name__)

# Global variables to store the generation progress and file path
progress = 0
status_message = "Waiting to start..."
generated_file_path = ""
error_message = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    global progress, status_message, generated_file_path, error_message
    progress = 0
    status_message = "Starting blog generation..."
    generated_file_path = ""
    error_message = ""

    topic = request.form['topic']
    keywords = request.form['keywords']
    purpose = request.form['purpose']
    section_count = int(request.form['section_count'])
    words_per_section = int(request.form['words_per_section'])

    # Start the blog generation in a separate thread
    threading.Thread(target=generate_blog_post_thread, args=(topic, keywords, purpose, section_count, words_per_section)).start()

    return jsonify({"message": "Blog generation started"})

@app.route('/progress')
def get_progress():
    global progress, status_message, error_message
    return jsonify({"progress": progress, "status": status_message, "error": error_message})

@app.route('/download')
def download():
    global generated_file_path
    if generated_file_path and os.path.exists(generated_file_path):
        return send_file(generated_file_path, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404

def generate_blog_post_thread(topic, keywords, purpose, section_count, words_per_section):
    global progress, status_message, generated_file_path, error_message

    def update_progress(new_progress, message):
        global progress, status_message
        progress = new_progress
        status_message = message

    try:
        # Parse keywords JSON string to a Python object
        keywords_list = json.loads(keywords)
        # Convert the Python object back to a properly formatted string
        keywords_str = json.dumps(keywords_list)
        
        # Call your existing blog generation function here
        generated_file_path = generate_blog_post(topic, keywords_str, purpose, section_count, words_per_section, update_progress)
    except json.JSONDecodeError as e:
        error_message = f"Error parsing keywords JSON: {str(e)}\nPlease check your JSON format and try again."
        update_progress(100, "Error occurred")
        print(error_message)
    except Exception as e:
        error_message = f"Error in blog post generation: {str(e)}"
        update_progress(100, "Error occurred")
        print(error_message)

if __name__ == '__main__':
    app.run(debug=True)