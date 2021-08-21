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

# To be implemented:

# @app.route('/<x>/<y>/<color1>/<color2>')
# def contact(x, y, color1=[12, 11, 11, 0.4], color2=[136, 0, 0, 0.4]):
#     return render_template('repeat.html', x=int(x), y=int(y), color1=list(color1), color2=list(color2))


if __name__ == "__main__":
    app.run(debug=True)
