from flask import Flask, json, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index_lapa():
  return render_template('chats.html', aktiva_lapa ="chats")

@app.route('/home')
def home():
  return render_template("home.html", aktiva_lapa ="home")

@app.route('/about')
def about():
  return render_template("about.html", aktiva_lapa ="about")

@app.route('/contacts')
def contacts():
  return render_template("contacts.html", aktiva_lapa ="contacts")

@app.route('/testingarea')
def testingarea():
  return render_template("testingarea.html", aktiva_lapa ="testingarea")

@app.route('/health')
def health_check():
  return "OK"


@app.route('/chats/lasi')
def ielasit_chatu():
  chata_rindas = []
  with open("chats.txt", "r", encoding="UTF-8") as f:
    for rinda in f:
      chata_rindas.append(rinda)
  return jsonify({"chats": chata_rindas})


@app.route('/chats/suuti', methods=['POST'])
def suutiit_zinju():
  dati = request.json
  
  with open("chats.txt", "a", newline="", encoding="UTF-8") as f:
    f.write(dati["chats"] + "\n")

  return ielasit_chatu()
  

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(host='0.0.0.0', port = 5000, threaded = True, debug = True)