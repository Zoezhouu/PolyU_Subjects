package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.*;

public class Scanning {
    private int line = 1;

    private final typeMap types = new typeMap();
    private final KeywordsMap keywords = new KeywordsMap();
    private final operatorMap operators = new operatorMap();

    public List<IndividualToken> parseToTokens(String input){ //return an ArrayList containing individual tokens
        List<IndividualToken> tokenList = new ArrayList<IndividualToken>();
        scanToken(input,tokenList);
        line++;
        return tokenList;
    }

    private void scanToken(String input,List<IndividualToken> tokenList){

        String[] splitInput = input.split(" ");
        for(int i = 0; i < splitInput.length;i++){
            if(keywords.getFromMap(splitInput[i]) != null){    //add keywords
                addToken(keywords.getFromMap(splitInput[i]),splitInput[i],tokenList);
            }
            else if(types.getFromMap(splitInput[i]) != null){                                         //add types
                addToken(types.getFromMap(splitInput[i]),splitInput[i],tokenList);
            }
            else if(operators.getFromMap(splitInput[i]) != null)
                addToken(operators.getFromMap(splitInput[i]),splitInput[i],tokenList);
            else if(isNumeric(splitInput[i])){
                addNumeric(splitInput[i],tokenList);
            }
            else if(splitInput[i].equals("true") || splitInput[i].equals("TRUE")) {
                addBoolean(splitInput[i],tokenList);
            }
            else if(splitInput[i].equals("false") || splitInput[i].equals("FALSE")){
                addBoolean(splitInput[i],tokenList);
            }
            else{
                addToken(Tokens.IDENTIFIER,splitInput[i],tokenList);
            }
        }

    }


    private boolean isNumeric(String c){
        try{
            Integer.parseInt(c);
        }catch (NumberFormatException e){
            return false;
        }
        return true;
    }
    private void addToken(Tokens type, Object literal, String inputString,List<IndividualToken> tokenList){         //deal with string input other than keywords and identifier
        tokenList.add(new IndividualToken(type,inputString,literal,line));
    }

    private void addNumeric(String c,List<IndividualToken> tokenList){
        if(isNumeric(c)){
            addToken(Tokens.INTVALUE,Integer.parseInt(c),c,tokenList);
        }
    }

    private void addBoolean(String c,List<IndividualToken> tokenList){
        if(c.equals("true")){
            addToken(Tokens.BOOLVALUE,true,"true",tokenList);
        }
        if(c.equals("false")){
            addToken(Tokens.BOOLVALUE,false,"false",tokenList);
        }
    }

    private void addToken(Tokens type, String inputString,List<IndividualToken> tokenList){
        addToken(type,null,inputString,tokenList);
    }
}
