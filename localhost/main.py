from flask import Flask, render_template_string, request, redirect
import subprocess

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Shutdown Server</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding-top: 50px; }
        button {
            font-size: 24px;
            padding: 20px 40px;
            background-color: red;
            color: white;
            border: none;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <h1>Shutdown Server</h1>
    <form method="post">
        <button type="submit">Shutdown Now</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def shutdown():
    if request.method == "POST":
        subprocess.Popen(["sudo", "shutdown"])
        return "Server is shutting down..."
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
