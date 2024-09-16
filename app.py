from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de animes inicial
animes = [
    {"nome": "Naruto", "genero": "Ação", "episodios": 500},
    {"nome": "One Piece", "genero": "Aventura", "episodios": 1000},
]

@app.route('/')
def index():
    return render_template('index.html', animes=animes)

@app.route('/add', methods=['GET', 'POST'])
def add_anime():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        episodios = request.form['episodios']
        animes.append({"nome": nome, "genero": genero, "episodios": episodios})
        return redirect(url_for('index'))
    return render_template('add_anime.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
