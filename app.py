from flask import Flask,render_template, request
from testing import getAkeyFromGoogle as koena
import google.generativeai as genai

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/callgemini")
def geminicall():
    q=request.args.get("question")
    key=koena()
    genai.configure(api_key=key)
    model=genai.GenerativeModel("gemini-2.0-flash")
    response=model.generate_content(q)
    return render_template("gemini_response.html", response_text=response.text)
    

if __name__=='__main__':
    app.run(debug=True)