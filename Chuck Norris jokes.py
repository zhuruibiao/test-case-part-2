from flask import Flask, render_template, redirect
import urllib.request, json



app = Flask(__name__)
app.config['SECRET_KEY'] = '1271628bb0b13ce0c676dfde280ba245'

with urllib.request.urlopen("http://api.icndb.com/jokes/random/10") as url:
    data = json.loads(url.read().decode())
    print(data)
    connectType = data['type']
    print(connectType)
    jokes = data['value']
    print(jokes)


@app.route("/")

@app.route("/getJokes")
def getJokes():

    return render_template('getJokes.html', jokes=jokes)

@app.route("/flushJokes")
def flushJokes():

    global jokes
    jokes=[]

    return render_template('flushJokes.html', jokes=jokes)

@app.route("/getNewJokes")
def getNewJokes():
    with urllib.request.urlopen("http://api.icndb.com/jokes/random/10") as url:
        data = json.loads(url.read().decode())
        value = data['value']

    return render_template('getNewJokes.html', jokes=value)

if __name__ == '__main__':
    app.run(debug=True)
