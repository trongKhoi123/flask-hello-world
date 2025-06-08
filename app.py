from flask import Flask, render_template_string

app = Flask(__name__)

# Giao diện đã chỉnh màu và nội dung
base_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #1e2a38;
            color: #f0f0f0;
        }
        nav a {
            margin-right: 15px;
            color: #4fc3f7;
            text-decoration: none;
        }
        nav a:hover {
            text-decoration: underline;
        }
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
                                  heading="Chào mừng Mai Trọng Khôi - 22dh111734",
                                  message="Đây là trang chủ để test lab 3.")

@app.route('/about')
def about():
    return render_template_string(base_template,
                                  title="About Page",
                                  heading="Giới thiệu",
                                  message="Đây là một web test đơn giản dùng Flask.")

if __name__ == '__main__':
    app.run(debug=True)
