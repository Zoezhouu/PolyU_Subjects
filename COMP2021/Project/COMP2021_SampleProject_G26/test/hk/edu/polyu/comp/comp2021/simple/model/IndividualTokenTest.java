package hk.edu.polyu.comp.comp2021.simple.model;

import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class IndividualTokenTest {
    @Test
    public void testEquals1(){
        IndividualToken token1 = new IndividualToken(Tokens.IDENTIFIER,"x",null,1);
        IndividualToken token2 = new IndividualToken(Tokens.IDENTIFIER,"y",null,1);
        assertFalse(token1.equals(token2));
    }

    @Test
    public void testEquals2(){
        IndividualToken token1 = new IndividualToken(Tokens.IDENTIFIER,"x",null,1);
        int x = 10;
        assertFalse(token1.equals(x));
    }

    @Test
    public void testToString(){
        IndividualToken token1 = new IndividualToken(Tokens.IDENTIFIER,"x",null,1);
        assertEquals("x",token1.toSting());
    }


}