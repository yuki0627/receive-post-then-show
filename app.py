from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST'])
def display_post():
    print("Headers:", request.headers)
    print("Body:", request.get_data(as_text=True))
    text = request.form['text']
    return text

@app.route('/test', methods=['POST'])
def test_endpoint():
    # リクエストからパラメータを取得
    # data = request.form.to_dict()  # formデータの場合
    data = request.json  # JSONデータの場合
    print(data)
    return "パラメータを受け取りました。"

if __name__ == '__main__':
    app.run(debug=True)
