# receive-post

Describe your project here.

```sh
curl -X POST -d 'text=Hello, World!' http://localhost:5000
```

```sh
ngrok http http://127.0.0.1:5000
```

```sh
curl -X POST -d 'text=Hello, World!' https://d674-122-210-136-202.ngrok-free.app/
```

```sh
curl -X POST http://localhost:5000/test -H "Content-Type: application/json" -d '{"param1":"value1", "param2":"value2"}'
```

```sh
curl -X POST  https://d674-122-210-136-202.ngrok-free.app/test -H "Content-Type: application/json" -d '{"from":"ngrok", "text":"hoge"}'
```
