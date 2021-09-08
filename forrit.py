
from flask import Flask, render_template, json
import urllib.request 

app = Flask(__name__)

with urllib.request.urlopen("https://restcountries.eu/rest/v2/all") as url:
    gogn = json.loads(url.read().decode())


@app.route("/")
def index():
    return render_template('INDEX.html', listi = gogn)

@app.route('/country/<val>')
def land(val):

    for i in gogn:
        if i['alpha2Code'] == val:
            land = i 
            
    return render_template('LAND.html', listi = gogn, land = land)

@app.route("/region/<heimsalfa>")
def region(heimsalfa):
    heimsalfur=[]
    counter = 0

    for i in gogn:
        if i['region'] == heimsalfa:
            counter=counter+1
            region = i 
            heimsalfur.append(i)

            

    return render_template('heimsalfa.html', listi = gogn, heimsalfur = heimsalfur, counter = counter)

@app.errorhandler(404)
def villa(e):
    return render_template('error.html')
    

if __name__ == '__main__':
    app.run(debug=True)
