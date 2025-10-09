# EJERCICIO UNIDAD 4.
# Cree un menú en el cual la primera opción debe ser ejercutar el problema que ustedes programaron. La segunda opción debe ser salir.

def CALC_CG (MT, PMT):
                CG = MT / PMT
                return CG


def OP2 ():
                info_aeronave = {
                "MDL": "",
                "MTCL": "",
                "NSRE": ""
                }


                info_aeronave["MDL"] = input("Ingrese el modelo de la aeronave: ")
                info_aeronave["MTCL"] = input("Ingrese la matrícula de la aeronave: ")
                info_aeronave["NSRE"] = input("Ingrese el número de serie de la aeronave: ")


                datum = []


                BDMN = float(input("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren de nariz (ft): "))
                datum.append(BDMN)
                BDMP = float(input("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren principal: "))
                datum.append(BDMN)
                RPCG = float(input("Ingrese el Rango Permitido del Centro de Gravedad (en distancia desde el datum): "))
                datum.append(BDMN)
                RPCGmin = datum[2] - 1
                datum.append(RPCGmin)
                RPCGmax = datum[2] + 1
                datum.append(RPCGmax)


                while True:
                    PMTN = float(input("Ingrese el peso registrado en el Tren de nariz (lb): "))
                    PMTPI = float(input("Ingrese el peso registrado en el Tren principal (izquierda)): "))
                    PMTPD = float(input("Ingrese el peso registrado en el Tren principal (derecha): "))
                    PMTP = PMTPI + PMTPD    
                    PMT = PMTP + PMTN
                    MPN = PMTN * BDMN
                    MPP = PMTP * BDMP
                    MT = MPN + MPP
                    CG = CALC_CG (MT, PMT)
                    if datum[3] < CG < datum[4]:
                        break
                    elif CG < datum[3]:
                        print ("Añada más peso atras o reduzca adelante e introduzca los nuevos datos")
                    elif CG > datum[4]:
                        print ("Añada más peso adelante o reduzca atras e introduzca los nuevos datos")
                print (f"El avión {info_aeronave["MDL"]} con matrícula {info_aeronave["MTCL"]} y numero de serie {info_aeronave["NSRE"]}, cuenta con un CG a {CG} metros del Datum, Dato valido para permitir su salida.")


while True:
    print ("Bienvenido, este menú le permitirá realizar las siguientes tareas:")
    opcion = int(input("(1) Peso, balance y centro de gravedad de una aeronave.\n(2) Salir del programa. \nPor favor, ingrese una opción: "))
    match (opcion):
        case 1:
            OP2()
        case 2:
            print ("Saliendo del programa...")
            break
        case _:
            print ("Por favor, ingrese una opción válida.")