from models import startDB,app,Voter,Aspirant
from flask import request,jsonify,abort,render_template

startDB()

@app.route('/')
@app.route('/home')
def index():
    return render_template('pages/home.html')

@app.route('/vote')
def render_vote():
    return render_template('pages/vote.html')
@app.route('/cast-vote')
def render_cast_vote():
    return render_template('pages/cast-vote.html')
if __name__ == "__main__":
    app.run(debug=True)