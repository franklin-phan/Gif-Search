from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    query = request.args.get('query')
    # b) your API key, 'key'
    apikey = "JWEOV1L8X0N2"

    # c) how many GIFs to return, 'limit'
    lmt = 9

    # params dictionary
    params = {
        "q": query,
        "key": apikey,
        'limit': lmt
        }

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    r = requests.get("https://api.tenor.com/v1/search", params)

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", gifs = gifs)

@app.route('/trending')
def trending():
    #parameters dictionary for trending
    params = {
        "key": 'JWEOV1L8X0N2',
        'limit': 9
        }
    #gets trending gifs
    r = requests.get("https://api.tenor.com/v1/trending", params)
    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None
    #returns trending to index.html and gifs
    return render_template('index.html', gifs = gifs)

@app.route('/random')
def random():
    #parameters dictionary for trending
    query = request.args.get('query')

    params = {
        "q": query,
        "key": 'JWEOV1L8X0N2',
        'limit': 9
        }
    #gets trending gifs
    r = requests.get("https://api.tenor.com/v1/random?", params)
    if r.status_code == 200:
        gifs = json.loads(r.content)['results']
    else:
        gifs = None
    #returns random to index.html and gifs
    return render_template('index.html', gifs = gifs, query=query)


if __name__ == '__main__':
    app.run(debug=True)

#spaghetti
