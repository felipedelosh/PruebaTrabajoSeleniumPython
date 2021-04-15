"""
FelipedelosH

Esto genera datos de personas al azar apoyadas en la carpeta humanData
"""
# -⁻- coding: UTF-8 -*-
import os # Para cargar archivos desde HDD
import random # Para generar aleatoreamente los datos
import math # Para calculos complejos 
from datetime import date
import time

class Persona:
    def __init__(self):
        self.edad = ""
        self.sexo = ""
        self.tipoDeDocumento = "" # Cedula o tarjeta
        self.numeroDedocumento = 0
        self.nombre = ""
        self.apellidos = ""
        self.diaDeNacimiento = 0
        self.nroMesNaciemiento = 0 
        self.anoNacimiento = 0
        self.correoelectronico = ""
        self.telefonoCelular = ""

    def verDatosPersona(self):
        txt = self.nombre + " "  + self.apellidos + "\n"
        txt = txt + "Edad: " + str(self.edad) + " Datos Nacimiento: " + str(self.diaDeNacimiento) + "/" + str(self.nroMesNaciemiento) + "/" + str(self.anoNacimiento) + "\n"
        txt = txt + "TipoDocu: " + self.tipoDeDocumento + " N: " + str(self.numeroDedocumento) + " Genero: " + self.sexo + "\n" 
        txt = txt + " Contacto: " + self.correoelectronico + "/" + self.telefonoCelular

        print(txt)


class Controladora:
    def __init__(self):
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # Saber la ruta del disco duro del proyecto
        self.apellidos = []
        self.nombresMasculinos = []
        self.nombresFemeninos = []
        self.cargarDatosHumanos()



    def cargarDatosHumanos(self):
        try:
            ruta = self.rutaDelProyecto + "\\humanData\\"

            self.apellidos = self.cargarDatosTXT(ruta+"dbLASTNAME.txt")
            self.nombresMasculinos = self.cargarDatosTXT(ruta+"dbNAMEMALE.txt")
            self.nombresFemeninos = self.cargarDatosTXT(ruta+"dbNAMEFEMALE.txt")

        except:
            self.apellidos = ["Hernandez", "Rios", "Mejia"]
            self.nombresMasculinos = ["Juan", "Carlos", "David"]
            self.nombresFemeninos = ["Manuela", "Juanita", "Sofia"]


    def cargarDatosTXT(self, ruta):
        """
        Lee line a linea un .txt y retorna un vector str,str,...str
        """
        temp = []
        f = open(ruta, "r", encoding="UTF-8")
        for i in f.read().split("\n"):
                if i.strip() != "":
                    temp.append(i)

        return temp


    def retornarGeneroAzar(self):
        k = random.randint(0, 1)
        if k == 0:
            return "M"
        else:
            return "F"

    def retornarNumeroDocumentoAzar(self):
        nroDocumento = "105"

        for i in range(0, 7):
            nroDocumento = nroDocumento + str(random.randint(0, 9))

        return int(nroDocumento)

    def retornarTelefonoCelularAlAzar(self):
        nro = "31"

        nro = nro + str(random.randint(1,7))

        for i in range(0, 7):
            nro = nro + str(random.randint(0, 9))

        return nro

    def retornarNombreFemneninoAzar(self):
        return self.nombresFemeninos[random.randint(0, len(self.nombresFemeninos)-1)]

    def retornarNombreMasculinoAzar(self):
        return self.nombresMasculinos[random.randint(0, len(self.nombresMasculinos)-1)]

    def retornarApellidoAlAzar(self):
        return self.apellidos[random.randint(0, len(self.apellidos)-1)]


    def generarAdultoAlAzar(self):
        """
        Retorna una persona Masculina o Femenina de mas de 18 años
        """
        p = Persona()
        p.edad = random.randint(18, 70) # Determina la edad
        # Se pone un fecha de nacimiento
        d = date.today()
        p.diaDeNacimiento = random.randint(1, 25)
        if d.month > 1:
            p.nroMesNaciemiento = random.randint(1, d.month)
        else:
            p.nroMesNaciemiento = 1

        p.anoNacimiento = d.year - p.edad
        p.tipoDeDocumento = "CC"
        p.numeroDedocumento = self.retornarNumeroDocumentoAzar()

        # Se pone el nombre y 2 apellidos
        p.sexo = self.retornarGeneroAzar()
        if p.sexo == "F":
            p.nombre = self.retornarNombreFemneninoAzar()
        else:
            p.nombre = self.retornarNombreMasculinoAzar()

        p.apellidos = self.retornarApellidoAlAzar() + " " + self.retornarApellidoAlAzar()

        # Se pone el correo nombre+_+anoNacimiento+x+numeros+@+google.com
        p.correoelectronico = str(p.nombre).lower()+"_"+str(p.anoNacimiento)+"x"+str(random.randint(111,777))+"@google.com"

        # Se pone un numero de celular
        p.telefonoCelular = self.retornarTelefonoCelularAlAzar()


        return p




    def generarNinoAlAzar(self):
        pass

    def generarBebeAlAzar(self):
        """
        Retorna un bebe masculino o femenino de 0, 23 meses
        """
        p = Persona()
        # Genero los meses
        meses = random.randint(0, 23)
        # Tenermino cuantos a+os son y pongo los datos de edad
        d = date.today()
        anhos =  math.floor(meses/12)

        if anhos == 0:
            # Si la fecha actual es superior a febrero lo registro 1 mes antes 
            # Si la fecha actual es enero lo registro a finales
            if d.month > 1:
                p.edad = 0
                p.diaDeNacimiento = random.randint(1, 28)
                p.nroMesNaciemiento = d.month - 1
                p.anoNacimiento = d.year
            else:
                p.edad = 0
                p.diaDeNacimiento = random.randint(1, 28)
                p.nroMesNaciemiento = d.month(10, 12)
                p.anoNacimiento = d.year - 1
                
        else:
            p.edad = 1
            p.diaDeNacimiento = random.randint(1, 28)
            p.nroMesNaciemiento = d.month - random.randint(1, 3)
            p.anoNacimiento = d.year - 1

        p.tipoDeDocumento = "RC"
        p.numeroDedocumento = self.retornarNumeroDocumentoAzar()

        p.sexo = self.retornarGeneroAzar()


        # Se pone q nombre y 2 pellidos
        if p.sexo == "F":
            p.nombre = self.retornarNombreFemneninoAzar()
        else:
            p.nombre = self.retornarNombreMasculinoAzar()

        p.apellidos = self.retornarApellidoAlAzar() + " " + self.retornarApellidoAlAzar()


        return p