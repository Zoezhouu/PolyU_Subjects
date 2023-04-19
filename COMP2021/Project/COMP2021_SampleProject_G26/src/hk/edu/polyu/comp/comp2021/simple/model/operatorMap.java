package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.HashMap;

public class operatorMap implements HashMaps{
    private static final HashMap<String,Tokens> operatorType = new HashMap<String, Tokens>();
    static{
        //+-*/#~> < >= <= == != && || !
        operatorType.put("+",Tokens.PLUS);
        operatorType.put("-",Tokens.MINUS);
        operatorType.put("*",Tokens.MULTIPLY);
        operatorType.put("/",Tokens.DIVISION);
        operatorType.put("#",Tokens.SIGNPLUS);
        operatorType.put("~",Tokens.NEGATION);
        operatorType.put(">",Tokens.GREATER);
        operatorType.put("<",Tokens.SMALLER);
        operatorType.put(">=",Tokens.GREATER_EQUAL);
        operatorType.put("<=",Tokens.SMALLER_EQUAL);
        operatorType.put("==",Tokens.EQUAL);
        operatorType.put("!=",Tokens.NOT_EQUAL);
        operatorType.put("&&",Tokens.AND);
        operatorType.put("||",Tokens.OR);
        operatorType.put("!",Tokens.NOT);
        operatorType.put("%",Tokens.MODULO);
    }

    @Override
    public Tokens getFromMap(String key) {
        return operatorType.get(key);
    }
}
