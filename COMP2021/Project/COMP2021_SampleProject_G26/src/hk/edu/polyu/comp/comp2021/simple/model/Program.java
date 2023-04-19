package hk.edu.polyu.comp.comp2021.simple.model;

import javax.imageio.plugins.tiff.ExifInteroperabilityTagSet;
import java.util.ArrayList;
import java.util.List;

public class Program {
    private expressionMap programExpressions;
    private variableMaps programVariables = new variableMaps();
    private While myWhile;
    private If myIf;
    private Runner interpreter;
    private Block block;
    private String programName;



    public Program(expressionMap expressions,While myWhile, If myIf, Runner interpreter, Block block,String programName){

        setProgramExpressions(expressions);
        setBlock(block);
        setInterpreter(interpreter);
        setMyIf(myIf);
        setMyWhile(myWhile);
        setProgramName(programName);
    }
    //private Block block = new Block();

    public List<String> setProgramExpression(String programName){
        List<String> statements = new ArrayList<>();
        if(programExpressions.containsExpr(programName)) {
            String programBody = programExpressions.getContents(programName).get(2).getInputString();
            int line = programExpressions.getContents(programName).get(0).getLine();
            statements.add(programBody);
            for(int i = 0; i < statements.size();i++){
                if(!programExpressions.containsExpr(statements.get(i))){
                    Error.checkExpressionNotDefinedError(line);
                }
                else{
                    Tokens bodyType = programExpressions.getContents(statements.get(i)).get(0).getType();
                    switch (bodyType) {
                        case BLOCK:
                            statements.remove(i);
                            statements.addAll(getBlock().getBasicMethods(programExpressions, programBody));
                            return statements;
                        case WHILE:
                            statements.remove(i);
                            statements.addAll(getMyWhile().getExecuteOrder(programExpressions, programVariables, programBody));
                            return statements;
                        case IF:
                            statements.remove(i);
                            statements.addAll(getMyIf().getExecuteOrder(programExpressions, programVariables, programBody));
                            return statements;
                        case BINEXPR:
                            statements.remove(i);
                            statements.addAll(CheckExpression.checkBothSides(programExpressions, programBody));
                            statements.add(programBody);
                            return statements;
                        case VARDEF:
                        case ASSIGN:
                        case UNEXPR:
                            statements.addAll(CheckExpression.checkOneSide(programExpressions, programBody));
                            return statements;
                        case PRINT:
                        case SKIP:
                            return statements;
                        default:
                            Error.checkInvalidOperations(line);
                    }
                }
            }
        }
        else {
            Error.noDefinedProgram(programName);
        }
        return statements;
    }
//=====================================setter and getter methods==================================
    public Runner getInterpreter(){
        return interpreter;
    }

    public While getMyWhile(){
        return myWhile;
    }

    public If getMyIf() {
        return myIf;
    }

    public Block getBlock() {
        return block;
    }

    public expressionMap getProgramExpressions() {
        return programExpressions;
    }

    public String getProgramName() {
        return programName;
    }

    public variableMaps getProgramVariables() {
        return programVariables;
    }

    public void setBlock(Block block) {
        this.block = block;
    }
    public void setProgramExpressions(expressionMap programExpressions){
        this.programExpressions  = programExpressions;
    }

    public void setInterpreter(Runner interpreter) {
        this.interpreter = interpreter;
    }

    public void setMyIf(If myIf) {
        this.myIf = myIf;
    }

    public void setMyWhile(While myWhile) {
        this.myWhile = myWhile;
    }

    public void setProgramName(String programName) {
        this.programName = programName;
    }

    public void setProgramVariables(variableMaps programVariables) {
        this.programVariables = programVariables;
    }
}
