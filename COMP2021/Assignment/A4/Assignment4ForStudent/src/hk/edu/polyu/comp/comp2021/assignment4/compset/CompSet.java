package hk.edu.polyu.comp.comp2021.assignment4.compset;

import java.util.ArrayList;
import java.util.List;

class CompSet<T> {

    /** Each CompSet uses at most 1023 buckets.   */
    private static final int NUBMER_OF_BUCKETS = 1023;

    /** An array of buckets as the storage for each set. */
    private final List<T>[] storage;

    public CompSet() {
        storage = new List[NUBMER_OF_BUCKETS];
    }

    /**
     * Initialize 'this' with the unique elements from 'elements'.
     * Throw IllegalArgumentException if 'elements' is null.
     */
    public CompSet(List<T> elements) {
        // Add missing code here
        storage = new List[NUBMER_OF_BUCKETS];
        if (elements == null)
            throw new IllegalArgumentException();


        for(int i = 0; i < this.storage.length; i++){
            this.storage[i] = new ArrayList<>();
        }

        for (T element: elements){
            this.add(element);
        }


    }

    /**
     * Get the total number of elements stored in 'this'.
     */
    public int getCount() {
        // Add missing code here
        int count = 0;
        for (int i = 0; i < storage.length; i++){
            if(this.isEmpty())
                return 0;
            if(!storage[i].isEmpty())
                count++;
        }
        return count;
    }

    public boolean isEmpty() {
        // Add missing code here
        if(this.storage[0] == null)
            return true;
        return false;
    }

    /**
     * Whether 'element' is contained in 'this'?
     */
    public boolean contains(T element) {
        // Add missing code here
        if(element == null){
            for(int i = 0; i < this.getCount(); i++){

                if (storage[i] == null)
                    return true;
                return false;
            }
        }
        for(int i = 0; i < this.getCount(); i++){
            if(element == null){
                if (storage[i] == null)
                    return true;
                return false;
            }
            if (element.equals(storage[i]))
                return true;
        }


        return storage[getIndex(element)].contains(element);
    }

    /**
     * Get all elements of 'this' as a list.
     */
    public List<T> getElements() {
        // Add missing code here
        List<T> temp = new ArrayList<>();
        for (int i = 0; i < NUBMER_OF_BUCKETS; i++){
            temp.addAll(storage[i]);
        }
        return temp;

    }

    /**
     * Add 'element' to 'this', if it is not contained in 'this' yet.
     * Throw IllegalArgumentException if 'element' is null.
     */
    public void add(T element) {
        // Add missing code here
        if (element == null)
            throw new IllegalArgumentException();

        if(!this.contains(element))
            storage[getIndex(element)].add(element);
    }

    /**
     * Two CompSets are equivalent is they contain the same elements.
     * The order of the elements inside each CompSet is irrelevant.
     */
    public boolean equals(Object other){
        // Add missing code here

        if(other instanceof CompSet)
            return(this.getElements().equals(((CompSet<T>) other).getElements()));
        return false;
    }

    /**
     * Remove 'element' from 'this', if it is contained in 'this'.
     * Throw IllegalArgumentException if 'element' is null.
     */
    public void remove (T element) {
        // Add missing code here
        if (element == null)
            throw new IllegalArgumentException();

        if(this.contains(element))
            storage[getIndex(element)].remove(element);

    }

    //========================================================================== private methods

    private int getIndex(T element) {
        return element.hashCode() % NUBMER_OF_BUCKETS;
    }

}


