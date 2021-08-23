import re
from xml.dom import minidom
import os
import graphviz

j=1 
class Nodo:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        self.up = None
        self.down = None
class NodoGround:
    def __init__(self,data):
        self.data = data
        self.next = None
class ListGround:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def Empty(self):
        return self.first == None
    def AddFinal(self, data):
        if self.Empty():
            self.first = self.last = NodoGround(data)
        else:
            temp = self.last
            self.last = temp.next = NodoGround(data)
        self.size += 1
    def SeachGround(self, name):
        temp = self.first
        while temp:
            if self.Empty():
                print("Vacia")
            else:
                if temp.data.getName() == name:
                    return temp.data
                else:
                    if temp == self.last: 
                        print("No se encontro un terreno con el nombre "+name)
                    else:
                        temp = temp.next
class Area :
    def __init__(self,comb,coorx, coory):
        self.comb = comb
        self.coorx = coorx
        self.coory = coory
class Ground:
    def __init__(self,name,bX,bY,fX,fY):
        self.nameGround = name 
        self.raiz = Nodo(Area(None,None,None))
        self.beginX = bX
        self.beginY = bY
        self.finalX = fX
        self.finalY = fY
    def getName(self):
        return self.nameGround
    def NewAreaX(self,comb,coorX,coorY):
        global j 
        print("Nodo",j)
        j+=1
        print(coorX,coorY)
        if self.raiz.next == None:#Recorrido en X
            aux = Nodo(Area(None,coorX,None))
            self.raiz.next = aux
            aux.prev = self.raiz
            aux.down = auxtemp = Nodo(Area(comb,coorX,coorY))
            auxtemp.up = aux 
            self.NewAreaY(auxtemp, coorX,coorY)
            return
        else:
            aux = self.raiz.next
            while aux:
                if aux.data.coorx < int(coorX):
                    if aux.next == None:
                        print(coorX,coorY)
                        auxtemp = Nodo(Area(None,coorX,None))
                        aux.next = auxtemp 
                        auxtemp.prev = aux 
                        auxtemp.down  = nodoaux = Nodo(Area(comb,coorX,coorY))
                        nodoaux.up = auxtemp
                        self.NewAreaY(nodoaux, coorX,coorY)
                        return
                    else:
                        aux = aux.next
                elif aux.data.coorx == int(coorX):
                    aux = aux.down
                    while aux:
                        if aux.data.coory < int(coorY) :
                            if aux.down == None:
                                aux.down = nodoaux = Nodo(Area(comb,coorX,coorY)) 
                                nodoaux.up = aux
                                self.NewAreaY(nodoaux,coorX,coorY)
                                return

                            aux = aux.down    
                        elif aux.data.coory == coorY:
                            #aux = Nodo(Area(comb,coorX,coorY))
                            return
                        else:
                            auxtemp = aux.up
                            nodoaux = Nodo(Area(comb,coorX,coorY))
                            auxtemp.down = nodoaux
                            nodoaux.down = aux
                            aux.up = nodoaux
                            nodoaux.up = auxtemp
                            self.NewAreaY(nodoaux, coorX,coorY)
                            return

                        
                else:
                    print("entreenca",coorX,coorY)
                    auxtemp = aux.prev
                    auxtemp.next  = NodoEnc = Nodo(Area(None,coorX,None))
                    NodoEnc.next = aux
                    NodoEnc.prev = auxtemp
                    aux.prev = NodoEnc
                    NodoEnc.down = nodoaux = Nodo(Area(comb,coorX,coorY))
                    nodoaux.up = NodoEnc
                    self.NewAreaY(nodoaux, coorX,coorY)
                    return
                  
    def NewAreaY(self, auxNodo, coorX,coorY):
        
        if self.raiz.down == None:
            aux= Nodo(Area(None,None,coorY))
            aux.up = self.raiz
            self.raiz.down  = aux
            aux.next = auxNodo
            auxNodo.prev = aux
            return
        else:
            
            aux = self.raiz.down
            while aux:
                if aux.data.coory < int(coorY) :
                    if aux.down == None:
                        aux.down = auxtemp = Nodo(Area(None,None,coorY))
                        auxtemp.up = aux
                        auxtemp.next = auxNodo
                        auxNodo.prev = auxtemp
                        return
                    else:
                        aux = aux.down
                elif aux.data.coory == int(coorY) :

                    aux = aux.next
                    while aux :

                        if aux.data.coorx < coorX:
                            if aux.next == None:
                                aux.next = auxNodo
                                auxNodo.prev = aux
                                return

                                

                        else: 
                            auxtemp = aux.prev
                            auxtemp.next = auxNodo
                            aux.prev = auxNodo
                            auxNodo.prev = auxtemp
                            auxNodo.next = aux
                            return
                            
                        aux = aux.next   
                else:
                    auxtemp = aux.up
                    auxtemp.down = auxEnc = Nodo(Area(None, None, coorY))
                    auxEnc.up = auxtemp
                    auxEnc.down = aux
                    auxEnc.next = auxNodo
                    auxNodo.prev = auxEnc
                    return
    def GetRaiz(self):
        return self.raiz
   # def GetArea(self,nod):

Grounds = ListGround()


def MenuPricipal():
    print("Menu Principal")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiatne")
    print("5. Generar grafica")
    print("6. Salida")
    option = input()
    if option == "1":
        clearConsole()
        FileUpload()
    elif option == "2":
        clearConsole()
        processGround()
        return#ProcesarArchivo()
    elif option == "3":
        clearConsole()
        printSalida()
        
    elif option == "4":
        clearConsole()
        DataStudent()
    elif option == "5":
        clearConsole()
        return#Graficar()
    elif option == "6":
        clearConsole()
        exit()
    else:
        return
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
def DataStudent():
    print("Erick Daniel Ajche Hernandez")
    print("201701043")
    print("Introduccion a la Programacion y computacion seccion D")
    print("Ingenieria en Ciencias y Sistemas")
    print("4to Semestre")
    input()
    clearConsole()
    MenuPricipal()
