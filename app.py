from flask import Flask, request, render_template_string,render_template

app = Flask(__name__)

# メモリにデータを保存するための変数
received_data_list = []

@app.route('/test', methods=['POST'])
def test_endpoint():
    global received_data_list
    # リクエストからパラメータを取得
    # data = request.form.to_dict()  # formデータの場合
    data = request.json  # JSONデータの場合
    received_data_list.insert(0, data)
    return "パラメータを受け取りました。"

@app.route('/')
def display_data():
    global received_data_list
    return render_template("index.html", received_data_list=received_data_list)

if __name__ == '__main__':
    app.run(debug=True)