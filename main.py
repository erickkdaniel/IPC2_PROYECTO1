from xml.dom import minidom
import graphviz
import os
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
    def travelGrounds(self):
        listGrounds = []
        aux= self.first
        while aux:
            listGrounds.append(aux)
            aux = aux.next
        return listGrounds
    def SeachGround(self, name):
        temp = self.first
        while temp:
            if self.Empty():
                print("No se han agregado terrenos")
                input()
                clearConsole()
                MenuPricipal()
            else:
                if temp.data.getName() == name:
                    return temp.data
                else:
                    if temp == self.last: 
                        print("No se encontro un terreno con el nombre: "+name)
                        input()
                        clearConsole()
                        MenuPricipal()
                    else:
                        temp = temp.next
    def SeachGroundID(self, ID):
        temp = self.first
        while temp:
            if self.Empty():
                print("No se han agregado terrenos")
                input()
                clearConsole()
                MenuPricipal()
            else:
                if str(temp.data.id) == ID:
                    return temp.data
                else:
                    if temp == self.last: 
                        print("No se encontro un terreno con el ID: "+ID)
                        input()
                        clearConsole()
                        graficGround()
                    else:
                        temp = temp.next
class Area:
    def __init__(self,comb,coorx, coory):
        self.comb = comb
        self.coorx = coorx
        self.coory = coory
class Ground:
    def __init__(self,name,bX,bY,fX,fY,mX,nY,id):
        self.nameGround = name 
        self.raiz = Nodo(Area(None,None,None))
        self.dimX = mX
        self.dimY = nY
        self.beginX = bX
        self.beginY = bY
        self.finalX = fX
        self.finalY = fY
        self.id = id
        self.listCamino = []
        self.combGastado = 0
    def setComb(self, combu):
        self.combGastado = combu
    def getName(self):
        return self.nameGround
    def setlistCamino(self, listacam):
        self.listCamino = listacam
    def getlistCamino(self):
        return self.listCamino
    def NewAreaX(self,comb,coorX,coorY):
        if self.raiz.next == None:
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
Grounds = ListGround()
def MenuPricipal1():
    print("Menu Principal")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiatne")
    print("5. Generar gráfica")
    print("6. Salida")
    option = input()
    if option == "1":
        clearConsole()
        FileUpload()
    elif option == "2":
        print("No se ha ingresado ninguna lista de terrenos.")
        input()
        clearConsole()
        MenuPricipal1()
    elif option == "3":
        print("No se ha ingresado ninguna lista de terrenos.")
        input()
        clearConsole()
        MenuPricipal1()
    elif option == "4":
        clearConsole()
        DataStudent()
        MenuPricipal1()
    elif option == "5":
        print("No se ha ingresado ninguna lista de terrenos.")
        input()
        clearConsole()
        MenuPricipal1()
    elif option == "6":
        clearConsole()
        quit()
    else:
        clearConsole()
        print("Debe de ingresar alguna opcion valida.")
        input()
        clearConsole()
        MenuPricipal()
def MenuPricipal():
    print("Menu Principal")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiatne")
    print("5. Generar gráfica")
    print("6. Salida")
    option = input()
    if option == "1":
        clearConsole()
        FileUpload()
    elif option == "2":
        clearConsole()
        processGround()
    elif option == "3":
        clearConsole()
        Salida()
    elif option == "4":
        clearConsole()
        DataStudent()
        MenuPricipal()
    elif option == "5":
        clearConsole()
        graficGround()
    elif option == "6":
        clearConsole()
        exit()
    else:
        clearConsole()
        print("Debe de ingresar alguna opcion valida.")
        input()
        clearConsole()
        MenuPricipal()
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
    return
def FileUpload():
    print("Ingresa la direccion de archivo")
    dx = input()
    try:
        FileUploadAnalysis(dx)
    except OSError as e:
        clearConsole()
        print("Archivo no encontrado vuelva a intentarlo o el archivo no cumple con los requisitos")
        input()
        clearConsole()
        FileUpload()
