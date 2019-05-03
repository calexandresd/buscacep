# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def busca():
    return render_template('busca.html')


@app.route('/resposta', methods=['POST'])
def resposta():
    cep = request.form['cep']
    r = requests.get('https://api.postmon.com.br/v1/cep/'+cep+'')
    cep1 = r.json()
    rua = cep1['logradouro']
    bairro = cep1['bairro']
    cidade = cep1['cidade']
    estado = cep1['estado']
    return render_template('resposta.html', cep=cep, rua=rua,
     bairro=bairro, cidade=cidade, estado=estado)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
