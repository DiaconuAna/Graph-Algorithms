#include "wgraph.h"
#include <iostream>

WGraph::WGraph() : Graph() {};

WGraph::WGraph(const WGraph &original) {
    this->nr_activeV = original.nr_activeV;
    this->nr_vertices = original.nr_vertices;
    this->nr_edges = original.nr_edges;
    this->inEdges = original.inEdges;
    this->outEdges = original.outEdges;
    this->costEdges = original.costEdges;
}

WGraph& WGraph::operator=(const WGraph& original){
    if (this != &original){
        this->nr_activeV = original.nr_activeV;
        this->nr_vertices = original.nr_vertices;
        this->nr_edges = original.nr_edges;
        this->inEdges = original.inEdges;
        this->outEdges = original.outEdges;
        this->costEdges = original.costEdges;
    }
    return *this;
}

int WGraph::get_cost(int svf, int evf, bool doChecks) {
    if (doChecks and getEdge(svf, evf, Graph::outEdges) == -1)
        throw 1;

    return costEdges[Edge(svf, evf)];
}

void WGraph::m_cost(int svf, int evf, int new_cost, bool doChecks) {
    if (doChecks and getEdge(svf, evf, Graph::outEdges) == -1)
        throw 1;

    costEdges[Edge(svf, evf)] = new_cost;
}

void WGraph::add_edge(int svf, int evf, int cost, bool doChecks) {
    if (doChecks and (!isActiveVertex(svf) or !isActiveVertex(evf) or is_edge(svf, evf))) {
        throw 1;
    }

    Graph::outEdges[svf].push_back(evf);
    Graph::inEdges[evf].push_back(svf);

    Edge nEdge(svf, evf);
    costEdges[nEdge] = cost;
    nr_edges++;
}

void WGraph::remove_edge(int svf, int evf) {
    Graph::remove_edge(svf, evf);
    costEdges.erase(Edge(svf,evf));

}

void WGraph::print_graph() {
    for (auto costEdgesIter : costEdges) {
        cout << costEdgesIter.first.svf << " " << costEdgesIter.first.evf << " " << costEdgesIter.second << "\n";
    }
}

void WGraph::remove_vertex(int vertex) {
    for (VectorIterator iter(outEdges[vertex]); iter.isValid(); ++iter) {
        costEdges.erase(Edge(vertex, (*iter)));
    }
    Graph::remove_vertex(vertex);
}

void WGraph::clear_graph() {
    Graph::clear_graph();
    costEdges.clear();
}