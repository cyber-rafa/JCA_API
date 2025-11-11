from flask import Flask, jsonify, request

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

app.route('/alunos', methods=['GET'])  
def get_alunos():
    return jsonify(alunos)


app.route('/alunos', methods=['POST'])
def insort_aluno():
    novo_aluno = request.get_json()
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201
