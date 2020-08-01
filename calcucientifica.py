import math
class CalcuCientifica():
    operacion=0
    resultado=0
    def __init__(self,operacion,resultado):
        self.operacion=operacion
        self.resultado=resultado
# menu general del programa
    def menu(self):
        print("Calculadora Cientifica")
        print("Seleccione opcion a realizar: ")
        print("1: Operaciones Basicas\n2: Funciones trigonometricas\n3: Raices,Potencias y Logaritmos\n4: Otros")
        seleccion=int(input())
        if seleccion==1:
            self.basicas()
        elif seleccion==2:
            self.trigonometricas()
        elif seleccion==3:
            self.racExpLog()
        elif seleccion==4:
            self.otros()
        else:
            print("Opcion no valida")
            self.menu()

#Seccion de operaciones basicas
    def basicas(self):
        print("Basicas")
        print("Seleccione opcion a realizar: ")
        print("1: Suma\n2: Resta\n3: Multiplicacion\n4: Division")
        selBas=int(input())
        if selBas==1:
            self.suma()
        elif selBas==2:
            self.resta()
        elif selBas==3:
            self.multipli()
        elif selBas==4:
            self.division()
        else:
            print("Opcion no valida")
            self.basicas()

    def suma(self):
        print("Ingrese el primer numero")
        num1=int(input())
        print("Ingrese el segundo numero")
        num2=int(input())
        resultado=num1+num2
        print(num1,'+',num2,'=',resultado)
    def resta(self):
        print("Ingrese el minuendo")
        num1=int(input())
        print("Ingrese el sustraendo")
        num2=int(input())
        resultado=num1-num2
        print(num1,'-',num2,'=',resultado)
    def multipli(self):
        print("Ingrese el primer numero")
        num1=int(input())
        print("Ingrese el segundo numero")
        num2=int(input())
        resultado=num1*num2
        print(num1,'*',num2,'=',resultado)
    def division(self):
        print("Ingrese el dividendo")
        num1=int(input())
        print("Ingrese el divisor")
        num2=int(input())
        resultado=num1/num2
        print(num1,'/',num2,'=',resultado)

