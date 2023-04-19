package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.ArrayList;
import java.util.List;

public class While {


//    //public While(expressionMap conditionExpr, variableMaps conditionVar) {
//        super(conditionExpr, conditionVar);
//    }

    //Runner conditionRunner = new Runner(conditionExpr,conditionVar);


    public List<String> sendConditions(expressionMap programExpressions, variableMaps variables, IndividualToken condition){
        List<String> conditions = new ArrayList<>();
        conditions.add(condition.getInputString());
        return conditions;
    }

    public List<String> getExecuteOrder(expressionMap programExpressions, variableMaps variables, String programBody) {
        IndividualToken conditions = programExpressions.getContents(programBody).get(2);
        IndividualToken body = programExpressions.getContents(programBody).get(3);
        Tokens bodyType = programExpressions.getContents(body.getInputString()).get(0).getType();
        List<String> bodyStmt = new ArrayList<>();
        checkConditions(programExpressions,variables,conditions,bodyStmt,body.getInputString(),programBody);
        return bodyStmt;
    }

    public void checkConditions(expressionMap programExpressions, variableMaps variables, IndividualToken condition, List<String> bodyStatement, String bodyName, String programName) {
        Tokens condiType = condition.getType();
        switch (condiType){
            case INTVALUE:
                int value = (int)condition.getVariable();
                if(value > 0){
                    bodyStatement.add(bodyName);
                    bodyStatement.add(programName);
                }
                break;
            case BOOLVALUE:
                if((boolean) condition.getVariable()){
                    bodyStatement.add(bodyName);
                    bodyStatement.add(programName);
                }
                break;
            case IDENTIFIER:
                if(variables.definedBoolContains(condition.getInputString())){
                    if(variables.getFromDefinedBool(condition.getInputString())){
                        bodyStatement.add(bodyName);
                        bodyStatement.add(programName);
                    }
                }
                else if(variables.definedIntContains(condition.getInputString())){
                    if(variables.getFromDefinedInt(condition.getInputString()) > 0){
                        bodyStatement.add(bodyName);
                        bodyStatement.add(programName);
                    }
                }
                else if(programExpressions.containsExpr(condition.getInputString())) {
                    //sendConditions(programExpressions,variables,condition);
                    if(variables.tempBoolContains("temp" + condition.getInputString())){
                        if(variables.getFromTempBool("temp" + condition.getInputString())){
                            bodyStatement.add(condition.getInputString());
                            bodyStatement.add(bodyName);
                            bodyStatement.add(programName);
                        }
                    }
                    else{
                        bodyStatement.add(condition.getInputString());
                        bodyStatement.add(programName);
                    }
                }
                else {
                    System.out.println("report expression not defined here");
                }
        }
    }
}
