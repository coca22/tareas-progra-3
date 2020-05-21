class Triatlon():
    triatlon = [[0,0,0],[0,0,0]]
    tiempoGanador= 0

    for equipo in range (0, 2):
        for atletas in range(0, 3):

            tiempo = float(input("Favor ingresar el tiempo  del " + str(atletas + 1) + "  triatleta : " + str(equipo + 1) + "  "))

            triatlon[equipo][atletas] = tiempo

    for equipo in range (0, 2):

        acumuladorTiempo =0

        for atletas in range(0, 3):
            acumuladorTiempo = acumuladorTiempo + triatlon[equipo][atletas]

       # promedioTiempo = float(acumuladorTiempo / 3)


        if acumuladorTiempo==triatlon[equipo]:
            print("EL ganador es "+ str(acumuladorTiempo))

        #if(promedioTiempo< tiempoGanador):
         #   tiempoGanador = promedioTiempo


        print("El promedio tiempo del Equipo " + str(equipo + 1) + " es de:" + str(acumuladorTiempo))

   # print("El Equipo ganador obtuvo un tiempo de: " + str(tiempoGanador))
