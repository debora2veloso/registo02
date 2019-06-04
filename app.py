from flask import Flask, render_template ,request

app = Flask(__name__)

def gravar():
    import sqlite3
    ficheiro = sqlite3.connect('db/Utilizadores.db')
    db = ficheiro.cursor()
    db.execute("CREATE TABEL IF NOT EXISTS urs (nome text, email text, passe text)")
    db.execute("INSER INTO usr VALUES (?,?,?)", (v1,v2,v3))
    ficheiro.commit()
    ficheiro.close()

def alterar():
    import sqlite3
    ficheiro = sqlite3.connect('db/Utilizadores.db')
    db = ficheiro.cursor()
    db.execute("UPDATE usr SET passe = ? WHERE nome = ?",(v2, v1))
    ficheiro.commit()
    ficheiro.close()

@app.route('/registo',  methods=['Get', 'Post'])
def route():
    erro = None
    if request.method == 'Post':
        v1 = request.form['utilizador']
        v3 = request.form['passe']
        v4 = request.form['cpasse']
        if v3 != v4:
            erro = 'A palavra passe não coincide.'
        else:
            alterar(v1, v3)
    return render_template('registo.html', erro=erro)

@app.route('/', methods=['Get', 'Post'])
def newpasse ():
    erro = None
    if request.method == 'Post':
        v1 = request.form['utilizador']
        v2 = request.form['email']
        v3 = request.form['passe']
        v4 = request.form['cpasse']
        if v3 != v4:
            erro = 'A palavra passe não coincide.'
        else:
            alterar(v1, v2, v3)
    return render_template('registo.html', erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
