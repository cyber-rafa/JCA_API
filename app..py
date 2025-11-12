from builtins import enumerate
from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

alunos = [

    {   "id": 1,
        "nome": "Ramon",
        "idade": 20
    },
    {   "id": 2,
        "nome": "Marllon",
        "idade": 22
    },
    {
        "id": 3,
        "nome": "Mathues",
        "idade": 22
    },
    {
        "id": 4,
        "nome": "Rafael",
        "idade": 19
    }
]

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/alunos', methods=['GET'])  
def get_alunos():
    return jsonify(alunos)  


@app.route('/alunos', methods=['POST'])
def insort_aluno():
    novo_aluno = request.get_json()
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

@app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    for indice, aluno in enumerate(alunos):
        if aluno['id'] == aluno_id:
            del alunos[indice]
        return jsonify(), 200
    
@app.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    aluno_atualizado = request.get_json()
    for indice, aluno in enumerate(alunos):
        if aluno['id'] == aluno_id:
            alunos[indice].update(aluno_atualizado)
            return jsonify(alunos[indice]), 200
    return jsonify({'mensagem': 'Aluno não encontrado!'}), 404

app.run(port=5000,host='localhost',debug=True)
