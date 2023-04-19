package hk.edu.polyu.comp.comp2021.simple.model;

import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class typeMapTest {
    @Test
    public void typeMapTest(){
        typeMap keywords = new typeMap();
        assertEquals(Tokens.BOOL,keywords.getFromMap("bool"));
        assertEquals(Tokens.INT,keywords.getFromMap("int"));
    }
}