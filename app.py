#Autor: Olavo M

from flask import Flask, render_template, request, redirect 
#import somente do necessario para a interface web

app = Flask(__name__)

class Noh: #clase do no, contendo seu valor e o ponteiro para o proximo
    def __init__(self, valor):
        self.valor = valor #o valor pode ser de qualquer tipo, mas tratei como string (nos inputs e demais funcoes)
        self.proximo = None

class ListaEncadeada: #classe da lista encadeada simples
    def __init__(self): #eh iniciada sem valor
        self.prim=None
        self.qtdNoh=0
    def insere(self, valor):
        if self.qtdNoh==0: #caso seja o primeiro valor, eh definido como prim
            self.prim=Noh(valor)
            self.qtdNoh+=1
        else: #acrescenta os demais valores, percorrendo a lista ate o final
            nohAtual = self.prim
            while nohAtual.proximo != None:
                nohAtual = nohAtual.proximo
            nohAtual.proximo = Noh(valor)
            self.qtdNoh+=1
    def imprime(self): #retorna uma string com os valores da lista, para depois serem impressos
        cursor = self.prim
        resultado = ""
        while cursor != None:
            resultado += (str(cursor.valor)+" ")
            cursor = cursor.proximo
        return resultado
    def inverte(self): #inverte em O(n) com tres ponteiros auxiliares
        P_Anterior = None 
        P_Atual = self.prim 
        P_Prox = self.prim.proximo
        while P_Prox != None: #percorre a lista ate o ultimo elemento
            P_Atual.proximo = P_Anterior #inverte o ponteiro proximo, um por um
            P_Anterior = P_Atual
            P_Atual = P_Prox
            P_Prox = P_Prox.proximo
        P_Atual.proximo = P_Anterior #finaliza a operacao no ultimo elemento
        self.prim = P_Atual #define o novo primeiro elemento
        return P_Atual #retorna a noh da cabeca da lista resultante para cumprir com o enunciado, entretanto o valor do retorno devido a linguagem utilizada e o codigo escrito nao sera utilizado

Lista = ListaEncadeada()

@app.route("/", methods=['POST', 'GET'])
def index():    
    if request.method == "POST": #adiciona o valor na lista, passado por parametro pelo form
        var = request.form["valor"]
        Lista.insere(var)
        print(Lista.imprime())
        return redirect("/")
    else:
        if request.args.get("inverter"): #se o botao inverter for acionado, o metodo eh chamado
            Lista.inverte()
        texto = Lista.imprime()
        return render_template("index.html", elementos=texto)

if __name__ == "__main__":
    app.run()