def ProsFile():
    print("Ingresa el nombre del Terreno")
    name_ground = input()
def FileUpload():
    print("Ingresa la direccion de archivo")
    dx = input()
    mydoc = minidom.parse("p1.xml")
    grounds = mydoc.getElementsByTagName("terreno")
    for terrenos in grounds:
        NameG = terrenos.attributes['nombre'].value
        CoorI = terrenos.getElementsByTagName("posicioninicio")[0]
        coorx = CoorI.getElementsByTagName("x")
        Bx = coorx[0].firstChild.data
        coory = CoorI.getElementsByTagName("y")
        By = coory[0].firstChild.data
        CoorF = terrenos.getElementsByTagName("posicionfin")[0]
        coorx = CoorF.getElementsByTagName("x")
        Fx = coorx[0].firstChild.data
        coory = CoorF.getElementsByTagName("y")
        Fy = coory[0].firstChild.data
        Areas = terrenos.getElementsByTagName("posicion")
        ActualG = Ground(NameG,int(Bx),int(By),int(Fx),int(Fy))
        Grounds.AddFinal(ActualG)
        for Area in Areas:
            Px = Area.attributes['x'].value
            Py = Area.attributes['y'].value
            Comb = Area.firstChild.data
            ActualG.NewAreaX(int(Comb),int(Px),int(Py))
            #print("Posicion x "+Area.attributes['x'].value+", y "+Area.attributes['y'].value+" Combustible "+Area.firstChild.data)
    MenuPricipal()

def printSalida():
    print("Inserte el nombre de terreno que le interesa")
    nameg = input()
    AuxGround = Grounds.SeachGround(nameg)
    aux = AuxGround.raiz
    aux = aux.down
    while aux:
        auxf = aux.next
        while auxf:
            print("x: "+str(auxf.data.coorx)+" y: "+str(auxf.data.coory)+" C: "+str(auxf.data.comb))
            auxf = auxf.next
        aux = aux.down

    
             
    MenuPricipal()
def  graficGround():
    dot = graphviz.Digraph(comment='The Round Table')
    dot.edge('B', 'L', constraint='false')
    print(dot.source)
    dot.render('Terreno/Terreno2', view=True) 
def processGround():
    print("Inserte el nombre de terreno que le interesa")
    nameg = input()
    AuxGround = Grounds.SeachGround("terreno2")
    aux = AuxGround.raiz
    aux = aux.down
    print(AuxGround.beginX,AuxGround.beginY,AuxGround.finalX,AuxGround.finalY)
    while aux:
        if aux.data.coory == AuxGround.beginY:
            aux = aux.next
            while aux:
                if aux.data.coorx == AuxGround.beginY:
                    NodoInicio=aux
                    aux = AuxGround.raiz
                    aux = aux.down
                    print(NodoInicio.data.coorx,NodoInicio.data.coory)
                    while aux:
                        if aux.data.coory == AuxGround.finalY:
                            aux = aux.next
                            while aux:
                                if aux.data.coorx == AuxGround.finalX:
                                    NodoFinal=aux
                                    print(NodoInicio.data.coorx,NodoInicio.data.coory,NodoFinal.data.coorx, NodoFinal.data.coory)
                                    listCamino = camino(NodoInicio,NodoFinal)
                                    printCamino()                                    
                                aux = aux.next    
                        aux = aux.down
                aux = aux.next       
        aux = aux.down
def printCamino(Ground,listCamino):
    Ground

    

def camino(inicio,fin):
    lista = []
    resultado = caminoRecorrer(inicio,lista,fin)
    for c in resultado:
        print(c.data.coorx,c.data.coory)

def caminoRecorrer(actual,listaRecorridos,fin):
    if(actual is  None):
        return False
        
    if(actual.data.comb is None):
        return False

    if(actual==fin):
        listaRecorridos.append(actual)
        return listaRecorridos

    for item in listaRecorridos:
        if(item==actual):
            return  False


    nuevaLista = listaRecorridos.copy()
    nuevaLista.append(actual)


    camino1 = caminoRecorrer(actual.next,nuevaLista,fin)
    camino2 = caminoRecorrer(actual.prev,nuevaLista,fin)
    camino3 = caminoRecorrer(actual.up,nuevaLista,fin)
    camino4 = caminoRecorrer(actual.down,nuevaLista,fin)

    costoEvaluar1 = evaluarCosto(camino1)
    costoEvaluar2 = evaluarCosto(camino2)
    costoEvaluar3 = evaluarCosto(camino3)
    costoEvaluar4 = evaluarCosto(camino4)


    tupla1 = (costoEvaluar1,camino1)
    tupla2 = (costoEvaluar2,camino2)
    tupla3 = (costoEvaluar3,camino3)
    tupla4 = (costoEvaluar4,camino4)

    cmp1 = compararCosto(tupla1,tupla2)
    cmp2 = compararCosto(tupla3,tupla4)
    return compararCosto(cmp1,cmp2)[1]

def compararCosto(costo1,costo2):
    if(costo1[0] == False and costo2[0] == False):
        return (False,False)
    if(costo1[0] == False):
        return costo2
    if(costo2[0] == False):
        return costo1
    if(costo1[0]<=costo2[0]):
        return costo1
    else:
        return costo2

def evaluarCosto(lst):
    if(lst is False):
        return False

    costo = 0
    for cada in lst:
        if(cada.data.comb is not None):
            
            costo = costo + cada.data.comb

    return costo


    

clearConsole()
FileUpload()
MenuPricipal() 