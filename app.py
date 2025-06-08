from flask import Flask, render_template_string

app = Flask(__name__)

# Template HTML dùng cho tất cả các trang
base_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        nav a { margin-right: 10px; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
    </nav>
    <h1>{{ heading }}</h1>
    <p>{{ message }}</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(base_template,
                                  title="Home Page",
                                  heading="Chào mừng bạn đến với Mai Trong Khoi App!",
                                  message="Đây là trang chủ để test Lab3.")

@app.route('/about')
def about():
    return render_template_string(base_template,
                                  title="About Page",
                                  heading="Giới thiệu",
                                  message="Đây là một web test đơn giản dùng Flask.")

if __name__ == '__main__':
    app.run(debug=True)
