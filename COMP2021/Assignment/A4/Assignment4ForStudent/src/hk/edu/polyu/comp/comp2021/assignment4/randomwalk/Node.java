package hk.edu.polyu.comp.comp2021.assignment4.randomwalk;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Random;

class Node{

    // degree of a node is the number of adjacency nodes, i.e., the number of nodes that are connected to this node by an edge.
    private int degree;

    //The graph this node belongs to
    private Graph graph;

    public Graph getGraph(){
        return this.graph;
    }

    public void setGraph(Graph graph){
        this.graph = graph;
    }

    // Task 1: Obtain the degree of this by referring to all the random walk sequences.
    public void setDegree(){
        int degree = 0;
        HashSet<RandomWalkSequence> allRandomWalkSequence = getGraph().getAllRandomWalkSequences();
        ArrayList<Node> iList = new ArrayList<>();
        for (RandomWalkSequence i: allRandomWalkSequence){
            iList = i.getSequence();
            if (iList.contains(this))
                degree++;
        }
        this.degree = degree - 1;
    }

    public int getDegree(){
        return this.degree;
    }

    // Task 2: Given another node o, obtain the transition probability from this node to the given node.
    // transition probability is calculated by f(this, o) / f(this, all).
    // f(this, o) is the frequency of o as the next node of this within all random walk sequences.
    // f(this, all) is the frequency of this having a next node within all random walk sequences.
    // When f(this, all) = 0, the transition probability is 0.
    public double transitionProbability(Node o){
        double f_this_o = 0;
        double f_this_all = 0;
        HashSet<RandomWalkSequence> allRandomWalkSequence = getGraph().getAllRandomWalkSequences();

        for (RandomWalkSequence i: allRandomWalkSequence){
            ArrayList<Node> iList = new ArrayList<>();
            iList = i.getSequence();
            if(iList.contains(this)){
                int thisIndex = iList.indexOf(this);
                if (thisIndex != iList.size() - 1){
                    f_this_all++;
                }
                if(iList.get(thisIndex+1) == o
                        && thisIndex != iList.size() - 1)

                    f_this_o++;
            }
        }
        if(f_this_all == 0)
            return 0;

        return f_this_o/f_this_all;
    }
}