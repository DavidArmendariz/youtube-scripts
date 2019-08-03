no_cambia_puerta = function(n){
  x = list()
  for(i in 1:n){
    l = c(0,0,0)
    index1 = sample(1:3,1)
    l[index1] = 1
    x[[i]] = l
  }
  aciertos = 0
  for(r in x){
    puerta_escogida = sample(1:3,1)
    puerta_con_premio = match(1,r)
    if(puerta_escogida==puerta_con_premio){
      aciertos = aciertos+1
    }
  }
  prob = (aciertos/length(x))*100
  sprintf("%.2f %%",prob)
}

cambia_puerta = function(n){
  x = list()
  for(i in 1:n){
    l = c(0,0,0)
    index1 = sample(1:3,1)
    l[index1] = 1
    x[[i]] = l
  }
  aciertos = 0
  for(r in x){
    puerta_escogida = sample(1:3,1)
    ind_puerta_con_premio = match(1,r)
    puertas_con_cabras = c(1:3)
    puertas_con_cabras = puertas_con_cabras[-ind_puerta_con_premio]
    puerta_mostrada = 0
    if(puerta_escogida==ind_puerta_con_premio){
      puerta_mostrada = sample(puertas_con_cabras,1)
    }
    else{
      puertas_con_cabras=puertas_con_cabras[puertas_con_cabras!=puerta_escogida]
      puerta_mostrada=puertas_con_cabras[1]
    }
    puerta_cambiada = c(1:3)
    puerta_cambiada = puerta_cambiada[puerta_cambiada!=puerta_escogida]
    puerta_cambiada = puerta_cambiada[puerta_cambiada!=puerta_mostrada]
    puerta_cambiada = puerta_cambiada[1]
    if(puerta_cambiada == ind_puerta_con_premio){
      aciertos = aciertos+1
    }
  }
  prob = (aciertos/length(x))*100
  sprintf("%.2f %%",prob)
}
