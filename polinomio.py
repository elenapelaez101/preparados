class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
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
        else:
            actual = polinomio.termino_mayor
            actual-polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual- actual.sig
            aux.sig-actual.sig
            actual.sig - aux

    def modificar_termino(polinomio ,termino, valor):
        aux = polinomio.termino_mayor
        while aux is not None and aux.info.termino != termino:
            aux = aux.sig
            aux.info.valor = valor

    def obtener_valor(polinomio, termino):
        aux= polinomio.termino_mayor
        if aux is not None and aux.info.termino > termino:
            aux = aux.sig
        elif aux is not None and aux.info.termino == termino:
            return aux.info.valor
        else:
            return 0

    def mostrar(polinomio):
        aux = polinomio.termino_mayor
        pol = ""
        signo = ""
        if aux.info.valor >= 0:
            signo += "+"
            pol += signo + str(aux.info.valor) + "x**" + str(aux.info.termino)
        else:
            return pol

p1 = Polinomio()
p2 = Polinomio()
print(p1)
print(p2)
