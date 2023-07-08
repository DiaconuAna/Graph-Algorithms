#pragma once
#include <vector>
#include "vectorIterator.h"

using namespace std;
typedef vector <vector <int>> AdjacentVertexList;

class Graph {
private:
    ;

protected:
    int nr_activeV;
    int nr_vertices;
    int nr_edges;
    AdjacentVertexList inEdges;
    AdjacentVertexList outEdges;

    int getEdge(int svf, int evf, AdjacentVertexList v);

public:
    Graph();
    void init_g(int nr_v);
    void clear_graph();
    int get_nrE();
    int get_nrV();
    int get_nrActiveV();
    bool isActiveVertex(int vertex);
    bool is_edge(int svf, int evf);
    int getInDegree(int vertex);
    int getOutDegree(int vertex);
    VectorIterator in_iterator(int vertex);
    VectorIterator out_iterator(int vertex);
    void add_edge(int svf, int evf);
    void remove_edge(int svf, int evf);
    void add_vertex();
    void remove_vertex(int vertex);
};
