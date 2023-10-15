from game2dboard import Board
import threading
import time

    
def mostrar(matriz, caminos) :
    rows = len(matriz)
    cols = len(matriz[0])

    b = Board( int(rows), int(cols) )
    b.title = "Laberinto"
    b.cell_size = 60
    b.cell_color = "white"
    b.grid_color= "blue"
    
    for i in range(rows) :
        for j in range(cols) :
            if matriz[i][j] == 1 :
                b[i][j] = "cuadro.png"
                
    # aux = []
    # for i in resultado :
    #     aux.append(i.split("\n"))
        
    # for i in aux :
    #     i.remove("")
    
    # aux2 = []
    # for i in aux :
    #     for j in i :
    #         aux2.append(j)
    
    t = threading.Thread(target=timer, args=(caminos, b,))
    t.start()
    b.show()
        
    
def timer(caminos, b) :
    for camino in caminos :
        for i in camino:
            b[i[0]][i[1]] = "cuadro2.png"    
            time.sleep(0.25)
            b[i[0]][i[1]] = None
        
      
    
    