#seccion funciones trigonometricas

    def trigonometricas(self):
        print("Trigonometricas")
        print("Seleccione tipo de funcion trigonometrica: ")
        print("1: SENO\n2: COSENO\n3: TANGENTE\n4: ARCOSENO\n5: ARCOCOSENO\n6: ARCOTANGENTE")
        seltri=int(input())
        if seltri==1:
            self.seno()
        elif seltri==2:
            self.coseno()

        elif seltri==3:
            self.tangente()

        elif seltri==4:
            self.arcoseno()

        elif seltri==5:
            self.arcocoseno()

        elif seltri==6:
            self.arcotangente()

        else:
            print("Opcion no valida")
            self.trigonometricas()

    def seno(self):
        print("Seno(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.sin(angulo)
        print("El seno de ",angulo," es: ",resultado)
    def coseno(self):
        print("Coseno(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.cos(angulo)
        print("El coseno de ",angulo," es: ",resultado)
    def tangente(self):
        print("Tangente(x)")
        print("Ingrese el valor del angulo x en radianes")
        angulo=float(input())
        resultado=math.tan(angulo)
        print("La tangente de ",angulo," es: ",resultado)
    def arcoseno(self):
        print("ArcoSeno(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.asin(angulo)
        print("El arcoseno de ",angulo," es el angulo: ",resultado," rad")
    def arcocoseno(self):
        print("ArcoCoseno(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.acos(angulo)
        print("El arcocoseno de ",angulo," es el angulo: ",resultado," rad")
    def arcotangente(self):
        print("ArcoTangente(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.atan(angulo)
        print("La arcotangente de ",angulo," es el angulo: ",resultado," rad")


#seccion raices exponentes y logaritmos
    def racExpLog(self):
        print("Raices,Potencias y Logaritmos")
        print("Seleccione tipo de operacion: ")
        print("1: Raiz\n2: Potencia\n3: Logaritmo")
        selRacExpLog=int(input())
        if selRacExpLog==1:
            self.raices()
        elif selRacExpLog==2:
            self.potencia()
        elif selRacExpLog==3:
            self.logaritmos()
        else:
            print("Opcion no valida")
            self.racExpLog()

    def raices(self):
        print("Raices")
        print("Ingrese el indice")
        indice=int(input())
        print("Ingrese el radicando")
        radicando=float(input())
        resultado=radicando**(1/indice)
        print("La respuesta de esa raiz es: ",resultado)
    def potencia(self):
        print("Potencias")
        print("Ingrese la base")
        base=float(input())
        print("Ingrese el exponente")
        exponente=int(input())
        resultado=base**exponente
        print("La respuesta de la potencia es: ",resultado)
    def logaritmos(self):
        print("Logaritmos")
        print("Seleccione el tipo de Logaritmo")
        print("1: Logaritmo Decimal\n2: Logaritmo Natural")
        selecLog=int(input())
        if selecLog==1:
            self.logB()
        elif selecLog==2:
            self.logNat()
        else:
            print("Opcion no valida")
            self.logaritmos()
    def logB(self):
        print("Logaritmos decimales")
        print("Ingrese la base:")
        base=int(input())
        print("Ingrese el argumento:")
        argumento=float(input())
        resultado=math.log(argumento,base)
        print("El logaritmo base ",base," de ",argumento," es: ",resultado)

    def logNat(self):
        print("Logaritmos naturales")
        print("Ingrese el argumento")
        argumento=float(input())
        resultado=math.log(argumento,math.e)
        print("El logaritmo natural de",argumento," es: ",resultado)


#seccion de operaciones
    def otros(self):
        print("Otras operaciones")
        print("Seleccione la opcion a realizar")
        print("1:Factorial de un numero\n2:Valor Absoluto de un numero\n3:Funciones Hiperbolicas")
        selecOtros=int(input())
        if selecOtros==1:
            self.factorial()
        elif selecOtros==2:
            self.vabsoluto()
        elif selecOtros==3:
            self.hiperbolicas()
        else:
            print("Opcion no valida")
            self.otros()

    def factorial(self):
        print("Factorial")
        print("Ingrese el numero")
        numerof=int(input())
        resultado=math.factorial(numerof)
        print("El factorial de ",numerof," es ",resultado)

    def vabsoluto(self):
        print("Valor Absoluto")
        print("Ingrese el numero")
        numero=float(input())
        resultado=math.fabs(numero)
        print("El valor absoluto de ",numero," es ",resultado)

    def hiperbolicas(self):
        print("Funciones hiperbolicas")
        print("Seleccione tipo de funcion hiperbolica: ")
        print("1: SENO HIPERBOLICO\n2: COSENO HIPERBOLICO\n3: TANGENTE HIPERBOLICA")
        print("4: ARCOSENO HIPERBOLICO \n5: ARCOCOSENO HIPERBOLICO\n6: ARCOTANGENTE HIPERBOLICA")
        selecHiper=int(input())
        if selecHiper==1:
            self.senoh()
        elif selecHiper==2:
            self.cosenoh()

        elif selecHiper==3:
            self.tangenteh()

        elif selecHiper==4:
            self.arcosenoh()

        elif selecHiper==5:
            self.arcocosenoh()

        elif selecHiper==6:
            self.arcotangenteh()

        else:
            print("Opcion no valida")
            self.hiperbolicas()

    def senoh(self):
        print("Senh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.sinh(angulo)
        print("El seno hiperbolico de ",angulo," es: ",resultado)
    def cosenoh(self):
        print("Cosh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.cosh(angulo)
        print("El coseno hiperbolico de ",angulo," es: ",resultado)
    def tangenteh(self):
        print("Tanh(x)")
        print("Ingrese el valor de x")
        angulo=float(input())
        resultado=math.tanh(angulo)
        print("La tangente hiperbolica de ",angulo," es: ",resultado)
    def arcosenoh(self):
        print("ArcSenh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.asinh(angulo)
        print("El arcoseno hiperbolico de ",angulo," es: ",resultado)
    def arcocosenoh(self):
        print("ArcCosh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.acosh(angulo)
        print("El arcocoseno hiperbolico de ",angulo," es: ",resultado)
    def arcotangenteh(self):
        print("ArcTanh(x)")
        print("Ingrese el valor de x ")
        angulo=float(input())
        resultado=math.atanh(angulo)
        print("La arcotangente hiperbolica de ",angulo," es: ",resultado)



calculo=CalcuCientifica(0,0)
selecOperacion=calculo.menu()
