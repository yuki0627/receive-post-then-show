from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST'])
def display_post():
    text = request.form['text']
    return text

if __name__ == '__main__':
    app.run()
