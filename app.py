from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 'About me' is the home page
    return render_template('About_me.html', title="About Me")

@app.route('/projects')
def projects():
    return render_template('Projects.html', title="Projects")

@app.route('/portfolio')
def portfolio():
    return render_template('Portfolio.html', title="Portfolio")

if __name__ == '__main__':
    app.run(debug=True)