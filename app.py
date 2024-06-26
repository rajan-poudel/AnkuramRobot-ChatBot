#Importing libraries
from flask import Flask , render_template ,request,redirect
import webbrowser
import google.generativeai as genai

#Gemini
import os
my_api_key_gemini = os.getenv('my_new_api_key_here')

genai.configure(api_key=my_api_key_gemini)

# Automatic opening in browser
# url = ""
# webbrowser.open(url)

#Flask app
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = prompt
            response = model.generate_content(question)

            if response.text:
                return response.text
            else:
                return "Sorry, but I think Gemini didn't want to answer that!"
        except Exception as e:
            return "Sorry, but Gemini didn't want to answer that!"

    return render_template('index.html', **locals())
