from flask import Flask,render_template,request
from geopy.geocoders import Nominatim
app = Flask(__name__)



def localizar(palavraChave):
    loc = Nominatim(user_agent="GetLoc") 
    getLoc = loc.geocode(palavraChave) 
    print(getLoc.address) 
    print("Latitude = ", getLoc.latitude, "\n") 
    print("Longitude = ", getLoc.longitude) 
    return getLoc
    



@app.route('/', methods=['GET','POST'])
def map_func():
    if request.method == 'POST':
        enderecoForm = request.form['endereco']
        loc = localizar(enderecoForm)
        return render_template('index.html', localizacao = loc)

    return render_template('index.html', localizacao = localizar("São Paulo"))

if __name__ == '__main__':
    app.run(debug = True)    