def analizador_finaciero():
    #preguntas para analizar el ahorro
    dinero=float(input("¿cuànto dinero tienes actualmente? "))
    ganancia=float(input("cuanto ganas por semana?"))
    meta=float(input("cuàl es tu meta de ahorro?"))
    #lista para la asignacion de gastos
    gastos=[]  
    cantidad_gastos=int(input("cuantos gastos quieres registrar?"))
    for i in range(cantidad_gastos):
        gasto=float(input(f"gasto{i+1}:"))
        gastos.append(gasto)
    total_gastos=0
    for g in gastos:
        total_gastos=total_gastos+g
    # mayor gasto
    gasto_mayor_50=0
    mayor_gasto=0
    for mg in gastos:
        if mg>mayor_gasto:
            mayor_gasto=mg
        if mg>50:
            gasto_mayor_50=gasto_mayor_50+1
    # cuanto ahorras
    cuanto_ahorras=ganancia-total_gastos
    semanas=0
    while dinero<meta:
        dinero=dinero+cuanto_ahorras
        semanas=semanas+1
    # unidad de tiempo
    if semanas<=4:
        tiempo= semanas
        unidad="semanas"
    elif semanas<=48:
        tiempo=semanas/4
        unidad="meses"
    else:
        tiempo=semanas/52
        unidad="años"
    if cuanto_ahorras<=99:
        print("tu capacidad de ahorro es baja, te recomiendo que reduzcas tus gastos")
    elif cuanto_ahorras<=199:
        print("tu capacidad de ahorro es media, te recomiendo que reduzcas tus gastos")
    else:
        print("tu capacidad de ahorro es alta, mantente así")

    print(f"tu ahorro total es de ${dinero:,.2f},tu ganancia semanal es de ${ganancia:,.2f}, tus gastos totales fueron de ${total_gastos:,.2f} tus gastos mayor es de ${mayor_gasto:,.2f}, tu meta de ahorro es de ${meta:,.2f}, el tiempo que te tomara alcanzar tu meta es de {tiempo:.2f} {unidad}, porque tu ahorro semanal es de {cuanto_ahorras:,.2f} a la semana")
analizador_finaciero()


    
    
           

    






