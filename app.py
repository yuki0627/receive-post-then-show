from flask import Flask, request, render_template_string,render_template

app = Flask(__name__)

# メモリにデータを保存するための変数
received_data = {}

@app.route('/test', methods=['POST'])
def test_endpoint():
    global received_data
    # リクエストからパラメータを取得
    # data = request.form.to_dict()  # formデータの場合
    data = request.json  # JSONデータの場合
    received_data = data  # 受け取ったデータをメモリに保存
    print(data)
    print(received_data)
    return "パラメータを受け取りました。"

@app.route('/')
def display_data():
    global received_data
    print(received_data)
    return render_template("index.html", data=received_data)

if __name__ == '__main__':
    app.run(debug=True)