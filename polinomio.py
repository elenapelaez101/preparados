class datopolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1
    
    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if(termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino