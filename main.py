import re
from xml.dom import minidom
import os
#import graphviz


class Nodo:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        self.up = None
        self.down = None

        self.link = None
        self.linkCost = 0

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
                        return
                    else:
                        temp = temp.next
class Area :
    def __init__(self,comb,coorx, coory):
        self.comb = comb
        self.coorx = coorx
        self.coory = coory
class Ground:
    def __init__(self,name,bX,bY,fX,fY,mX,nY):
        self.nameGround = name 
        self.raiz = Nodo(Area(None,None,None))
        self.dimX = mX
        self.dimY = nY
        self.beginX = bX
        self.beginY = bY
        self.finalX = fX
        self.finalY = fY
        self.listCamino = []
    def getName(self):
        return self.nameGround
    def setlistCamino(self, listacam):
        self.listCamino = listacam
    def getlistCamino(self):
        return self.listCamino
    def NewAreaX(self,comb,coorX,coorY):
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
        Salida()
        
    elif option == "4":
        clearConsole()
        DataStudent()
    elif option == "5":
        clearConsole()
        graficGround()
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
    mydoc = minidom.parse(dx+".xml")
    grounds = mydoc.getElementsByTagName("terreno")
    for terrenos in grounds:
        NameG = terrenos.attributes['nombre'].value
        CoorF = terrenos.getElementsByTagName("dimension")[0]
        mx = CoorF.getElementsByTagName("m")
        Mx = mx[0].firstChild.data
        ny = CoorF.getElementsByTagName("n")
        Ny = ny[0].firstChild.data
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
        ActualG = Ground(NameG,int(Bx),int(By),int(Fx),int(Fy),int(Mx),int(Ny))
        Grounds.AddFinal(ActualG)
        for Area in Areas:
            Px = Area.attributes['x'].value
            Py = Area.attributes['y'].value
            Comb = Area.firstChild.data
            ActualG.NewAreaX(int(Comb),int(Px),int(Py))
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
    print()
    MenuPricipal()
def  graficGround():
    nameg = input()
    AuxGround = Grounds.SeachGround(nameg)
    aux = AuxGround.raiz
    aux = aux.down
    strdot = "graph "+AuxGround.nameGround+" {\n"
    while aux:
        auxf = aux.next
        while auxf:
            strdot= strdot + "  x"+str(auxf.data.coorx)+"y"+str(auxf.data.coory)+' [label = "'+str(auxf.data.comb)+'"];\n'
            auxf = auxf.next
        aux = aux.down
    strdot = strdot+dotEnlace(AuxGround)
    strdot = strdot + "}"
    print(strdot)
    file = open("C:\\Users\\danie\\Desktop\\terreno.dot", "w")
    file.write(strdot)

def dotEnlace(Ground):
    aux = Ground.raiz
    aux = aux.down
    strdot=""
    while aux:
        auxf = aux.next
        while auxf:
            if auxf.next != None:
                if auxf.next.data.comb != None:
                    tempaux = auxf.next
                    strdot = strdot+"  x"+str(auxf.data.coorx)+"y"+str(auxf.data.coory)+"--x"+str(tempaux.data.coorx)+"y"+str(tempaux.data.coory)+"[constraint = false]"+"\n"
            #if auxf.prev != None:
                #if auxf.prev.data.comb != None:
                    #tempaux = auxf.prev
                    #strdot = strdot+"  a"+str(auxf.data.coorx)+str(auxf.data.coory)+"--a"+str(tempaux.data.coorx)+str(tempaux.data.coory)+"\n"
            if auxf.down != None:
                if auxf.down.data.comb != None:
                    tempaux = auxf.down
                    strdot = strdot+"  x"+str(auxf.data.coorx)+"y"+str(auxf.data.coory)+"--x"+str(tempaux.data.coorx)+"y"+str(tempaux.data.coory)+"[constraint = true]"+"\n"
            #if auxf.up != None:
                #if auxf.up.data.comb != None:
                    #tempaux = auxf.up
                    #strdot = strdot+"  a"+str(auxf.data.coorx)+str(auxf.data.coory)+"--a"+str(tempaux.data.coorx)+str(tempaux.data.coory)+"\n"
            auxf = auxf.next
        aux = aux.down
    return strdot
def processGround():
    print("Inserte el nombre de terreno que le interesa")
    nameg = input()
    AuxGround = Grounds.SeachGround(nameg)
    aux = AuxGround.raiz
    aux = aux.down
    print(AuxGround.beginX,AuxGround.beginY,AuxGround.finalX,AuxGround.finalY)
    while aux:
        if aux.data.coory == AuxGround.beginY:
            aux = aux.next
            while aux:
                if aux.data.coorx == AuxGround.beginX:
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
                                    #listCamino = camino(NodoInicio,NodoFinal)
                                    listCamino = road(NodoInicio,NodoFinal,AuxGround.dimX,AuxGround.dimY,AuxGround.raiz)
                                    AuxGround.setlistCamino(listCamino)
                                    printCamino(AuxGround,listCamino) 
                                    input()
                                    MenuPricipal()                                   
                                aux = aux.next    
                        aux = aux.down
                aux = aux.next       
        aux = aux.down
def printCamino(Ground,listCamino):
    aux = Ground.raiz
    aux = aux.down
    while aux:
        fila="|"
        auxf = aux.next
        while auxf:
            try:
                n = listCamino.index(auxf)
            except:
                n = -1
            if n !=-1:
                fila = fila + " 1 |"
            else:
                fila = fila + " 0 |"
                

            auxf = auxf.next
        print(fila)
        aux = aux.down


def road(start,end,dimX,dimY,root):
    bigger = dimX
    if dimY > dimX:
        bigger = dimY
    
    for r in range(0,5*bigger):
        yPointer = root.down.next
        for y in range(0,dimY):
            xPointer = yPointer
            for i in range(0,dimX): 
                updateLink(start,end,xPointer,xPointer.down)
                updateLink(start,end,xPointer,xPointer.up)
                updateLink(start,end,xPointer,xPointer.next)
                updateLink(start,end,xPointer,xPointer.prev)
                xPointer=xPointer.next


            yPointer = yPointer.down
    
    lstRet = []
    nextPtr = end.link 
    while nextPtr is not start:
        lstRet.append(nextPtr)
        nextPtr = nextPtr.link
    lstRet.append(start)
    lstRet.append(end)
    return lstRet

def updateLink(start,end,node,neighbor):
    if(neighbor is None or neighbor.data.comb is None):
        return 
    if(neighbor==end and end.link is not None):
        return True

    if(neighbor==start):
        node.linkCost = start.data.comb  + node.data.comb 
        node.link = neighbor
        return
    if neighbor.link is not None:
        if node.linkCost is 0:
            node.linkCost = neighbor.linkCost + node.data.comb
            node.link = neighbor
        elif node.linkCost > neighbor.linkCost + node.data.comb:
            node.linkCost = neighbor.linkCost + node.data.comb 
            node.link = neighbor



        
    


def Salida():
    print("Inserte el nombre de terreno que le interesa")
    nameg = input()
    AuxGround = Grounds.SeachGround(nameg)
    Bx = str(AuxGround.beginX)
    By = str(AuxGround.beginY)
    Fx =str(AuxGround.finalX)
    Fy =str(AuxGround.finalY)
    Mx = str(AuxGround.dimX)
    Ny = str(AuxGround.dimY)
    Cb = str(10)
    listCam = AuxGround.getlistCamino()
    strxml = '<terreno nombre="'+AuxGround.getName()+'">\n'
    strxml = strxml + '     <dimension>\n'
    strxml = strxml + '     <m>'+Mx+'</m>'+'\n'
    strxml = strxml + '     <n>'+Ny+'</n>'+'\n'
    strxml = strxml + '     </dimension>\n'
    strxml = strxml + '     <posicioninicio>\n'
    strxml = strxml + '     <x>'+Bx+'</x>'+'\n'
    strxml = strxml + '     <y>'+By+'</y>'+'\n'
    strxml = strxml + '     </posicioninicio>\n'
    strxml = strxml + '     <posicionfin>\n'
    strxml = strxml + '     <x>'+Fx+'</x>'+'\n'
    strxml = strxml + '     <y>'+Fy+'</y>'+'\n'
    strxml = strxml + '     </posicionfin>\n'
    strxml = strxml + '     <combustible>'+Cb+'</combustible>\n'
    for nod in listCam:
        strxml = strxml + '     <posicion x="'+str(nod.data.coorx)+'" y="'+str(nod.data.coory)+'">'+str(nod.data.comb)+'</posicion>\n'
    strxml = strxml + '</terreno>\n'
    print(strxml)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path+"\\"+nameg+".xml", "w")
    file.write(strxml)
    file.close()
    input()
    MenuPricipal()



    

clearConsole()
FileUpload()
MenuPricipal() 