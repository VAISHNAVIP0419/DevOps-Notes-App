from flask import Flask, render_template

app = Flask(__name__)

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for notes pages
@app.route('/notes/<topic>')
def notes(topic):
    return render_template('notes.html', topic=topic)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
