from MazeSolver import MazeSolver
import Interfaz
import csv

class Main:
    def __init__(self):
        self.maze = self.leerArchivo()
        mazeSolver = MazeSolver()
        solucion = mazeSolver.validar(self.maze)
        mazeSolver.mostrarCaminos()
        self.caminos = mazeSolver.getCaminos()
        self.resultado(solucion)
        Interfaz.mostrar(self.maze, self.caminos)

    # Funcion de lectura del archivo
    def leerArchivo(self):
        file_read = csv.reader(open("mazeSolverP/archivo.csv")) # Ruta del archivo local
        maze = [ [ int(data) for data in row] for row in file_read] 
        return maze
    
    def resultado(self, solucion):
        if solucion : 
            print("Tiene unica solucion") 
        else :
            print("Tiene multiples soluciones")
    
        
        
a = Main()