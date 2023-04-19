package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class variableMaps{
    private final Map<String, Boolean> definedBool = new HashMap<>();
    private final Map<String,Integer> definedInt = new HashMap<>();
    private final HashSet<String> variables = new HashSet<String>();
    private final Map<String,Boolean> tempBool = new HashMap<>();
    private final Map<String,Integer> tempInt = new HashMap<>();

    public void addToDefinedBool(String varName, Boolean value, int line) {  //defining variable
        if(definedBool.containsKey(varName)){
            Error.checkVarAlreadyDefinedError(line);
        }
        definedBool.put(varName,value);
    }
    public void updateDefinedBool(String varName, Boolean value, int line){ //updating variable
        if(!definedBool.containsKey(varName)){
            Error.checkExpressionNotDefinedError(line);
        }
        definedBool.put(varName,value);
    }

    public void addToDefinedInt(String varName, Integer value, int line) {
        if(definedInt.containsKey(varName)){
            Error.checkVarAlreadyDefinedError(line);
        }
        definedInt.put(varName,value);
    }

    public void updateDefinedInt(String varName, Integer value, int line){
        if(!definedInt.containsKey(varName)){
            Error.checkExpressionNotDefinedError(line);
        }
        definedInt.put(varName,value);
    }




    public void addToVariables(String varName){
        variables.add(varName);
    }
    public void addToTempBool(String name,Boolean value){
        tempBool.put(name,value);
    }
    public void addToTempInt(String name, Integer value) {
        tempInt.put(name,value);
    }
    public boolean containsVariable(String varName){
        return variables.contains(varName);
    }

    public Boolean getFromTempBool(String name){
        return tempBool.get(name);
    }
    public Integer getFromTempInt(String name){
        return tempInt.get(name);
    }

    public Boolean getFromDefinedBool(String name){
        return definedBool.get(name);
    }
    public Integer getFromDefinedInt(String name){
        return definedInt.get(name);
    }

    public boolean tempBoolContains(String name){
        return tempBool.containsKey(name);
    }

    public boolean tempIntContains(String name){
        return tempInt.containsKey(name);
    }

    public boolean definedBoolContains(String name){
        return definedBool.containsKey(name);
    }

    public boolean definedIntContains(String name){
        return definedInt.containsKey(name);
    }

}

