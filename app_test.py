#Autor: Olavo Marini

from unittest import TestCase
from app import Noh, ListaEncadeada

class TesteLista(TestCase):
    def teste_insere(self): #teste do metodo insere()
        Lista = ListaEncadeada()
        listaComp = []

        for i in range(10):
            Lista.insere(i)
            listaComp.append(i)
        
        cursor = Lista.prim
        for i in range(10):
            self.assertEqual(cursor.valor, listaComp[i])
            cursor = cursor.proximo
    
    def teste_imprime(self): #teste do metodo imprime()
        Lista = ListaEncadeada()
        textoComp = ""
        for i in range(10):
            Lista.insere(i)
            textoComp += (f"{i} ")
        
        self.assertEqual(Lista.imprime(), textoComp)
    
    def teste_inverte(self): #teste do metodo inverte()
        Lista = ListaEncadeada()
        listaComp = []

        for i in range(10):
            Lista.insere(i)
            listaComp.append(i)
        
        Lista.inverte()
        listaComp.reverse()

        cursor = Lista.prim
        for i in range(10):
            self.assertEqual(cursor.valor, listaComp[i])
            cursor = cursor.proximo
