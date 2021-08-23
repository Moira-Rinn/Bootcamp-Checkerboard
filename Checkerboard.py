from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def board(x=8, y=8):
    return render_template('board.html', x=int(x), y=int(y))


@app.route('/<y>')
def boardX(y, x=8):
    return render_template('board.html', x=int(x), y=int(y))


@app.route('/<x>/<y>')
def boardXy(x, y):
    return render_template('board.html', x=int(x), y=int(y))


if __name__ == "__main__":
    app.run(debug=True)
