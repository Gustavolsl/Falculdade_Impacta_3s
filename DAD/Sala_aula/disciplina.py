from flask import Flask, jsonify, request
import util
app = Flask(__name__)
import disciplina

@app.route('/')
def all():
    return jsonify(database)

@app.route('/reseta', methods=['POST'])
def reseta():
    util.reseta()
    return 'banco resetado'
    

@app.route('/disciplinas', methods=['GET'])
def disciplina():
    return jsonify(util.all_for_database('DISCIPLINA'))

@app.route('/disciplinas/<int:id_disciplina>', methods=['GET'])
def get_disciplina(id_disciplina):
    try: 
        disciplina = util.localiza(id_disciplina,'DISCIPLINA')
        return jsonify(disciplina)
    except util.NotFoundError:
        return jsonify({'erro':'disciplina nao encontrada'}),400

@app.route('/disciplinas/<int:id_disciplina>', methods=['DELETE'])
def deleta_disciplina(id_disciplina):
    try: 
        disciplina = util.localiza(id_disciplina,'DISCIPLINA')
        removido = util.remove(disciplina,'DISCIPLINA')
        return jsonify(removido)
    except util.NotFoundError:
        return jsonify({'erro':'disciplina nao encontrada'}),400

@app.route('/disciplinas/<int:id_disciplina>', methods=['PUT'])
def edita_aluno(id_disciplina):
    try: 
        disciplina = util.localiza(id_disciplina,'DISCIPLINA')
        nova_disciplina = request.json
        if 'nome' not in nova_disciplina:
            return jsonify({'erro':'disciplina sem nome'}),400
        for key in disciplina:
            if key in nova_disciplina:
                disciplina[key] = nova_disciplina[key]
        return jsonify(disciplina)
    except util.NotFoundError:
        return jsonify({'erro':'disciplina nao encontrada'}),400

#'plano_ensino':'dados','carga_horaria'
@app.route('/disciplinas', methods=['POST'])
def nova_disciplina():
    print('ola')
    nova_disciplina = request.json
    print(request.method)
    if 'nome' not in nova_disciplina:
        return jsonify({'erro':'disciplina sem nome'}),400
    if 'id' not in nova_disciplina:
        return jsonify({'erro':'disciplina sem id'}),400


    '''
     resposta,erro = util.verifica_campos(nova_disciplina,campos_inteiros=['id','status','plano_ensino','carga_horaria'],
    campos_texto=['plano_ensino','nome'],campos_opcionais=['id_coordenador'])
    if resposta == False:
        return erro, 400
    '''
    try:
        disciplina = util.localiza(nova_disciplina['id'],'DISCIPLINA')
        return jsonify({'erro':'id ja utilizada'}),400
    except util.NotFoundError:
        pass

    util.adiciona(nova_disciplina,'DISCIPLINA')
    return jsonify(util.all_for_database('DISCIPLINA'))


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)


