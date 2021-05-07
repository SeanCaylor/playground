from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return "No page there, homie"

@app.route('/')
def hello_world():
    return "Oh, hello. Look at the earth... I know what you're thinking... 'Thats a pretty sweet earth'WRONG"

@app.route('/play')
def playground1(color = "blue", number = 3):
    return render_template('index.html', color = color, number = number)

@app.route('/play/<int:number>')
def playground2(color = "blue", number = 3):
    return render_template('index.html', color = color, number = number)

@app.route('/play/<int:number>/<string:color>')
def playground3(color = "blue", number = 3):
    return render_template('index.html', color = color, number = number)


if __name__ == "__main__":
    app.run(debug = True)