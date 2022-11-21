from os import sep
import os
LimpiarPantalla = lambda: os.system('cls')

#region Metodos
def separador():
    print("="*60)

def productosABC():
    global Total_Anual
    LimpiarPantalla()
    # Producto A

    print("\t\tProducto A")
    print("PRIMER SEMESTRE")
    cant_A = int(input("No. de Unidades: "))
    precio_A = int(input("Precio: "))
    Importe_A = (cant_A * precio_A)
    print(f"El importe de Prodcuto A en el primer semestre es: {Importe_A}")
    print("\n")

    print("SEGUNDO SEMESTRE")
    cant_A2 = int(input("No. de Unidades: "))
    precio_A2 = int(input("Precio: "))
    Importe_A2 = (cant_A2 * precio_A2)
    print(f"El importe de Prodcuto A en el segundo semestre es: {Importe_A2}")
    print("\n")

    print("TOTAL Producto A: ")
    Total_A = (Importe_A + Importe_A2)
    print(Total_A)
    separador()

    #Producto B
    print("\t\tProducto B")
    print("PRIMER SEMESTRE")
    cant_B = int(input("No. de Unidades: "))
    precio_B = int(input("Precio: "))
    Importe_B = (cant_B * precio_B)
    print(f"El importe de Prodcuto B en el primer semestre es: {Importe_B}")
    print("\n")

    print("\t\tProducto B")
    print("SEGUNDO SEMESTRE")
    cant_B = int(input("No. de Unidades: "))
    precio_B = int(input("Precio: "))
    Importe_B2 = (cant_B * precio_B)
    print(f"El importe de Prodcuto B en el segundo semestre es: {Importe_B2}")
    print("\n")

    print("TOTAL Producto B: ")
    Total_B = (Importe_B + Importe_B2)
    print(Total_B)
    separador()

    # Producto C
    print("\t\tProducto C")
    print("PRIMER SEMESTRE")
    cant_C = int(input("No. de Unidades: "))
    precio_C = int(input("Precio: "))
    Importe_C = (cant_C * precio_C)
    print(f"El importe de Prodcuto C en el primer semestre es: {Importe_C}")
    print("\n")

    print("\t\tProducto C")
    print("SEGUNDO SEMESTRE")
    cant_C = int(input("No. de Unidades: "))
    precio_C = int(input("Precio: "))
    Importe_C2 = (cant_C * precio_C)
    print(f"El importe de Prodcuto C en el segundo semestre es: {Importe_C2}")
    print("\n")

    print("El total del Producto C es de: ")
    Total_C= (Importe_C + Importe_C2)
    print(Total_C)
    separador()

    print("VENTAS POR SEMESTRE")
    Total_Semestre = (Importe_A + Importe_B + Importe_C)
    Total_Semestre_2 = (Importe_A2 + Importe_B2 + Importe_C2)
    Total_Anual = (Total_A + Total_B + Total_C)
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL ANUAL'])
    t.add_row([Total_Semestre,Total_Semestre_2,Total_Anual])
    print(t)
    input("Pulse Enter para continuar...")
    separador()

def SaldoFlujo():
    LimpiarPantalla()

    # Saldo Clientes
    print(f"\tSALDO CLIENTES")
    separador()
    print("Saldo Clientes: ")
    saldo_cliente= int(input())
    print(f"Ventas: {Total_Anual}")
    total_clientes= (saldo_cliente + Total_Anual)
    print(f"Saldo Clientes Total: {total_clientes}")

    # Entradas
    print("\tENTRADAS")
    primer_año= int(input("Cobro Primer Año: "))
    segundo_año= int(input("Cobro Segundo Año: "))
    entradas_total= (primer_año + segundo_año)
    print(f"Total de Entradas: {entradas_total} ")
    total_clientes2= (total_clientes - entradas_total)
    print(f"Saldo Clientes: {total_clientes2}")
    separador()
    input("Pulse Enter para continuar...")

