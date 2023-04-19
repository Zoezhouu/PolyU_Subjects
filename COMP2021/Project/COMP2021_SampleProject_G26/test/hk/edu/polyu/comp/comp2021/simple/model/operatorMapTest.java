package hk.edu.polyu.comp.comp2021.simple.model;

import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class operatorMapTest {
    @Test
    public void operatorMapTest(){
        operatorMap operators = new operatorMap();
        assertEquals(Tokens.PLUS,operators.getFromMap("+"));
        assertEquals(Tokens.DIVISION,operators.getFromMap("/"));
    }
}