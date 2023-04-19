package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.ArrayList;
import java.util.List;


public class CheckExpression {
    public static List<String> checkBothSides(expressionMap expressions, String binaryExpr){
        List<String> statements = new ArrayList<>();
        IndividualToken leftSide,rightSide;
        List<IndividualToken> oriBinary = expressions.getContents(binaryExpr);
        if(expressions.containsExpr(oriBinary.get(2).getInputString())){
            leftSide = expressions.getContents(oriBinary.get(2).getInputString()).get(0);
            if(leftSide.getType() == Tokens.BINEXPR){
                statements.add(oriBinary.get(2).getInputString());
            }
            else if(leftSide.getType() == Tokens.UNEXPR){
                statements.add(oriBinary.get(2).getInputString());

            }
        }
        if(expressions.containsExpr(oriBinary.get(4).getInputString())){
            rightSide = expressions.getContents(oriBinary.get(4).getInputString()).get(0);
            if(rightSide.getType() == Tokens.BINEXPR){
                statements.add(oriBinary.get(4).getInputString());

            }
            else if(rightSide.getType() == Tokens.UNEXPR){
                statements.add(oriBinary.get(4).getInputString());

            }
        }
        return statements;
    }

    public static List<String> checkOneSide(expressionMap expressions, String binaryExpr){
        List<String> statements = new ArrayList<>();
        List<IndividualToken> oriBinary = expressions.getContents(binaryExpr);
        IndividualToken rightSide;
        if(expressions.containsExpr(oriBinary.get(3).getInputString())){
            rightSide = expressions.getContents(oriBinary.get(3).getInputString()).get(0);
            if(rightSide.getType() == Tokens.BINEXPR){
                statements.add(oriBinary.get(3).getInputString());
            }
            else if(rightSide.getType() == Tokens.UNEXPR){
                statements.add(oriBinary.get(3).getInputString());
            }
        }
        return statements;
    }

}
