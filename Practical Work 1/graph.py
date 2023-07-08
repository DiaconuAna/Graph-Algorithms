import copy
import random

class Graph:
    def __init__(self):
        self._dIn = {}
        self._dOut = {}
        self._dCost = {}
        self._noVertices = 0
        self._noEdges = 0
        self._vertexList = []

    def loadFromFileInit(self, file_name):
        """
        Loads the data  of a directed graph  from  a text file
        :return:
        """
        try:
            f = open(file_name, "r")
            lines = f.readlines()
            f.close()

            #the first line contains the number of vertices and edges
            tokens = lines[0].split()
            if len(tokens) == 2:
                self._noVertices = int(tokens[0])
                edgesNumber = int(tokens[1])
            else:
                raise ValueError("Invalid input!")

            self.EmptyGraphInit(0)
            for index in range(edgesNumber):
                tokens = lines[index+1].split()
                if len(tokens) == 0:
                    break
                startVertex = int(tokens[0])
                endVertex = int(tokens[1])
                edgeCost = int(tokens[2])
                self.addEdge(startVertex, endVertex,  edgeCost)

            #print(edgesNumber+1, len(lines))
        except IOError:
            pass

    def loadFromFile(self, file_name):
        """
        Loads the data  of a directed graph  from  a text file
        :return:
        """
        try:
            f = open(file_name, "r")
            lines = f.readlines()
            f.close()

            self._noEdges = 0

            #the first line contains the number of vertices and edges
            tokens = lines[0].split()
            if len(tokens) == 2:
                self._noVertices = int(tokens[0])
                edgesNumber = int(tokens[1])
            else:
                raise ValueError("Invalid input!")

            #print(edgesNumber)
           # print(self._vertexList)
            #self._noVertices = len(self._vertexList)
            index = 1
            self._vertexList.clear()
            for i in range(self._noVertices):
                self._vertexList.append(int(lines[index]))
                #print(int(lines[index]))
                index += 1

            #print(self._vertexList)
            self.EmptyGraphInit(1)
            for i in range(edgesNumber):
                tokens = lines[index].split()
                #print(lines[index])
                index += 1
                #print(tokens)
                if len(tokens) == 0:
                    break
                startVertex = int(tokens[0])
                endVertex = int(tokens[1])
                edgeCost = int(tokens[2])
                self.addEdge(startVertex, endVertex,  edgeCost)


            while index < len(lines):
                tokens = lines[index].split()
                index+=1
                if (len(tokens)) == 0:
                    break
                self.addVertex(int(tokens[0]))
        except IOError:
            pass

    def writeToFile(self, file_name):
        """
        Write the graph data  to a file
        :return:
        """
        f = open(file_name, "w")
        self._noVertices = len(self._vertexList)
        line = str(self._noVertices)+" "+str(self._noEdges)

        f.write(line)
        f.write("\n")

        for vertex in self._vertexList:
            line = str(vertex)
            f.write(line)
            f.write("\n")

        for edge in self._dCost.keys():
            line = str(edge[0]) + " " + str(edge[1]) + " " + str(self._dCost[edge])
            f.write(line)
            f.write("\n")

        for vertex in self._vertexList:
            if self.checkIsolatedVertex(vertex):
                line = str(vertex)
                f.write(line)
                f.write("\n")

        f.close()

    def addVertex(self,  vertex):
        """
        Add a new vertex  to the graph
        by creating its corresponding
        successors and predecessors  lists, incrementing the vertex number
        and adding it to the vertices list
        Precondition: the vertex must not exist in the graph beforehand
        :param: vertex
        :return: 0 if the vertex already exists and cannot be added, else 1
        """
        #if vertex not in self._vertexList:
        #    self._vertexList.append(vertex)
        if self.checkifVertexExists(vertex) == 1:
            return 0
        self._dIn[vertex] = []
        self._dOut[vertex] = []
        self._vertexList.append(vertex)
        self._noVertices += 1
        return 1

    def removeVertex(self, vertex):
        """
        Remove a vertex from the graph (and the edges containing it)
        Precondition: the vertex must exist in the graph
        :param vertex:
        :return:
        """
        if self.checkifVertexExists(vertex) == 0:
            raise ValueError("Given vertex does not exist in the graph!")
        self._dIn.pop(vertex)
        self._dOut.pop(vertex)

        dict_list = []
        for keys in self._dCost.keys():
            if keys[0] == vertex or keys[1] == vertex:
                dict_list.append(keys)
        if len(dict_list):
            for keys in dict_list:
                self._dCost.pop(keys)
                self._noEdges -= 1

        self._noVertices -= 1
        self._vertexList.remove(vertex)

        for v in self._vertexList:
            if vertex in self._dIn[v]:
                self._dIn[v].remove(vertex)
            if vertex in self._dOut[v]:
                self._dOut[v].remove(vertex)


    def addEdge(self, StartVertex, EndVertex, edgeCost):
        """
        Adds and edge (StartVertex, EndVertex) of cost EdgeCost
        (if it doesn't exists and both vertices are in the graph)
        Preconditions: Both the source and the target vertices must exist
                       The edge must not exist in the graph
        :param StartVertex: the source vertex of  the edge
        :param EndVertex: the target vertex of the edge
        :param edgeCost: the edge's cost
        :return:-
        """
        if self.checkifEdgeExists(StartVertex, EndVertex) == 1:
            raise ValueError("Edge already exists")
        if self.checkifVertexExists(StartVertex) == 0:
            raise ValueError("Vertex ", StartVertex, " does not exist!")
        if self.checkifVertexExists(EndVertex) == 0:
            raise ValueError("Vertex ", EndVertex, " does not exist!")
        self._dIn[EndVertex].append(StartVertex)
        self._dOut[StartVertex].append(EndVertex)
        self._dCost[(StartVertex, EndVertex)] = edgeCost
        self._noEdges += 1

    def removeEdge(self, SourceVertex, TargetVertex):
        """
        Remove an edge identified by its target and source vertices
        Preconditions: both vertices must exist in the graph
                       the edge must exist in the graph
        :param SourceVertex:
        :param TargetVertex:
        :return:
        """
        if self.checkifEdgeExists(SourceVertex, TargetVertex) == 0:
            raise ValueError("Edge must exist in the graph!")
        if self.checkifVertexExists(SourceVertex) == 0:
            raise ValueError("Vertex ", SourceVertex, " does not exist!")
        if self.checkifVertexExists(TargetVertex) == 0:
            raise ValueError("Vertex ", TargetVertex, " does not exist!")
        self._dIn[TargetVertex].remove(SourceVertex)
        self._dOut[SourceVertex].remove(TargetVertex)
        self._dCost.pop((SourceVertex, TargetVertex))
        self._noEdges -= 1

    def EmptyGraphInit(self, id):
        """
        Initialises an empty graph with the
        given number of vertices/ given list of vertices
        :param id: 0 when loading the graph from the initial file, else 1
        :return:
        """
        self._dIn.clear()
        self._dOut.clear()
        self._dCost.clear()

        if id == 1:
            for vertex in self._vertexList:
                self._dIn[vertex] = []
                self._dOut[vertex] = []

        if id == 0:
            for vertex in range(self._noVertices):
                self.addVertex(vertex)

    def checkifEdgeExists(self, StartVertex, EndVertex):
        """
        Checks if an edge already exists in the graph
        :param StartVertex: the starting vertex of  the edge
        :param EndVertex: the ending vertex of the edge
        :return: 1 if the edge already exists, else 0
        """
        if StartVertex not in self._dIn.keys() or EndVertex not in self._dOut.keys():
            return 0
        for vertex in self._dIn[EndVertex]:
            if vertex == StartVertex:
                return 1
        return 0

    def checkifVertexExists(self, vertex):
        """
        Checks if a given vertex exists in the graph
        :param vertex: the given vertex
        :return: 1 if the vertex exists, else   0
        """
        #if vertex not in self._dIn.keys() or vertex not in self._dOut.keys():
        #    return 0
        if vertex not in self._vertexList:
            return 0
        return 1

    @property
    def numberOfVertices(self):
        #print(self._vertexList)
        return len(self._vertexList)

    def inDegree(self, vertex):
        """
        Gets the in degree of a given vertex
        Precondition: the vertex must exist in the graph beforehand
        :param vertex:
        :return:
        """
        if self.checkifVertexExists(vertex) == 0:
            raise ValueError("Given vertex does not exist in the graph.")
        return len(self._dIn[vertex])

    def outDegree(self, vertex):
        """
        Gets the out degree of a given vertex
        Precondition: the vertex must exist in the graph beforehand
        :param vertex:
        :return:
        """
        if self.checkifVertexExists(vertex) == 0:
            raise ValueError("Given vertex does not exist in the graph.")
        return len(self._dOut[vertex])

    def retrieveCost(self, edge):
        """
        Retrieve the information(cost) associated to an edge
        Precondition: check if edge exists
        :param edge:
        :return:
        """
        if self.checkifEdgeExists(edge[0], edge[1]) == 0:
            raise ValueError("Edge does not exist!")
        return self._dCost[edge]

    def modifyCost(self, edge, value):
        """
        Modify the information(cost) associated to an edge
        Precondition: check if edge exists
        :param edge:
        :param value:
        :return:
        """
        if self.checkifEdgeExists(edge[0], edge[1]) == 0:
            raise ValueError("Edge does not exist!")
        self._dCost[edge] = value

    def checkIsolatedVertex(self, vertex):
        """
        Checks if a vertex is an isolated one
        Precondition: check if vertex exists
        :param vertex:
        :return: 1 if the vertex is isolated (both its in-degree and out-degree are zero), else 0
        """
        if self.checkifVertexExists(vertex) == 0:
            raise ValueError("Vertex does not exist in the graph!")

        if len(self._dIn[vertex]) == 0 and len(self._dOut[vertex]) == 0:
            return 1
        return 0

    def parseVertices(self):
        """
        Parse through the set of vertices in the graph
        :return:
        """
        return [x for x in self._vertexList]

    def parseInbound(self, vertex):
        """
        Parse the set of inbound edges of a specified vertex and
        provide the source vertex for each
        Precondition: the vertex must exist in the graph
        :param vertex:
        :return:
        """
        if self.checkifVertexExists(vertex) == 0:
            raise ValueError("Given vertex does not exist in the graph! ")
        return [source for source in self._dIn[vertex]]

    def parseOutbound(self, vertex):
        """
        parsethe set of outbound edges of a specified vertex and
        provide the target vertex  for each
        Precondition: the vertex must exist in the graph
        :param vertex:
        :return:
        """
        if self.checkifVertexExists(vertex) == 0:
            raise ValueError("Given vertex does not exist in the graph! ")
        return [source for source in self._dOut[vertex]]

    def copy(self):
        """
        Returns a copy of the graph
        :return:
        """
        return copy.deepcopy(self)






