package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.ArrayList;
import java.util.List;

public class If {

    public List<String> sendConditions(String condition){
        List<String> conditions = new ArrayList<>();
        conditions.add(condition);
        return conditions;
    }

    public List<String> getExecuteOrder(expressionMap programExpressions, variableMaps variables, String programBody) {
        IndividualToken conditions = programExpressions.getContents(programBody).get(2);
        IndividualToken body1 = programExpressions.getContents(programBody).get(3);
        IndividualToken body2 = programExpressions.getContents(programBody).get(4);
        List<String> bodyStmt = new ArrayList<>();
        bodyStmt.add(conditions.getInputString());
        Tokens condiType = conditions.getType();
        switch (condiType) {
            case INTVALUE:
                int value = (int) conditions.getVariable();
                if (value > 0) {
                    bodyStmt.add(body1.getInputString());
                } else {
                    bodyStmt.add(body2.getInputString());
                }
                break;
            case BOOLVALUE:
                if ((boolean) conditions.getVariable()) {
                    bodyStmt.add(body1.getInputString());
                } else {
                    bodyStmt.add(body2.getInputString());
                }
                break;
            case IDENTIFIER:
                if(variables.definedBoolContains(conditions.getInputString())){
                    if(variables.getFromDefinedBool(conditions.getInputString())){
                        bodyStmt.add(body1.getInputString());
                    }
                    else {
                        bodyStmt.add(body2.getInputString());
                    }
                }
                else if(variables.definedIntContains(conditions.getInputString())){
                    if(variables.getFromDefinedInt(conditions.getInputString()) > 0){
                        bodyStmt.add(body1.getInputString());
                    }
                    else {
                        bodyStmt.add(body2.getInputString());
                    }
                }
                else if(programExpressions.containsExpr(conditions.getInputString())) {
                    bodyStmt = sendConditions(conditions.getInputString());
                }
                break;
        }
        return bodyStmt;
    }


    public List<String> checkConditions(expressionMap programExpressions,variableMaps variables,String programName) {
        int line = programExpressions.getContents(programName).get(0).getLine();
        String condition = programExpressions.getContents(programName).get(2).getInputString();
        String trueBody = programExpressions.getContents(programName).get(3).getInputString();
        String falseBody = programExpressions.getContents(programName).get(4).getInputString();
        List<String> bodyStatement = new ArrayList<>();
        if (variables.tempBoolContains("temp" + condition)) {
            if (variables.getFromTempBool("temp" + condition)) {
                bodyStatement.add(trueBody);
            }
            else {
                bodyStatement.add(falseBody);
            }
        }
        else {
            Error.checkExpressionNotDefinedError(line);
        }

        return bodyStatement;
    }

}