def FileUploadAnalysis(dx):
    id = 1
    mydoc = minidom.parse(dx+".xml")
    grounds = mydoc.getElementsByTagName("terreno")
    for terrenos in grounds:
        NameG = terrenos.attributes['nombre'].value
        CoorF = terrenos.getElementsByTagName("dimension")[0]
        my = CoorF.getElementsByTagName("m")
        My = my[0].firstChild.data
        nx = CoorF.getElementsByTagName("n")
        Nx = nx[0].firstChild.data
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
        ActualG = Ground(NameG,int(By),int(Bx),int(Fy),int(Fx),int(Nx),int(My),id)
        id=id+1
        Grounds.AddFinal(ActualG)
        for Area in Areas:
            Px = Area.attributes['x'].value
            Py = Area.attributes['y'].value
            Comb = Area.firstChild.data
            ActualG.NewAreaX(int(Comb),int(Py),int(Px))
    print("Ingresada nueva lista de terrenos")
    input()
    clearConsole()
    MenuPricipal()
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
    listCam = AuxGround.getlistCamino()
    if len(listCam) == 0:
        clearConsole()
        print("Este archivo no ha sido procesado")
        input()
        clearConsole()
        MenuPricipal()
    Cb = str(listCam[-1].linkCost)
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
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path+"\\"+nameg+".xml", "w")
    file.write(strxml)
    file.close()
    print("El archivo (.xml) del terreno "+AuxGround.getName()+" fue escrito.")
    input()
    MenuPricipal()
def graficGround():
    print("Graficador")
    lsGrounds = Grounds.travelGrounds()
    for i in lsGrounds:
        print(str(i.data.id)+'. '+i.data.nameGround)
        idl = i.data.id
    print("Ingrese el numero de terreno que le interese graficar")
    idi = input()
    if verifi(idl,idi):
        print("la opcion que ingreso no es valida")
        input()
        clearConsole()
        graficGround()
    AuxGround = Grounds.SeachGroundID(idi)
    aux = AuxGround.raiz
    aux = aux.down
    strdot = "graph "+AuxGround.nameGround+" {\n"
    strdot =strdot+'labelloc="b";\n'
    strdot =strdot+'label="'+AuxGround.nameGround+'"\n';
    strdot =strdot+'fontsize="25";\n'
    while aux:
        auxf = aux.next
        while auxf:
            strdot= strdot + "  x"+str(auxf.data.coorx)+"y"+str(auxf.data.coory)+' [label = "'+str(auxf.data.comb)+'"];\n'
            auxf = auxf.next
        aux = aux.down
    strdot = strdot+dotEnlace(AuxGround)
    strdot = strdot + "}"
    src = graphviz.Source(strdot)
    file = open("C:\\Users\\danie\\Desktop\\terreno.dot", "w")
    file.write(strdot)
    src.render('C:\\Users\\danie\\Desktop\\'+AuxGround.nameGround+'.pdf', view=True) 
    clearConsole()
    print("Gráfica del terreno "+AuxGround.nameGround+" creada")
    input()
    MenuPricipal()
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
            if auxf.down != None:
                if auxf.down.data.comb != None:
                    tempaux = auxf.down
                    strdot = strdot+"  x"+str(auxf.data.coorx)+"y"+str(auxf.data.coory)+"--x"+str(tempaux.data.coorx)+"y"+str(tempaux.data.coory)+"[constraint = true]"+"\n"
            auxf = auxf.next
        aux = aux.down
    return strdot
def processGround():
    print("Procesar Terreno:")
    print("Inserte el nombre de terreno que le interese.")
    nameg = input()
    AuxGround = Grounds.SeachGround(nameg)
    clearConsole()
    print("Encontrando la mejor ruta...")
    aux = AuxGround.raiz
    aux = aux.down
    while aux:
        if aux.data.coory == AuxGround.beginY:
            aux = aux.next
            while aux:
                if aux.data.coorx == AuxGround.beginX:
                    NodoInicio=aux
                    aux = AuxGround.raiz
                    aux = aux.down
                    while aux:
                        if aux.data.coory == AuxGround.finalY:
                            aux = aux.next
                            while aux:
                                if aux.data.coorx == AuxGround.finalX:
                                    NodoFinal=aux
                                    listCamino = road(NodoInicio,NodoFinal,AuxGround.dimX,AuxGround.dimY,AuxGround.raiz)
                                    AuxGround.setlistCamino(listCamino)
                                    input()
                                    clearConsole()
                                    print("Calculando el combustible gastado...")
                                    input()
                                    clearConsole()
                                    printCamino(AuxGround,listCamino)
                                    input()
                                    clearConsole()
                                    MenuPricipal()                                   
                                aux = aux.next    
                        aux = aux.down
                aux = aux.next       
        aux = aux.down
def printCamino(Ground,listCamino):
    aux = Ground.raiz
    aux = aux.down
    comb = listCamino[-1].linkCost
    print("Combustible gastado: "+str(comb))
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
    newList = [] 
    lstRet.append(end)
    while nextPtr is not start:
        lstRet.append(nextPtr)
        nextPtr = nextPtr.link
    lstRet.append(start)
    idx = len(lstRet) - 1
    while (idx >= 0):
        newList.append(lstRet[idx])
        idx = idx - 1
    return newList
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
def verifi(max,id):
    max = int(max)
    if id.isnumeric():
        id = int(id)
        if id <= max and id > 0:
            return False
    return True
clearConsole()
MenuPricipal1()