def PresupuestoProduccion():
    LimpiarPantalla()
    print("\tPRESUPUESTO DE PRODUCCION")
    separador()

    # Produccion A PRIMER SEMESTRE
    print(f"\t\tPresupuesto de Produccion PRODUCTO A Primer Semestre")
    no_unidades_A = int(input("No. de Unidades: "))
    inventario_finalA = int(input("Inventario Final: "))
    total_unidades = (no_unidades_A + inventario_finalA)
    print(f"Total de unidades es de: {total_unidades}")
    inventario_inicialA = int(input("Inventario  incial: "))
    unidades_producir = (total_unidades - inventario_inicialA)
    print(f"Las unidades a producir en primer semestre son: {unidades_producir}")
    
    # Produccion A SEGUNDO SEMESTRE
    print(f"\t\tPresupuesto de Produccion PRODUCTO A Segundo Semestre")
    no_unidades_A2 = int(input("No. de Unidades: "))
    inventario_finalA2 = int(input("Inventario Final: "))
    print("Total de unidades es de: ")
    total_unidades2 = (no_unidades_A2 + inventario_finalA2)
    print(f"Total de unidades es de: {total_unidades2}")
    inventario_inicialA2 = int(input("Inventario  incial: "))
    unidades_producirA2 = (total_unidades2 - inventario_inicialA2)
    print(f"Las unidades a producir en segundo semestre son: {unidades_producirA2}")

    # Produccion Total A
    print(f"\t\tProduccion Total PRODUCTO A")
    no_unidades_AT = (no_unidades_A + no_unidades_A2)
    print(f"Unidades a Vender: {no_unidades_AT}")
    print(f"Inventario Final: {inventario_finalA2}")
    Total_UnidadesA= (no_unidades_AT + inventario_finalA2)
    print(f"Total de unidades de: {Total_UnidadesA}")
    inventario_inicialA = inventario_finalA
    TotalT= (Total_UnidadesA - inventario_inicialA)
    print(f"Unidades Totales de PRODUCTO A: {TotalT}")
    separador()

    # Producto B PRIMER SEMESTRE
    print(f"\t\tPresupuesto de Produccion PRODUCTO B Primer Semestre")
    no_unidades_B = int(input("No. de Unidades: "))
    inventario_finalB = int(input("Inventario Final: "))
    total_unidades = (no_unidades_B + inventario_finalB)
    print(f"Total de unidades es de: {total_unidades}")
    inventario_inicialB = int(input("Inventario  incial: "))
    unidades_producir = (total_unidades - inventario_inicialB)
    print(f"Las unidades a producir en primer semestre son: {unidades_producir}")
    
    # Produccion B SEGUNDO SEMESTRE
    print(f"\t\tPresupuesto de Produccion PRODUCTO B Segundo Semestre")
    no_unidades_B2 = int(input("No. de Unidades: "))
    inventario_finalB2 = int(input("Inventario Final: "))
    print("Total de unidades es de: ")
    total_unidades2 = (no_unidades_B2 + inventario_finalB2)
    print(f"Total de unidades es de: {total_unidades2}")
    inventario_inicialB2 = int(input("Inventario  incial: "))
    unidades_producirB2 = (total_unidades2 - inventario_inicialB2)
    print(f"Las unidades a producir en segundo semestre son: {unidades_producirB2}")

    # Produccion Total B
    print(f"\t\tProduccion Total PRODUCTO B")
    no_unidades_BT = (no_unidades_B + no_unidades_B2)
    print(f"Unidades a Vender: {no_unidades_BT}")
    print(f"Inventario Final: {inventario_finalB2}")
    Total_UnidadesB= (no_unidades_BT + inventario_finalB2)
    print(f"Total de unidades de: {Total_UnidadesB}")
    inventario_inicialB = inventario_finalB
    TotalBT= (Total_UnidadesB - inventario_inicialB)
    print(f"Unidades Totales de PRODUCTO B: {TotalBT}")
    separador()

    # Producto C PRIMER SEMESTRE
    print(f"\t\tPresupuesto de Produccion PRODUCTO C Primer Semestre")
    no_unidades_C = int(input("No. de Unidades: "))
    inventario_finalC = int(input("Inventario Final: "))
    total_unidades = (no_unidades_C + inventario_finalC)
    print(f"Total de unidades es de: {total_unidades}")
    inventario_inicialC = int(input("Inventario  incial: "))
    unidades_producir = (total_unidades - inventario_inicialC)
    print(f"Las unidades a producir en primer semestre son: {unidades_producir}")
    
    # Produccion C SEGUNDO SEMESTRE
    print(f"\t\tPresupuesto de Produccion PRODUCTO C Segundo Semestre")
    no_unidades_C2 = int(input("No. de Unidades: "))
    inventario_finalC2 = int(input("Inventario Final: "))
    print("Total de unidades es de: ")
    total_unidades2 = (no_unidades_C2 + inventario_finalC2)
    print(f"Total de unidades es de: {total_unidades2}")
    inventario_inicialC2 = int(input("Inventario  incial: "))
    unidades_producirC2 = (total_unidades2 - inventario_inicialC2)
    print(f"Las unidades a producir en segundo semestre son: {unidades_producirC2}")

    # Produccion Total C
    no_unidades_CT = (no_unidades_C + no_unidades_C2)
    print(f"Unidades a Vender: {no_unidades_CT}")
    print(f"Inventario Final: {inventario_finalC2}")
    Total_UnidadesC= (no_unidades_CT + inventario_finalC2)
    print(f"Total de unidades de: {Total_UnidadesC}")
    inventario_inicialC = inventario_finalC
    TotalCT= (Total_UnidadesC - inventario_inicialC)
    print(f"Unidades Totales de PRODUCTO C: {TotalCT}")
    separador()
    input("Presione Enter para continuar...")

