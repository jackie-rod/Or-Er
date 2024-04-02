from flask import Flask, request, render_template
from flask.helpers import flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        lines = text.split("\n")
        groups = [lines[i:i + 50] for i in range(0, len(lines), 50)]
        results = [" or ".join(group) for group in groups]
        return render_template('index.html', results=results)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)