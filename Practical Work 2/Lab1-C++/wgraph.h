#pragma once
#include "graph.h"
#include <unordered_map>
#include "customHash.h"

class WGraph : public Graph {
public:
    unordered_map <Edge, int, CustomHashFunction> costEdges;

    WGraph();
    WGraph(const WGraph& original);
    WGraph& operator=(const WGraph& original);
    void clear_graph();
    int get_cost(int svf, int evf, bool doChecks = true);
    void m_cost(int svf, int evf, int new_cost, bool doChecks = true);
    void add_edge(int svf, int evf, int cost, bool doChecks = true);
    void remove_edge(int svf, int evf);
    void print_graph();
    void remove_vertex(int vertex);

};