package hk.edu.polyu.comp.comp2021.simple.model;

import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class variableMapsTest {
    @Test
    public void testAddtoDefinedBool1(){
        variableMaps variables = new variableMaps();
        String name = "test";
        boolean value = true;
        variables.addToDefinedBool(name,value,1);
        variables.addToVariables(name);
        assertEquals(variables.getFromDefinedBool(name),value);
        assertTrue(variables.containsVariable(name));
    }

    @Test
    public void testAddtoDefinedBool2(){
        variableMaps variables = new variableMaps();
        String name = "test";
        boolean value = true;
        variables.addToDefinedBool(name,value,1);
        variables.addToVariables(name);
        try {
            variables.addToDefinedBool(name,value,1);
            variables.addToVariables(name);
        }catch (Error e){}
    }

    @Test
    public void testAddtoDefinedInt1(){
        variableMaps variables = new variableMaps();
        String name = "test";
        int value = 10;
        variables.addToDefinedInt(name,value,1);
        variables.addToVariables(name);
        assertEquals(variables.getFromDefinedInt(name),value);
        assertTrue(variables.containsVariable(name));
    }

    @Test
    public void testAddtoDefinedInt2(){
        variableMaps variables = new variableMaps();
        String name = "test";
        int value = 10;
        variables.addToDefinedInt(name,value,1);
        variables.addToVariables(name);
        try {
            variables.addToDefinedInt(name,value,1);
            variables.addToVariables(name);
        }catch (Error e){}
    }

    @Test
    public void testAddtoTempBool1(){
        variableMaps variables = new variableMaps();
        String name = "test";
        boolean value = true;
        variables.addToDefinedBool(name,value,1);
        variables.addToVariables(name);
        assertEquals(variables.getFromDefinedBool(name),value);
        assertTrue(variables.containsVariable(name));
    }

}