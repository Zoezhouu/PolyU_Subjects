package hk.edu.polyu.comp.comp2021.simple.model;

import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class ScanningTest {
    @Test
    public void parseToTokenTest1(){
        Scanning testScanner = new Scanning();
        String input1 = "vardef def1 int x 10";
        //String input2 = "binexpr expr1 y + z";
        //String input3 = "block block1 def1 expr1 expr3";
        List<IndividualToken> testingList = new ArrayList<>();
        testingList.add(new IndividualToken(Tokens.VARDEF,"vardef",null,1));
        testingList.add(new IndividualToken(Tokens.IDENTIFIER,"def1",null,1));
        testingList.add(new IndividualToken(Tokens.INT,"int",null,1));
        testingList.add(new IndividualToken(Tokens.IDENTIFIER,"x",null,1));
        testingList.add(new IndividualToken(Tokens.INTVALUE,"10",10,1));
        List<IndividualToken> outputList = testScanner.parseToTokens(input1);
        assertTrue(outputList.get(0).equals(testingList.get(0)));
        assertTrue(outputList.get(1).equals(testingList.get(1)));
        assertTrue(outputList.get(2).equals(testingList.get(2)));
        assertTrue(outputList.get(3).equals(testingList.get(3)));
        assertTrue(outputList.get(4).equals(testingList.get(4)));
    }

    @Test
    public void parseToTokenTest2(){
        Scanning testScanner = new Scanning();
        String input1 = "block vardef def1 expr1 expr3";
        List<IndividualToken> testingList = new ArrayList<>();
        testingList.add(new IndividualToken(Tokens.BLOCK,"block",null,1));
        testingList.add(new IndividualToken(Tokens.VARDEF,"vardef",null,1));
        testingList.add(new IndividualToken(Tokens.IDENTIFIER,"def1",null,1));
        testingList.add(new IndividualToken(Tokens.IDENTIFIER,"expr1",null,1));
        testingList.add(new IndividualToken(Tokens.IDENTIFIER,"expr3",null,1));
        List<IndividualToken> outputList = testScanner.parseToTokens(input1);
        assertTrue(outputList.get(0).equals(testingList.get(0)));
        assertTrue(outputList.get(1).equals(testingList.get(1)));
        assertTrue(outputList.get(2).equals(testingList.get(2)));
        assertTrue(outputList.get(3).equals(testingList.get(3)));
        assertTrue(outputList.get(4).equals(testingList.get(4)));
    }

    @Test
    public void parseToTokensTest2(){
        Scanning testScanner = new Scanning();
        String input1 = "binexpr expr1 false && true";
        List<IndividualToken> testingList = new ArrayList<>();
        testingList.add(new IndividualToken(Tokens.BINEXPR,"binexpr",null,1));
        testingList.add(new IndividualToken(Tokens.IDENTIFIER,"expr1",null,1));
        testingList.add(new IndividualToken(Tokens.BOOLVALUE,"false",false,1));
        testingList.add(new IndividualToken(Tokens.AND,"&&",null,1));
        testingList.add(new IndividualToken(Tokens.BOOLVALUE,"true",true,1));
        List<IndividualToken> outputList = testScanner.parseToTokens(input1);
        assertTrue(outputList.get(0).equals(testingList.get(0)));
        assertTrue(outputList.get(1).equals(testingList.get(1)));
        assertTrue(outputList.get(2).equals(testingList.get(2)));
        assertTrue(outputList.get(3).equals(testingList.get(3)));
        assertTrue(outputList.get(4).equals(testingList.get(4)));
    }

}