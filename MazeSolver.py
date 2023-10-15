class MazeSolver:
    
    def __init__(self):
        self.caminos = []
        self.camino = []
    
    # valida que tenga entrada y salida unica
    def entrada_salida(self, maze):
        startX = startY = endX = endY = contadorEntradasSalidas = 0
        for i in range( len(maze) ):
            for j in range( len(maze[i]) ):
                if maze[i][j] == 0 and (i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[i]) - 1):
                    if contadorEntradasSalidas == 0:
                        startX = j
                        startY = i
                    elif contadorEntradasSalidas == 1:
                        endX = j
                        endY = i
                    contadorEntradasSalidas += 1
        if contadorEntradasSalidas == 2: return self.solve(maze, startX, startY, endX, endY) 
        return False 

    # valida la correcta forma del laberinto
    def validar(self, maze):
        for i in range( len(maze) ):
            for j in range( len(maze[i]) ):
                if 0 <= i < len(maze) - 1 and 0 <= j < len(maze[i]) - 1 :
                    if maze[i][j] == 0 and maze[i][j + 1] == 0 and maze[i + 1][j] == 0 and maze[i + 1][j + 1] == 0:
                        return False
                    if maze[i][j] == 1 and maze[i][j + 1] == 1 and maze[i + 1][j] == 1 and maze[i + 1][j + 1] == 1:
                        return False
        return self.entrada_salida(maze)
        
    # busca las soluciones
    def solve(self, maze, startX, startY, endX, endY):
        rows = len(maze)
        colums = len(maze[0])
        
        # verifica si estamos fuera de los límites o en una celda bloqueada
        if startX >= colums or startX < 0 or startY >= rows or startY < 0 or maze[startY][startX] == 1:
            return False
        
        # Verificar si hemos llegado a la salida
        if startX == endX and startY == endY:
            # print("Marca la posicion final ("+ str(startY) +" , " + str(startX) +")")
            # self.camino.append([startY, startX])
            aux = self.camino.copy()
            aux.append([startY, startX])
            self.caminos.append(aux)
            # print("_______________________________________________________________")
            return False
            # return True
        
        # Marcar la celda como visitada
        maze[startY][startX] = 1
        self.camino.append([startY, startX])
        # print("Marca la posicion ("+ str(startY) +" , " + str(startX) +")")
        
        # Explorar las cuatro direcciónes posibles
        if (
            self.solve(maze, startX + 1, startY, endX, endY) or
            self.solve(maze, startX, startY + 1, endX, endY) or 
            self.solve(maze, startX - 1, startY, endX, endY) or
            self.solve(maze, startX, startY - 1, endX, endY)
            ):
            return True 
        
        # Si ninguna dirección lleva a la solución, desmarcar la celda
        maze[startY][startX] = 0
        self.camino.remove([startY, startX])
        # print("Des marca la posicion ["+ str(startY) +" , " + str(startX) +"]")
        
        return False
    
    def getCaminos(self):
        return self.caminos
    
    def mostrarCaminos(self):
        for i in range(len(self.caminos)):
            print("Camino #"+ str(i + 1) +":")
            print(self.caminos[i])
            print()