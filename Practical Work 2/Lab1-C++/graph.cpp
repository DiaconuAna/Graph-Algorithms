#include "graph.h"
#include <iostream>

using namespace std;

int Graph::getEdge(int svf, int evf, AdjacentVertexList v) {
    int pos = 0;

    if (!isActiveVertex(svf) or !isActiveVertex(evf))
        return -1;

    for (VectorIterator iter(v[svf]); iter.isValid(); ++iter,  ++pos){
        if ((*iter) == evf)
            return pos;
    }

    return -1;
}

bool Graph::isActiveVertex(int vertex) {
    return vertex < nr_vertices and !(inEdges[vertex].size() == 1 and inEdges[vertex][0] == -1);
}

Graph::Graph(){
    nr_activeV = 0;
    nr_vertices = 0;
    nr_edges = 0;

}

void Graph::init_g(int nr_v){
    vector <int> empty;

    for (int i = 0; i < nr_v; i++){
        inEdges.push_back(empty);
        outEdges.push_back(empty);
    }
}

void Graph::clear_graph() {
    nr_activeV = 0;
    nr_vertices = 0;
    nr_edges = 0;
    inEdges.clear();
    outEdges.clear();
}

int Graph::get_nrE() {
    return nr_edges;
}

int Graph::get_nrV() {
    return nr_vertices;
}

int Graph::get_nrActiveV(){
    return nr_activeV;
}

bool Graph::is_edge(int svf, int evf){
    return (getEdge(svf, evf, outEdges) != -1);
}

int Graph::getInDegree(int vertex) {
    return inEdges[vertex].size();
}

int Graph::getOutDegree(int vertex) {
    return outEdges[vertex].size();
}

VectorIterator Graph::in_iterator(int vertex) {
    return VectorIterator(inEdges[vertex]);
}

VectorIterator Graph::out_iterator(int vertex) {
    return VectorIterator(outEdges[vertex]);
}

void Graph::add_edge(int svf, int evf) {
    if (is_edge(svf, evf))
        throw 1;

    outEdges[svf].push_back(evf);
    inEdges[evf].push_back(svf);
    nr_edges++;
}

void Graph::remove_edge(int svf, int evf) {
    int in_ePos = getEdge(evf, svf, inEdges);
    int out_ePos = getEdge(svf, evf, outEdges);

    if (in_ePos == -1 or out_ePos == -1)
        throw 1;

    outEdges[svf].erase(outEdges[svf].begin() + out_ePos);
    inEdges[evf].erase(inEdges[evf].begin() + in_ePos);
    nr_edges--;
}

void Graph::add_vertex() {
    vector <int> empty;

    inEdges.push_back(empty);
    outEdges.push_back(empty);
    nr_activeV++;
    nr_vertices++;
}

void Graph::remove_vertex(int vertex) {
    if (!isActiveVertex(vertex))
        throw 1;

    vector <int> temp;
    temp = inEdges[vertex];

    for (VectorIterator iter(temp); iter.isValid(); ++iter)
        remove_edge((*iter), vertex);

    inEdges[vertex].clear();

    temp = outEdges[vertex];
    for (VectorIterator iter(temp); iter.isValid(); ++iter)
        remove_edge(vertex, (*iter));

    outEdges[vertex].clear();

    inEdges[vertex].push_back(-1);
    outEdges[vertex].push_back(-1);

    nr_activeV--;
}
