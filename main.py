from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return render_template("home.html", aktiva_lapa ="home")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/contacts')
def contacts():
  return render_template("contacts.html")

@app.route('/params')
def params():
  args = request.args
  for key, value in args.items():
    print(f"{key}:{value}")
  return args

@app.route('/params_table')
def params_table():
  args = request.args
  return render_template('params_table.html', args = args)

@app.route('/')
def index_lapa():
  return render_template('chats2.html')

@app.route('/chats2/lasi')
def ielasit_chatu():
  chata_rindas = []
  with open("chats2.txt", "r", encoding="UTF-8") as f:
    for rinda in f:
      chata_rindas.append(rinda)
  return jsonify({"chats": chata_rindas})


@app.route('/chats2/suuti', methods=['POST'])
def suutiit_zinju():
  dati = request.json
  
  with open("chats2.txt", "a", newline="", encoding="UTF-8") as f:
    f.write(dati["chats"] + "\n")

  return ielasit_chatu()

@app.route('/chat')
def chat():
  return render_template("chat.html")

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, threaded = True, debug = True)