def PresupuestoReqMateriales():
    LimpiarPantalla()
    print("\tPRESUPUESTO REQUERIMENTOS PARA MATERIALES")

    # Producto A
    print(f"\tPRODUCTO A")
    no_unidades_A = int(input("No. de Unidades PRIMER SEMESTRE: "))
    no_unidades_A2 = int(input("No. de Unidades SEGUNDO SEMESTRE: "))

    print("--Requerimentos de los Materiales A, B y C--")
    req_A = float(input("Requermientos Primer Material A: "))
    req_A2 = float(input("Requermientos Segundo Material A: "))

    req_B = float(input("Requerimentos Primer Material B: "))
    req_B2 = float(input("Requerimentos Segundo Material B: "))

    req_C = float(input("Requerimentos Primer Material C: "))
    req_C2 = float(input("Requerimentos Segundo Material C: "))

    total_A1 = (no_unidades_A * req_A)
    total_A2 = (no_unidades_A2 * req_A2)
    total_AT = (total_A1 + total_A2)
    total_B1 = (no_unidades_A * req_B)
    total_B2 = (no_unidades_A2 * req_B2)
    total_BT = (total_B1 + total_B2)
    total_C1 = (no_unidades_A * req_C)
    total_C2 = (no_unidades_A2 * req_C2)
    total_CT = (total_C1 + total_C2)

    print("TOTAL MATERIAL A REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_A1,total_A2,total_AT])
    print(t)

    print("TOTAL MATERIAL B REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_B1,total_B2,total_BT])
    print(t)

    print("TOTAL MATERIAL C REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_C1,total_C2,total_CT])
    print(t)
    separador()
    input("Presione Enter para continuar...")

    # Producto B
    LimpiarPantalla()
    print(f"\tPRODUCTO B")
    no_unidades_A = float(input("No. de Unidades PRIMER SEMESTRE: "))
    no_unidades_A2 = float(input("No. de Unidades SEGUNDO SEMESTRE: "))

    print("--Requerimentos de los Materiales A, B y C--")
    req_A = float(input("Requermientos Primer Material A"))
    req_A2 = float(input("Requermientos Segundo Material A"))

    req_B = float(input("Requerimentos Primer Material B"))
    req_B2 = float(input("Requerimentos Segundo Material B"))

    req_C = float(input("Requerimentos Primer Material C"))
    req_C2 = float(input("Requerimentos Segundo Material C"))

    total_A1 = (no_unidades_A * req_A)
    total_A2 = (no_unidades_A2 * req_A2)
    total_AT = (total_A1 + total_A2)
    total_B1 = (no_unidades_A * req_B)
    total_B2 = (no_unidades_A2 * req_B2)
    total_BT = (total_B1 + total_B2)
    total_C1 = (no_unidades_A * req_C)
    total_C2 = (no_unidades_A2 * req_C2)
    total_CT = (total_C1 + total_C2)

    print("TOTAL MATERIAL A REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_A1,total_A2,total_AT])
    print(t)

    print("TOTAL MATERIAL B REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_B1,total_B2,total_BT])
    print(t)

    print("TOTAL MATERIAL C REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_C1,total_C2,total_CT])
    print(t)
    separador()
    input("Presione Enter para continuar...")

    # Producto C
    LimpiarPantalla()
    print(f"\tPRODUCTO C")
    no_unidades_A = float(input("No. de Unidades PRIMER SEMESTRE: "))
    no_unidades_A2 = float(input("No. de Unidades SEGUNDO SEMESTRE: "))

    print("--Requerimentos de los Materiales A, B y C--")
    req_A = float(input("Requermientos Primer Material A"))
    req_A2 = float(input("Requermientos Segundo Material A"))

    req_B = float(input("Requerimentos Primer Material B"))
    req_B2 = float(input("Requerimentos Segundo Material B"))

    req_C = float(input("Requerimentos Primer Material C"))
    req_C2 = float(input("Requerimentos Segundo Material C"))

    total_A1 = (no_unidades_A * req_A)
    total_A2 = (no_unidades_A2 * req_A2)
    total_AT = (total_A1 + total_A2)
    total_B1 = (no_unidades_A * req_B)
    total_B2 = (no_unidades_A2 * req_B2)
    total_BT = (total_B1 + total_B2)
    total_C1 = (no_unidades_A * req_C)
    total_C2 = (no_unidades_A2 * req_C2)
    total_CT = (total_C1 + total_C2)

    print("TOTAL MATERIAL A REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_A1,total_A2,total_AT])
    print(t)

    print("TOTAL MATERIAL B REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_B1,total_B2,total_BT])
    print(t)

    print("TOTAL MATERIAL C REQUERIDO")
    t = (['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_C1,total_C2,total_CT])
    print(t)
    separador()
    input("Presione Enter para continuar...")

def PresupuestoCompraMateriales():

    LimpiarPantalla()
    print(f"\tPRESUPUESTO COMPRA MATERIALES")

    # Material A PRIMER SEMESTRE
    print("MATERIAL A")
    separador()
    print("Primer Semestre")
    req_A = int(input("Requerimento de materiales: "))
    inv_finalA = int(input("Inventario final: "))
    total_materialesA = (req_A + inv_finalA)
    print(f"Materiales: {total_materialesA} ")
    inventario_inicialA = int(input("Inventario incial: "))
    total_materialesA_t = (total_materialesA - inventario_inicialA)
    print(f"Material a comprar: {total_materialesA_t}")
    precio_compra = int(input("Precio de compra: "))
    TotalMatA = (total_materialesA_t * precio_compra)
    print(f"Total Material A: {TotalMatA}")
    separador()

    # Material A SEGUNDO SEMESTRE
    print("Segundo Semestre")
    req_A2 = int(input("Requerimento de materiales: "))
    inv_finalA2 = int(input("Inventario final: "))
    total_materialesA = (req_A + inv_finalA)
    print(f"Total de Materiales: {total_materialesA} ")
    inventario_inicialA2 = int(input("Inventario incial: "))
    total_materialesA_t2 = (total_materialesA - inventario_inicialA2)
    print(f"Total de material a comprar: {total_materialesA_t2}")
    precio_compra = int(input("Precio de compra: "))
    TotalMatA2 = (total_materialesA_t * precio_compra)
    print(f"Total Material A Segundo Semestre: {TotalMatA2}")

    # Material A TOTAL
    LimpiarPantalla()
    print("\nTOTAL MATERIAL A")
    separador()
    print(f"Requerimentos de Materiales: {req_A + req_A2}")
    print(f"Inventario Final: {inv_finalA + inv_finalA2}")
    print(f"Materiales: {total_materialesA + total_materialesA_t2}")
    print(f"Inventario Inicial: {inventario_inicialA + inventario_inicialA2}")
    print(f"Materiales a comprar: {total_materialesA_t + total_materialesA_t2}")
    print(f"Material: ${TotalMatA + TotalMatA2} ")
    separador()
    input("Presione Enter para continuar...")

    # Material B PRIMER SEMESTRE
    print("MATERIAL B")
    separador()
    print("Primer Semestre")
    req_A = int(input("Requerimento de materiales: "))
    inv_finalA = int(input("Inventario final: "))
    total_materialesA = (req_A + inv_finalA)
    print(f"Materiales: {total_materialesA} ")
    inventario_inicialA = int(input("Inventario incial: "))
    total_materialesA_t = (total_materialesA - inventario_inicialA)
    print(f"Material a comprar: {total_materialesA_t}")
    precio_compra = int(input("Precio de compra: "))
    TotalMatA = (total_materialesA_t * precio_compra)
    print(f"Total Material B: {TotalMatA}")
    separador()

    # Material B SEGUNDO SEMESTRE
    print("Segundo Semestre")
    req_A2 = int(input("Requerimento de materiales: "))
    inv_finalA2 = int(input("Inventario final: "))
    total_materialesA = (req_A + inv_finalA)
    print(f"Total de Materiales: {total_materialesA} ")
    inventario_inicialA2 = int(input("Inventario incial: "))
    total_materialesA_t2 = (total_materialesA - inventario_inicialA2)
    print(f"Total de material a comprar: {total_materialesA_t2}")
    precio_compra = int(input("Precio de compra: "))
    TotalMatA2 = (total_materialesA_t * precio_compra)
    print(f"Total Material B Segundo Semestre: {TotalMatA2}")

    # Material B TOTAL
    LimpiarPantalla()
    print("\nTOTAL MATERIAL B")
    separador()
    print(f"Requerimentos de Materiales: {req_A + req_A2}")
    print(f"Inventario Final: {inv_finalA + inv_finalA2}")
    print(f"Materiales: {total_materialesA + total_materialesA_t2}")
    print(f"Inventario Inicial: {inventario_inicialA + inventario_inicialA2}")
    print(f"Materiales a comprar: {total_materialesA_t + total_materialesA_t2}")
    print(f"Material: ${TotalMatA + TotalMatA2} ")
    separador()
    input("Presione Enter para continuar...")

    # Material C PRIMER SEMESTRE
    print("MATERIAL C")
    separador()
    print("Primer Semestre")
    req_A = int(input("Requerimento de materiales: "))
    inv_finalA = int(input("Inventario final: "))
    total_materialesA = (req_A + inv_finalA)
    print(f"Materiales: {total_materialesA} ")
    inventario_inicialA = int(input("Inventario incial: "))
    total_materialesA_t = (total_materialesA - inventario_inicialA)
    print(f"Material a comprar: {total_materialesA_t}")
    precio_compra = int(input("Precio de compra: "))
    TotalMatA = (total_materialesA_t * precio_compra)
    print(f"Total Material C: {TotalMatA}")
    separador()

    # Material C SEGUNDO SEMESTRE
    print("Segundo Semestre")
    req_A2 = int(input("Requerimento de materiales: "))
    inv_finalA2 = int(input("Inventario final: "))
    total_materialesA = (req_A + inv_finalA)
    print(f"Total de Materiales: {total_materialesA} ")
    inventario_inicialA2 = int(input("Inventario incial: "))
    total_materialesA_t2 = (total_materialesA - inventario_inicialA2)
    print(f"Total de material a comprar: {total_materialesA_t2}")
    precio_compra = int(input("Precio de compra: "))
    TotalMatA2 = (total_materialesA_t * precio_compra)
    print(f"Total Material C Segundo Semestre: {TotalMatA2}")

    # Material A TOTAL
    LimpiarPantalla()
    print("\nTOTAL MATERIAL C")
    separador()
    print(f"Requerimentos de Materiales: {req_A + req_A2}")
    print(f"Inventario Final: {inv_finalA + inv_finalA2}")
    print(f"Materiales: {total_materialesA + total_materialesA_t2}")
    print(f"Inventario Inicial: {inventario_inicialA + inventario_inicialA2}")
    print(f"Materiales a comprar: {total_materialesA_t + total_materialesA_t2}")
    print(f"Material: ${TotalMatA + TotalMatA2} ")
    separador()
    input("Presione Enter para continuar...")

def SaldoProvFlujo():
    LimpiarPantalla()
    print("\tSALDOS PROVEEDORES Y FLUJOS DE SALIDA")
    separador()
    saldo_c = int(input("Saldo Clientes: "))
    total_clientes = (saldo_c + Total_Anual)
    print(f"Saldo Total Clientes: {total_clientes}")
    print("Entradas Efectivo")
    Año_1 = int(input("Cobranza Año 1: "))
    Año_2 = int(input("Cobranza Año 2: "))
    total_entradas = (Año_1 + Año_2)
    print(f"Total Entradas: {total_entradas}")
    Total_Clientes2 = (total_clientes - total_entradas)
    print(f"Saldo Clientes: {Total_Clientes2}")
    separador()
    input("Presione Enter para continuar...")

def manoObraDirecta():
    LimpiarPantalla()
    global total_horas_reqSum
    print("\tPRESUPUESTO PARA MANO DE OBRA DIRECTA")

    # Producto A PRIMER SEMESTRE
    separador()
    print("PRODUCTO A PRIMER SEMESTRE")
    unidades_p1= int(input("Unidades a producir: "))
    horas_por_unidad= int(input("Horas requeridas por unidad: "))
    total_horas_req1 = (unidades_p1 * horas_por_unidad)
    print(f"Total de horas requeridas: {total_horas_req1}")
    cuota_por_hora= int(input("Cuota por hora: "))
    importe_mano_obra_directa = total_horas_req1 * cuota_por_hora
    print(f"El importe de M.O.D es: {importe_mano_obra_directa}")

    # Producto A SEGUNDO SEMESTRE
    print("PRODUCTO A SEGUNDO SEMESTRE")
    unidades_p2 = int(input("Unidades a producir: "))
    horas_por_unidad2 = int(input("Horas requeridas por unidad: "))
    total_horas_req2 = (unidades_p2 * horas_por_unidad2)
    print(F"Total de horas requeridas: {total_horas_req2}")
    cuota_por_hora2 = int(input("Cuota por hora: "))
    importe_mano_obra_directa2 = total_horas_req2 * cuota_por_hora2
    print("El importe de M.O.D es: ", importe_mano_obra_directa2)

    # Producto A TOTAL
    unidades_totales = (unidades_p1 + unidades_p2)
    print(f"Total de unidades a producir: {unidades_totales}")
    Total_horas_unidad = (horas_por_unidad + horas_por_unidad2)
    print(f"Total de horas requeridas por unidad: {Total_horas_unidad}")
    Total_horas_req = (unidades_totales * Total_horas_unidad)
    print(f"Total de horas requeridas: {Total_horas_req}")
    Total_importemano_obra_directa = (importe_mano_obra_directa + importe_mano_obra_directa2)
    print(f"Total del importe de M.O.D: {Total_importemano_obra_directa}")
    separador()
    input("Pulse Enter para continuar...")

    
    # Producto B PRIMER SEMESTRE
    LimpiarPantalla()
    separador()
    print("PRODUCTO B PRIMER SEMESTRE")
    unidades_p1B = int(input("Unidades a producir: "))
    horas_por_unidadB1 = int(input("Horas requeridas por unidad: "))
    total_horas_reqB1 = (unidades_p1B * horas_por_unidadB1)
    print(f"Total de horas requeridas: {total_horas_reqB1}")
    cuota_por_horaB1= int(input("Cuota por hora: "))
    importe_mano_obra_directaB1= total_horas_reqB1 * cuota_por_horaB1
    print(f"El importe de M.O.D es: {importe_mano_obra_directaB1}")

    # Producto B SEGUNDO SEMESTRE
    print("PRODUCTO B SEGUNDO SEMESTRE")
    unidades_p1B2 = int(input("Unidades a producir: "))
    horas_por_unidadB2 = int(input("Horas requeridas por unidad: "))
    total_horas_reqB2 = (unidades_p1B2 * horas_por_unidadB2)
    print(f"Total de horas requeridas: {horas_por_unidadB1 + total_horas_reqB2}")
    cuota_por_horaB2 = int(input("Cuota por hora: "))
    importe_mano_obra_directaB2 = total_horas_reqB2 * cuota_por_horaB2
    print(f"El importe de M.O.D es: {importe_mano_obra_directaB2}")

    # Producto B TOTAL
    unidades_totalesB = (unidades_p1B + unidades_p1B2)
    print(f"El total de unidades a producir es de: {unidades_totalesB}")
    uniTotal_horas_unidadB = (horas_por_unidadB1)
    print(f"El total de horas requeridas por unidad es de: {uniTotal_horas_unidadB}")
    Total_horas_reqB = (unidades_totalesB * uniTotal_horas_unidadB)
    print("El total de horas requeridas es de: ", Total_horas_reqB)
    Total_importemano_obra_directaB = (importe_mano_obra_directaB1 + importe_mano_obra_directaB2)
    print("El total del importe de M.O.D es de: ", Total_importemano_obra_directaB)
    separador()
    input("Pulse Enter para continuar...")


    LimpiarPantalla()
    separador()
    print("\tTOTAL PRESUPUESTO")
    print(f"Unidades a producir: {unidades_totales + unidades_totalesB} ")
    print(f"Horas Requeridas por Unidad: {Total_horas_req + Total_horas_reqB}")
    total_horas_reqSum = Total_horas_req + total_horas_reqB1
    print(f"Horas Requeridas: {Total_horas_req + total_horas_reqB1}")
    print(f"Importe M.O.D: {Total_importemano_obra_directa + Total_importemano_obra_directaB}")

    print("\tHORAS REQUERIDAS")
    print(f"Primer semestre: {total_horas_req1 + total_horas_reqB1}")
    print(f"Segundo semestre: {total_horas_req2 + total_horas_reqB2}")
    print(f"Total Anual: {Total_horas_req + Total_horas_reqB}")

    print("\tTOTAL M.O.D")
    print(f"El total de M.O.D por el primer semestre es de: {importe_mano_obra_directa + importe_mano_obra_directaB1}")
    print(f"El total de M.O.D por el segundo semestre es de: {importe_mano_obra_directa2 + importe_mano_obra_directaB2} ")
    print(f"El total de M.O.D por semestre es de: {Total_importemano_obra_directa + Total_importemano_obra_directaB}")
    separador()
    input("Presione Enter para continuar...")

def gastosIndirectosFabricacion():
    LimpiarPantalla()
    global total_GIF
    print("\tGASTOS INDIRECTOS DE FABRICACION")
    separador()
    print("PRIMER SEMESTRE")
    seguros_s1 = int(input("Seguros: "))
    depreciacion_s1 = int(input("Depreciacion: "))
    energeticos_s1 = int(input("Energeticos: "))
    mantenimiento_s1 = int(input("Mantenimiento: "))
    varios_s1 = int(input("Varios: "))
    totalGIF_s1 = (depreciacion_s1 + seguros_s1 + mantenimiento_s1 + energeticos_s1 + varios_s1)
    print(f"G.I.F Total Primer Semestre: {totalGIF_s1}")

    print("SEGUNDO SEMESTRE")
    seguros_s2= int(input("Seguros: "))
    depreciacion_s2= int(input("Depreciacion: "))
    energeticos_s2= int(input("Energeticos: "))
    mantenimiento_s2= int(input("Mantenimiento: "))
    varios_s2= int(input("Varios: "))
    totalGIF_s2= (depreciacion_s2 + seguros_s2 + mantenimiento_s2 + energeticos_s2 + varios_s2)
    print(f"G.I.F Total Primer Semestre: {totalGIF_s2}")

    LimpiarPantalla()
    total_depreciacion = (depreciacion_s1 + depreciacion_s2)
    print(f"Total Depreciacion: {total_depreciacion}")

    total_seguros = (seguros_s1 + seguros_s2)
    print(f"Total Seguros: {total_seguros}")

    total_mantenimiento = (mantenimiento_s1 + mantenimiento_s2)
    print(f"Total Mantenimiento: {total_mantenimiento}")

    total_energeticos = (energeticos_s1 + energeticos_s2)
    print(f"Total Energeticos: {total_energeticos}")

    total_varios = (varios_s1 + varios_s2)
    print(f"Total Varios: {total_varios}")

    total_GIF = (total_depreciacion + total_seguros + total_mantenimiento + total_energeticos + total_varios)
    print(f"Total G.I.F: {total_GIF}")
    input("Presione Enter para continuar...")

    LimpiarPantalla()
    print("\tCOSTO POR HORA GASTOS INDIRECTOS")
    print(f"Total de G.I.F: {total_GIF}")
    print(f"El total de horas M.O.D anual es de: {total_horas_reqSum}")
    total_GIF = (total_GIF / total_horas_reqSum)
    print(f"El costo por hora de G.I.F es de: {total_GIF}")
    separador()
    input("Presione Enter para continuar...")

def PresupuestoGastosOp():
    LimpiarPantalla()
    print("\tGASTOS DE OPERACION")

    # GO Primer Semestre
    print("PRIMER SEMESTRE")
    depreciacion_s1 = int(input("Depreciacion : "))
    salarios_s1 = int(input("Salarios: "))
    comisiones_s1 = int(input("Comisiones: "))
    varios_s1 = int(input("Varios: "))
    intereses_s1 = int(input("Intereses por prestamo: "))
    print(f"Total: {depreciacion_s1 + salarios_s1 + comisiones_s1 + varios_s1 + intereses_s1}")

    # GO Segundo Semestre
    print("SEGUNDO SEMESTRE")
    depreciacion_s2 = int(input("Depreciacion : "))
    salarios_s2 = int(input("Salarios: "))
    comisiones_s2 = int(input("Comisiones: "))
    varios_s2 = int(input("Varios: "))
    intereses_s2 = int(input("Intereses por prestamo: "))
    print(f"Total: {depreciacion_s2 + salarios_s2 + comisiones_s2 + varios_s2 + intereses_s2}")
    input("Presione Enter para continuar...")


    # GO TOTAL
    print("\tTOTAL")
    print(f"Total Depreciacion: {depreciacion_s1 + depreciacion_s2}")
    print(f"Sueldos y Salarios: {salarios_s1 + salarios_s2}")
    print(f"Comisiones: {comisiones_s1 + comisiones_s2}")
    print(f"Varios: {varios_s1 + varios_s2}")
    print(f"Intereses por Préstamo: {intereses_s1 + intereses_s2}")
    print(f"Total de Gastos de Operación: {depreciacion_s1+ salarios_s1 +comisiones_s1+ varios_s1 + intereses_s1 + depreciacion_s2 + salarios_s2 + comisiones_s2 + varios_s2 + intereses_s2}")
    separador()
    input("Presione Enter para continuar...")

def costoUnitario():
    LimpiarPantalla()
    print("\tCOSTO UNITARIO PRODUCTO TERMINADO")
    
    # Producto A
    print("PRODUCTO A")
    print("Material A")
    costo_a = int(input("Costo: "))
    cantidad_a = int(input("Cantidad: "))
    costo_unitario = costo_a * cantidad_a 
    print(f"El Costo Unitario es: {costo_unitario}")

    print("Material B")
    costo_b = int(input("Costo: "))
    cantidad_b = int(input("Cantidad: "))
    costo_unitario_b = costo_b * cantidad_b 
    print(f"El Costo Unitario es: {costo_unitario_b}")

    print("Material C")
    costo_c = int(input("Costo: "))
    cantidad_c = int(input("Cantidad: "))
    costo_unitario_c = costo_c * cantidad_c 
    print(f"El Costo Unitario es: {costo_unitario_c}",)

    print("Mano de Obra")
    costo_mano = int(input("Costo"))
    cant_mano = int(input("Cantidad"))
    costo_unitario_mano = costo_mano * cant_mano 
    print(f"El Costo Unitario es: {costo_unitario_mano}")

    print("Gastos Indirectos de Fabricacion")
    costo_gastos_fab = int(input("Costo: "))
    print("Cantidad: ")
    cant_gastos = int(input())
    costo_unitario_fab = costo_gastos_fab * cant_gastos 
    print(f"Costo Unitario: {costo_unitario_fab}")

    print(f"Costo Unitario Total: ${costo_unitario+costo_unitario_b+costo_unitario_c+costo_unitario_mano+costo_unitario_fab}")
    separador()

    # Producto B
    print("PRODUCTO B")
    print("Material A")
    costo_a = int(input("Costo: "))
    cantidad_a = int(input("Cantidad: "))
    costo_unitario = costo_a * cantidad_a 
    print(f"El Costo Unitario es: {costo_unitario}")

    print("Material B")
    costo_b = int(input("Costo: "))
    cantidad_b = int(input("Cantidad: "))
    costo_unitario_b = costo_b * cantidad_b 
    print(f"El Costo Unitario es: {costo_unitario_b}")

    print("Material C")
    costo_c = int(input("Costo: "))
    cantidad_c = int(input("Cantidad: "))
    costo_unitario_c = costo_c * cantidad_c 
    print(f"El Costo Unitario es: {costo_unitario_c}",)

    print("Mano de Obra")
    costo_mano = int(input("Costo: "))
    cant_mano = int(input("Cantidad: "))
    costo_unitario_mano = costo_mano * cant_mano 
    print(f"El Costo Unitario es: {costo_unitario_mano}")

    print("Gastos Indirectos de Fabricacion")
    costo_gastos_fab = int(input("Costo: "))
    print("Cantidad: ")
    cant_gastos = int(input())
    costo_unitario_fab = costo_gastos_fab * cant_gastos 
    print(f"Costo Unitario: {costo_unitario_fab}")

    print(f"Costo Unitario Total ${costo_unitario+costo_unitario_b+costo_unitario_c+costo_unitario_mano+costo_unitario_fab}")
    separador()

    # Producto C
    print("PRODUCTO C")
    print("Material A")
    costo_a = int(input("Costo: "))
    cantidad_a = int(input("Cantidad: "))
    costo_unitario = costo_a * cantidad_a 
    print(f"El Costo Unitario es: {costo_unitario}")

    print("Material B")
    costo_b = int(input("Costo: "))
    cantidad_b = int(input("Cantidad: "))
    costo_unitario_b = costo_b * cantidad_b 
    print(f"El Costo Unitario es: {costo_unitario_b}")

    print("Material C")
    costo_c = int(input("Costo: "))
    cantidad_c = int(input("Cantidad: "))
    costo_unitario_c = costo_c * cantidad_c 
    print(f"El Costo Unitario es: {costo_unitario_c}",)

    print("Mano de Obra")
    costo_mano = int(input("Costo: "))
    cant_mano = int(input("Cantidad: "))
    costo_unitario_mano = costo_mano * cant_mano 
    print(f"El Costo Unitario es: {costo_unitario_mano}")

    print("Gastos Indirectos de Fabricacion")
    costo_gastos_fab = int(input("Costo: "))
    print("Cantidad: ")
    cant_gastos = int(input())
    costo_unitario_fab = costo_gastos_fab * cant_gastos 
    print(f"Costo Unitario: {costo_unitario_fab}")

    print(f"Costo Unitario Total ${costo_unitario+costo_unitario_b+costo_unitario_c+costo_unitario_mano+costo_unitario_fab}")
    separador()
    input("Presione Enter para continuar...")

def InventariosFinales():
    print("\tINVENTARIOS FINALES")
    print("Inventario Final de Materiales")
    print("Material A")
    unidades_a = int(input("Unidades: "))
    costo_a = int(input("Costo Unitario: "))
    costo_total_a = (unidades_a * costo_a)
    print(f"Costo Total: {costo_total_a}")

    print("Material B")
    unidades_b = int(input("Unidades: "))
    costo_b = float(input("Costo Unitario: "))
    costo_total_b = (unidades_b * costo_b)
    print(f"Costo Total: {costo_total_b}")

    print("Material C")
    unidades_c = int(input("Unidades: "))
    costo_c = int(input("Costo Unitario: "))
    costo_c = (unidades_c * costo_c)
    print(f"El costo total es de: {costo_c}")

    inventario_final_mat = (costo_total_a + costo_total_b + costo_c)
    print(f"Inventario Final Material: {inventario_final_mat}")

    print("Inventario Final Producto Terminado")
    print("Producto CL")
    print("Unidades: ")
    UDSA2= int(input())
    print("Costo Unitario: ")
    CUA2= float(input())
    CTA2= (UDSA2 * CUA2)
    print("El costo total es de: ", CTA2)

    print("Producto CE")
    print("Unidades: ")
    UDSB2= int(input())
    print("Costo Unitario: ")
    CUB2= float(input())
    CTB2= (UDSB2 * CUB2)
    print("El costo total es de: ", CTB2)

    print("Producto CR")
    print("Unidades: ")
    UDSC2= int(input())
    print("Costo Unitario: ")
    CUC2= float(input())
    CTC2= (UDSC2 * CUC2)
    print("El costo total es de: ", CTC2)

    inventario_final_mat2= (CTA2 + CTB2 + CTC2)
    print("El inventario final de producto terminado es de: ", inventario_final_mat2)
    separador()
    input("Presione Enter para continuar...")

def EstadoCostoProduccionVenta():
    print("\tESTADO DE COSTOS DE PRODUCCION Y VENTA")
    saldo_inicial = int(input("Saldo Inicial de Materiales: "))
    compras_materiales = int(input("Compras de Materiales: "))
    material_disponible = compras_materiales + saldo_inicial
    print(f"Material Disponible: {material_disponible}")

    inventario_final_m = int(input("Inventario Final de Materiales: "))
    materiales_utilizados = material_disponible - inventario_final_m
    print(f"Materiales Utilizados: {materiales_utilizados}")
    mano_obra_directa = int(input("Mano de Obra Directa: "))
    gastos_fab_indirectos = int(input("Gastos de Fabricación Indirectos: "))
    print(f"Costo de Producción: {materiales_utilizados + mano_obra_directa + gastos_fab_indirectos}")
    inventario_inicial = int(input("Inventario Inicial de Productos Terminados: "))
    total_productos = materiales_utilizados + mano_obra_directa + gastos_fab_indirectos + inventario_inicial
    print(f"Total de Producción Disponible: {total_productos}")
    inventario_final = int(input(f"Inventario Final de Productos Terminados: "))
    print(f"Costo de Ventas: {total_productos-inventario_final}")
    separador()
    input("Presione Enter para continuar...")

def EstadoResultados():
    LimpiarPantalla()
    print("\tESTADO DE RESULTADOS")
    separador()
    VER1 = int(input("Ventas: " ))
    CDV1 = int(input("Costo de Ventas: "))
    UtilidadBruta = VER1-CDV1
    print(f"Utilidad Total Bruta: {UtilidadBruta}")
    GastosO = int(input("Gastos de operacion: "))
    UtilidadO= (UtilidadBruta-GastosO)
    print (f"Total de Utilidad de operacion: {UtilidadO}")
    ISR1 = int(input("ISR: "))
    PTcant_A = int(input("PTU: "))
    UtilidadN = (UtilidadO-ISR1-PTcant_A)
    print (f"Utilidad Neta: {UtilidadN}")
    separador()
    input("Presione Enter para continuar...")

def EstadoFlujoEfectivo():
    LimpiarPantalla()
    print("\tESTADO FLUJO EFECTIVO")
    separador()
    print("---Entradas---")
    cobranza_1 = int(input("Cobranza No.1: "))
    cobranza_2 = int(input("Cobranza No.2: "))
    print(f"Total Entradas: {cobranza_1 + cobranza_2}")
    separador()
    print('---Salidas---')
    proveedor_1 = int(input("Proveedores No.1: "))
    proveedor_2 = int(input("Proveedores No.2: "))
    Pmano_obra_directa= int(input("Pago de Mano de Obra Directa: "))

    gastos_in = int(input("Gastos Indirectos de Fabricación: "))
    gastos_op = int(input("Gastos de Operación: "))
    compra_a = int(input("Compra de Activo Fijo (Maquinaria): "))
    ISR1 = int(input("Pago ISR No.1: "))
    ISR2 = int(input("Pago ISR No.2: "))
    print(f"Total de Salidas: {proveedor_1 + proveedor_2 + Pmano_obra_directa + gastos_in + gastos_op + compra_a + ISR1 + ISR2}")
    separador()
    input("Presione Enter para continuar...")

def BalanceGeneral():
    LimpiarPantalla()
    separador()
    print("\tEMPRESA, S.A. de C.V.")
    print("\tBalance General")
    separador()
    print("---ACTIVOS CIRCULANTES---")
    efectivo_a = int(input("Efectivo: "))
    clientes = int(input("Clientes: "))
    deudores = int(input("Deudores Diversos: "))
    empleados = int(input("Empleados: "))
    inventario_m = int(input("Inventario de Materiales"))
    inventario_producto = int(input("Inventario de Producto Terminado"))
    activo_circulante = efectivo_a + clientes + deudores + empleados + inventario_m + inventario_producto
    print(f"Total ACTIVOS CIRCULANTES: ${activo_circulante}")
    separador()

    print("---ACTIVOS NO CIRCULANTES---")
    terreno = int(input("Terreno: "))
    equipo = int(input("Planta y equipo: "))
    depreciacion = int(input("Depreciación: "))
    activo_no_circulante = terreno + equipo + depreciacion
    print(f"Total ACTIVOS NO CIRCULANTES: ${activo_no_circulante}")
    separador()

    print(f"Total ACTIVOS: {activo_circulante + activo_no_circulante}")

    print("\n---PASIVO CORTO PLAZO---")
    proveedores = int(input("Proveedores: "))
    documentos = int(input("Documentos por Pagar: "))
    ISR = int(input("ISR por Pagar: "))
    PTU = int(input("PTU por pagar: "))
    pasivo_corto_plazo = proveedores + documentos + ISR + PTU
    print(f"Total de PASIVO CORTO PLAZO: ${pasivo_corto_plazo}")
    separador()

    print("---PASIVO LARGO PLAZO---")
    prestamos_bancarios = int(input("Préstamos Bancarios: "))
    print(f"Total de Pasivo a Largo Plazo: ${prestamos_bancarios}")
    pasivo_total = pasivo_corto_plazo + prestamos_bancarios
    print(f"Pasivo Total: {pasivo_total}")
    separador()
    
    print("\n---CAPITAL CONTABLE---")
    cap_aportado = int(input("Capital Aportado"))
    cap_ganado = int(input("Capital Ganado"))
    utilidad = int(input("Utilidad del Ejercicio"))
    total_capital = cap_aportado + cap_ganado + utilidad
    print(f"Total de Capital Contable: ${total_capital}")

    print("\n---PASIVO Y CAPITAl---")
    print(total_capital + pasivo_total)
    separador()
    input("Presione Enter para continuar...")

def main():
    print(f"\tPresupuesto Maestro")
    separador()
    productosABC()
    SaldoFlujo()
    PresupuestoProduccion()
    PresupuestoReqMateriales()
    PresupuestoCompraMateriales()
    SaldoProvFlujo()
    manoObraDirecta()
    gastosIndirectosFabricacion()
    PresupuestoGastosOp()
    costoUnitario()
    InventariosFinales()
    EstadoCostoProduccionVenta()
    EstadoResultados()
    EstadoFlujoEfectivo()
    BalanceGeneral()
#endregion
