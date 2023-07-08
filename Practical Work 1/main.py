import random

from graph import Graph


class UI:
    def __init__(self, graph):
        self._graph = graph

    def loadFromFile(self, fileName):
        print("First time loading the graph? \n 1. Yes \n 2. No")
        command = int(input())
        if command == 1:
            self._graph.loadFromFileInit(fileName)
        else:
            self._graph.loadFromFile(fileName)

    def saveToFile(self, fileName):
        self._graph.writeToFile(fileName)

    @staticmethod
    def randomGraphGenerator(vertexNumber, edgeNumber, fileName):
        """
        Generate a random graph with specified number of vertices and of edges
        Precondition: number of edges can be maximum the square of number of edges
        Also  write it to a file
        :param vertexNumber: the number of vertices
        :param edgeNumber: the number of edges
        :param fileName: the name of  the file the graph will be saved to
        :return:
        """
        RandomGraph = Graph()
        if edgeNumber > vertexNumber * vertexNumber:
            raise ValueError("Invalid input")

        RandomGraph._noVertices = vertexNumber
        RandomGraph._noEdges = 0

        RandomGraph.EmptyGraphInit(0)

        while (RandomGraph._noEdges < edgeNumber):
            startVertex = random.randint(0, vertexNumber - 1)
            endVertex = random.randint(0, vertexNumber - 1)
            cost = random.randint(-1000, 1000)
            try:
                RandomGraph.addEdge(startVertex, endVertex, cost)
            except:
                pass

        RandomGraph.writeToFile(fileName)

    @staticmethod
    def  menu():
        print()
        print("0.Load the graph from a file //start version.")
        print("1.Load the graph from a file //isolated vertices version")
        print("2.Save the graph to a file.")
        print("3.Generate a random graph")
        print("4.Get the number of vertices")
        print("5.Given two vertices, find out whether there is an edge from the first one to the second one.")
        print("6.Get the in-degree of a given vertex")
        print("7.Get the out-degree of a given vertex")
        print("8.Retrieve the cost of  a given edge")
        print("9.Modify the cost of a given edge")
        print("10.Parse the set of vertices")
        print("11.Parse the set of outbound edges of a specified vertex and provide the target vertex for each")
        print("12.Parse the set of inbound edges of a specified vertex and provide the source vertex for each")
        print("13.Add an edge")
        print("14.Remove an edge")
        print("15.Add a vertex")
        print("16.Remove a vertex")
        print("17.Get a copy of the graph")
        print("18.Exit")

    def main_menu(self):
        over = 0

        while not over:
            self.menu()
            command = int(input("Choose an option: "))
            if command == 0:
                fileName = input("Input a file name: ")
                self._graph.loadFromFileInit(fileName)
            elif command == 1:
                fileName = input("Input a file name: ")
                self._graph.loadFromFile(fileName)
            elif command == 2:
                fileName = input("Input a file name: ")
                self.saveToFile(fileName)
            elif command == 3:
                fileName = input("Input a file name: ")
                vertexNumber = int(input("How many vertices? "))
                edgeNumber= int(input("How many edges? "))
                try:
                    self.randomGraphGenerator(vertexNumber, edgeNumber, fileName)
                except ValueError as verror:
                    print(str(verror))
            elif command == 4:
                vertexNumber = self._graph.numberOfVertices
                print("The number of vertices is ", vertexNumber)
            elif command == 5:
                startVertex = int(input("Input the source vertex: "))
                endVertex = int(input("Input the target vertex: "))
                result = self._graph.checkifEdgeExists(startVertex, endVertex)
                if result == 1:
                    print("The edge (",startVertex,",",endVertex,") exists!")
                else:
                    print("The edge (",startVertex,",",endVertex,") does not exist!")
            elif command == 6:
                try:
                    vertex = int(input("Pick a vertex: "))
                    result = self._graph.inDegree(vertex)
                    print("The in-degree of the vertex is: ",result)
                except ValueError as verror:
                    print(str(verror))
            elif command == 7:
                try:
                    vertex = int(input("Pick a vertex: "))
                    result = self._graph.outDegree(vertex)
                    print("The out-degree of the vertex is: ",result)
                except ValueError as verror:
                    print(str(verror))
            elif command == 8:
                try:
                    source = int(input("Input the source vertex of your edge:"))
                    destination = int(input("Input the destination vertex of your edge:"))
                    print("The given edge has the cost of", self._graph.retrieveCost((source, destination)))
                except ValueError as verror:
                    print(str(verror))
            elif command == 9:
                try:
                    source = int(input("Input the source vertex of your edge:"))
                    destination = int(input("Input the destination vertex of your edge:"))
                    value = int(input("Input new edge value: "))
                    self._graph.modifyCost((source,destination), value)
                except ValueError as verror:
                    print(str(verror))
            elif command == 10:
                iterator = self._graph.parseVertices()
                for vertex in iterator:
                    print(vertex, end=" ")
            elif command == 11:
                try:
                    vertex = int(input("Provide a vertex>> "))
                    iterator = self._graph.parseOutbound(vertex)
                    if (len(iterator) == 0):
                        print("Given vertex does not have any outbound edges")
                    for source in iterator:
                        print(source, end= " ")
                except ValueError as verr:
                    print(str(verr))
            elif command == 12:
                try:
                    vertex = int(input("Provide a vertex>> "))
                    iterator = self._graph.parseInbound(vertex)
                    if (len(iterator) == 0):
                        print("Given vertex does not have any inbound edges")
                    for source in iterator:
                        print(source, end= " ")

                except ValueError as verr:
                    print(str(verr))
            elif command == 13:
                try:
                    source = int(input("Please provide a source vertex: "))
                    target = int(input("Please provide a target vertex: "))
                    cost = int(input("Please provide an edge cost: "))
                    self._graph.addEdge(source, target, cost)
                except ValueError as verror:
                    print(str(verror))
            elif command == 14:
                try:
                    source = int(input("Please provide a source vertex: "))
                    target = int(input("Please provide a target vertex: "))
                    self._graph.removeEdge(source, target)
                except ValueError as verror:
                    print(str(verror))
            elif command == 15:
                vertex = int(input("Please provide a vertex: "))
                if self._graph.addVertex(vertex) == 0:
                    print("Vertex could not be added as it already exists in the graph")
            elif command == 16:
                try:
                    vertex = int(input("Please provide a vertex: "))
                    self._graph.removeVertex(vertex)
                except ValueError as verror:
                    print(str(verror))
            elif command == 17:
                GraphCopy = Graph()
                GraphCopy = self._graph.copy()
            elif command == 18:
                over = 1
                print("Come back soon!")



if __name__ == '__main__':
    graph = Graph()
    UI = UI(graph)
    UI.main_menu()
