#include <fstream>
#include <iostream>
#include "wgraph.h"

using namespace std;

void load(WGraph &g){
    int svf, evf, cost;
    int nr_v, nr_e;
    g.clear_graph();

    ifstream in(R"(D:\Faculty\Graph algo\Lab1-C++\graph.txt)");
    in >> nr_v >> nr_e;

    for (int i = 0; i < nr_v; i++)
        g.add_vertex();

    for (int i = 0; i < nr_e; i++){
        in >> svf >> evf >> cost;
        g.add_edge(svf, evf, cost, false);
    }

    in.close();
}

void save1(WGraph &g){
    ofstream out(R"(D:\Faculty\Graph algo\Lab1-C++\random_graph1.txt)");

    out << g.get_nrV() << " " << g.get_nrE() << "\n";

    for (auto cost : g.costEdges){
        out << cost.first.svf << " " << cost.first.evf << " " << cost.second << "\n";
    }

    out.close();
}

void save2(WGraph &g){
    ofstream out(R"(D:\Faculty\Graph algo\Lab1-C++\random_graph2.txt)");

    out << g.get_nrV() << " " << g.get_nrE() << "\n";

    for (auto cost : g.costEdges){
        out << cost.first.svf << " " << cost.first.evf << " " << cost.second << "\n";
    }

    out.close();
}

void save(WGraph &g){

    ofstream out(R"(D:\Faculty\Graph algo\Lab1-C++\savedg.txt)");

    out << g.get_nrV() << " " << g.get_nrE() << "\n";

    for (auto cost : g.costEdges){
        out << cost.first.svf << " " << cost.first.evf << " " << cost.second << "\n";
    }

    out.close();
}

void generate_r(WGraph& g, int nr_v, int nr_e){
    if (nr_v * nr_v < nr_e) {
        cout << "Invalid number of vertices / edges\n";
        throw 19;
    }
    int svf, evf, cost;
    g.clear_graph();

    for (int i = 0; i < nr_v; i++) {
        g.add_vertex();
    }

    while (nr_e > 0) {
        svf = rand() % nr_v;
        evf = rand() % nr_v;
        try {
            cost = rand() % 100;
            g.add_edge(svf, evf, cost);
            nr_e--;
        }
        catch (...) {
            ;
        }
    }
}

void p_menu(){
    cout << "0. Exit\n";
    cout << "1. Number of vertices\n";
    cout << "2. Parse the set of vertices\n";
    cout << "3. Check if the edge exists\n";
    cout << "4. Determine the in / out degree of a vertex\n";
    cout << "5. Parse the set of inbound edges of a vertex\n";
    cout << "6. Parse the set of outbound edges of a vertex\n";
    cout << "7. Get the cost of an edge\n";
    cout << "8. Modify the cost of an edge\n";
    cout << "9. Add edge\n";
    cout << "10. Remove edge\n";
    cout << "11. Add vertex\n";
    cout << "12. Remove vertex\n";
    cout << "13. Load the graph from a file\n";
    cout << "14. Save the graph to a file\n";
    cout << "15. Get a randomised graph\n";
}

int main(){

    int op, save_op;
    int svf, evf, cost, nr_v, nr_e;
    WGraph g;

    while(true){
        p_menu();
        cout << "Insert the option: \n";
        cin >> op;
        try {
            switch (op) {
                case 0: return 0;
                case 1:
                    cout << "Nr of vertices = " << g.get_nrActiveV() << "\n";
                    break;
                case 2:
                    for (int i = 0; i < g.get_nrV(); i++) {
                        if (g.isActiveVertex(i)) {
                            cout << i << " ";
                        }
                    }
                    cout << "\n";
                    break;
                case 3:
                    cout << "Insert starting vertex and ending vertex:\n";
                    cin >> svf >> evf;
                    if (g.is_edge(svf, evf)) {
                        cout << "The edge exists\n";
                    }
                    else {
                        cout << "The edge doesn't exist\n";
                    }
                    break;
                case 4:
                    cout << "Insert vertex:\n";
                    cin >> svf;
                    cout << "In degree: " << g.getInDegree(svf) << "\n";
                    cout << "Out degree: " << g.getOutDegree(svf) << "\n";
                    break;
                case 5:
                    cout << "Insert vertex:\n";
                    cin >> svf;
                    for (auto iter = g.in_iterator(svf); iter.isValid(); ++iter) {
                        cout << (*iter) << " -> " << svf << "\n";
                    }
                    cout << "\n";
                    break;
                case 6:
                    cout << "Insert vertex:\n";
                    cin >> svf;
                    for (auto iter = g.out_iterator(svf); iter.isValid(); ++iter) {
                        cout << svf << " -> " << (*iter) << "\n";
                    }
                    cout << "\n";
                    break;
                case 7:
                    cout << "Insert starting vertex and ending vertex:\n";
                    cin >> svf >> evf;
                    cout << g.get_cost(svf, evf) << "\n";
                    break;
                case 8:
                    cout << "Insert starting vertex, ending vertex and cost:\n";
                    cin >> svf >> evf >> cost;
                    g.m_cost(svf, evf, cost);
                    break;
                case 9:
                    cout << "Insert starting vertex, ending vertex and cost:\n";
                    cin >> svf >> evf >> cost;
                    g.add_edge(svf, evf, cost);
                    break;
                case 10:
                    cout << "Insert starting vertex and ending vertex:\n";
                    cin >> svf >> evf;
                    g.remove_edge(svf, evf);
                    break;
                case 11:
                    g.add_vertex();
                    break;
                case 12:
                    cout << "Insert vertex\n";
                    cin >> svf;
                    g.remove_vertex(svf);
                    break;
                case 13:
                    load(g);
                    break;
                case 14:
                    save(g);
                    break;
                case 15:
                    cout << "Insert nr. vertices and edges::\n";
                    cin >> nr_v >> nr_e;
                    cout <<"Insert 1 or 2:\n";
                    cin >> save_op;
                    if (save_op == 1){
                        generate_r(g, nr_v, nr_e);
                        save1(g);
                    }
                    else if (save_op == 2){
                        generate_r(g, nr_v, nr_e);
                        save2(g);
                    }
                    break;
                default: throw 19;
            }
        }
        catch (...) {
            cout << "There has been an error. The operation was not performed\n";
        }
    }
    return 0;
}

