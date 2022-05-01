from flask import Flask,render_template,request
from geopy.geocoders import Nominatim
app = Flask(__name__)



def localizar(palavraChave):
    try:
        loc = Nominatim(user_agent="GetLoc") 
        getLoc = loc.geocode(palavraChave) 
        print(getLoc.address)
        return getLoc
    except:
        loc = Nominatim(user_agent="GetLoc") 
        getLoc = loc.geocode("Avenida Rudge 315 Bom Retiro São Paulo") 
        return getLoc
    



@app.route('/', methods=['GET','POST'])
def mapa():
    if request.method == 'POST':
        enderecoForm = request.form['endereco']
        loc = localizar(enderecoForm)
        return render_template('index.html', localizacao = loc)
    return render_template('index.html', localizacao = localizar("Avenida Rudge 315 Bom Retiro São Paulo"))

if __name__ == '__main__':
    app.run(debug = True)    