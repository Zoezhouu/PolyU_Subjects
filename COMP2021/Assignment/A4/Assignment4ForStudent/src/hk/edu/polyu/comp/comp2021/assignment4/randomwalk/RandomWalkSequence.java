package hk.edu.polyu.comp.comp2021.assignment4.randomwalk;

import java.util.ArrayList;
import java.util.HashSet;

class RandomWalkSequence{

    // A random walk sequence is stored as a list of nodes
    private ArrayList<Node> sequence;

    // Each random walk sequence is a list of nodes that appear in the order at which they are visited by the random walk.
    // Given a starting node, a random walk randomly visits the next node according to the transition probabilities from the
    // node to all its adjacency nodes. The transition probabilies from a node to all its adjaceny node are summed to 100%.
    // For example, a random walk sequence is the following node sequence: n2, n3, n4, n6, n1, n2, n10.
    // node n2 is the starting node. The next node to be visited is mainly determined by the transition probabilites of n2 to all its adjacency nodes.
    // The larger the transition probability to an adjacency node is, the more likely the adjacency node is chosen as the next node.
    // Here n3 is the next node that is randomly chosen out of the adjacency nodes of n2.
    // n3 then becomes the starting node and the random visit of a next node repeats.
    // The length of a random walk sequence is larger than 1.
    public ArrayList<Node> getSequence() {
        return this.sequence;
    }

    public void setSequence(ArrayList<Node> sequence) {
         this.sequence = sequence;
    }

    //Task 3: Given another random walk sequence o, return a set of nodes that are shared between this and o.
    public HashSet<Node> nodeOverlapping(RandomWalkSequence o){
        HashSet <Node> overlapNode = new HashSet<Node>();
        for (Node node: getSequence()){
            if (sequence.contains(node))
                overlapNode.add(node);
        }
        return overlapNode;

    }



    // Task 4: Override equals method so that, for each pair of sequences s1 and s2 (s1 != null && s2 != null),
    // they are equal if and only if the same set of nodes are visited in the two random walk sequences
    // and the frequency of the visit of each node is the same.
    public boolean equals(Object o) {
        if (this == o) //same random walk sequences
            return true;
        if ( o == null || getClass()!= o.getClass()) //null or differenct classes
            return false;
        if(this.sequence.size()
                != ((RandomWalkSequence) o).getSequence().size()){ //different size
            return false;
        }

        for(Node node: this.sequence){
            ArrayList<Node> list = new ArrayList<>();
            list = ((RandomWalkSequence) o).getSequence();
            if(list.contains(node))  // does not contain node
                return false;
            return true;
        }
        return false;

    }


}
