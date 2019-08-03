import random
def no_cambia_puerta(n):
    x = []
    #aqui creamos los resultados
    for i in range(n):
        l = [0,0,0]
        index1 = random.randint(0,2)
        l[index1] = 1
        x.append(l)
    #aqui ahora vamos a jugar
    #en este caso no vamos a cambiar de puerta
    #nos quedamos con la puerta original
    aciertos = 0
    for r in x:
        puerta_escogida = random.randint(0,2)
        puerta_con_premio = r.index(1)
        if puerta_escogida == puerta_con_premio:
            aciertos += 1
    prob = (aciertos/len(x))*100
    print("{:.2f}%".format(prob))

def cambia_puerta(n):
    x = []
    #aqui creamos los resultados
    for i in range(n):
        l = [0,0,0]
        index1 = random.randint(0,2)
        l[index1] = 1
        x.append(l)
    #aqui ahora vamos a jugar
    #en este caso cambiamos la puerta
    aciertos = 0
    for r in x:
        puerta_escogida = random.randint(0,2)
        ind_puerta_con_premio = r.index(1)
        puertas_con_cabras = [0,1,2]
        del puertas_con_cabras[ind_puerta_con_premio]
        puerta_mostrada = 0
        if puerta_escogida == ind_puerta_con_premio:
            puerta_mostrada = random.choice(puertas_con_cabras)
        else:
            puertas_con_cabras.remove(puerta_escogida)
            puerta_mostrada = puertas_con_cabras[0]
        puerta_cambiada = [e for e in [0,1,2] if e not in (puerta_escogida,puerta_mostrada)]
        puerta_cambiada = puerta_cambiada[0]
        if puerta_cambiada == ind_puerta_con_premio:
            aciertos += 1
    prob = (aciertos/len(x))*100
    print("{:.2f}%".format(prob))
        
    
