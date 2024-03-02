from flask import Flask, request, render_template_string

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
    # メモリに保存されたデータを表示
    global received_data
    print(received_data)
    return render_template_string("""
        <h1>受け取ったデータ</h1>
        {% if data %}
            <ul>
            {% for key, value in data.items() %}
                <li>{{ key }}: {{ value }}</li>
            {% endfor %}
            </ul>
        {% else %}
            <p>データがありません。</p>
        {% endif %}
    """, data=received_data)

if __name__ == '__main__':
    app.run(debug=True)