package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.HashMap;

public class typeMap implements HashMaps{
    private static final HashMap<String,Tokens> variableType = new HashMap<String,Tokens>();
    static{
        variableType.put("int",Tokens.INT);
        variableType.put("bool", Tokens.BOOL);
    }


    @Override
    public Tokens getFromMap(String key) {
        return variableType.get(key);
    }

}

