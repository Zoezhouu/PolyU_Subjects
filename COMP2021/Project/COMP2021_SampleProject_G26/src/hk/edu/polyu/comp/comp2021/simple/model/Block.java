package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.ArrayList;
import java.util.List;

public class Block {

    public List<String> getBasicMethods(expressionMap expressions,String blockName){
        List<String> statements = new ArrayList<>();
        addToStatements(expressions,blockName,statements);
        return statements;
    }

    public void addToStatements(expressionMap expressions,String blockName, List<String> statements){
        for(int i = 2; i < expressions.getContents(blockName).size(); i++){
            statements.add(expressions.getContents(blockName).get(i).getInputString());
        }
    }
}
