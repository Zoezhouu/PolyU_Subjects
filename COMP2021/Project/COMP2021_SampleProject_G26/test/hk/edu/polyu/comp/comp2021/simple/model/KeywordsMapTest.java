package hk.edu.polyu.comp.comp2021.simple.model;

import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class KeywordsMapTest {
    @Test
    public void keywordsMapTest(){
        KeywordsMap keywords = new KeywordsMap();
        assertEquals(Tokens.VARDEF,keywords.getFromMap("vardef"));
        assertEquals(Tokens.BINEXPR,keywords.getFromMap("binexpr"));
    }
}