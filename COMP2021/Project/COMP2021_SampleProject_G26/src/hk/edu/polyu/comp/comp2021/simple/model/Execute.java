package hk.edu.polyu.comp.comp2021.simple.model;


import java.util.ArrayList;
import java.util.List;

public class Execute {

    public void executeProgram(String programName, Program newProgram){
        Tokens exeStatement;
        int size = 0;
        List<String> statements = newProgram.setProgramExpression(programName);
        for(int i = 0; i < statements.size(); i++){
            if(!newProgram.getProgramExpressions().containsExpr(statements.get(i))){
                Error.checkInvalidExpr();
            }else{
                int line = newProgram.getProgramExpressions().getContents(statements.get(i)).get(0).getLine();
                exeStatement = newProgram.getProgramExpressions().getContents(statements.get(i)).get(0).getType();
                switch (exeStatement) {
                    case BLOCK:
                        if (i + 1 < statements.size()) {
                            statements.addAll(i + 1, newProgram.getBlock().getBasicMethods(newProgram.getProgramExpressions(), statements.get(i)));
                        } else {
                            statements.addAll(newProgram.setProgramExpression(statements.get(i)));
                        }
                        break;
                    case VARDEF: //done
                        newProgram.getInterpreter().runVardef(newProgram.getProgramExpressions().getContents(statements.get(i)), newProgram.getProgramVariables(), newProgram.getProgramExpressions());
                        break;
                    case BINEXPR:
                        size = CheckExpression.checkBothSides(newProgram.getProgramExpressions(), statements.get(i)).size();
                        if (i >= size) {
                            if (!statements.subList(i - size, i).equals(CheckExpression.checkBothSides(newProgram.getProgramExpressions(), statements.get(i)))) {
                                statements.addAll(i, CheckExpression.checkBothSides(newProgram.getProgramExpressions(), statements.get(i)));
                            }
                        }
                        newProgram.getInterpreter().runBinexpr(newProgram.getProgramExpressions().getContents(statements.get(i)), newProgram.getProgramVariables());
                        break;
                    case UNEXPR:
                        size = CheckExpression.checkOneSide(newProgram.getProgramExpressions(), statements.get(i)).size();
                        if (i >= size) {
                            if (!statements.subList(i - size, i).equals(CheckExpression.checkOneSide(newProgram.getProgramExpressions(), statements.get(i)))) {
                                statements.addAll(i, CheckExpression.checkOneSide(newProgram.getProgramExpressions(), statements.get(i)));
                            }
                        }
                        newProgram.getInterpreter().runUnexpr(newProgram.getProgramExpressions().getContents(statements.get(i)), newProgram.getProgramVariables());
                        break;
                    case ASSIGN:
                        size = CheckExpression.checkOneSide(newProgram.getProgramExpressions(), statements.get(i)).size();
                        if (!statements.subList(i - size, i).equals(CheckExpression.checkOneSide(newProgram.getProgramExpressions(), statements.get(i)))) {
                            statements.addAll(i, CheckExpression.checkOneSide(newProgram.getProgramExpressions(), statements.get(i)));
                            if (newProgram.getProgramExpressions().getContents(statements.get(i)).get(0).getType() == Tokens.BINEXPR) {
                                newProgram.getInterpreter().runBinexpr(newProgram.getProgramExpressions().getContents(statements.get(i)), newProgram.getProgramVariables());
                                break;
                            } else if (newProgram.getProgramExpressions().getContents(statements.get(i)).get(0).getType() == Tokens.UNEXPR) {
                                newProgram.getInterpreter().runUnexpr(newProgram.getProgramExpressions().getContents(statements.get(i)), newProgram.getProgramVariables());
                                break;
                            }
                        }
                        newProgram.getInterpreter().runAssign(newProgram.getProgramExpressions().getContents(statements.get(i)), newProgram.getProgramVariables());
                        break;
                    case PRINT:
                        newProgram.getInterpreter().runPrint(newProgram.getProgramExpressions().getContents(statements.get(i)), newProgram.getProgramVariables());
                        break;
                    case SKIP:
                        break;
                    case WHILE:
                        statements.addAll(newProgram.getMyWhile().getExecuteOrder(newProgram.getProgramExpressions(), newProgram.getProgramVariables(), statements.get(i)));
                        break;
                    case IF:
                        if (newProgram.getProgramExpressions().getContents(statements.get(i)).get(2).getInputString().equals(statements.get(i - 1))) {
                            statements.addAll(i + 1, newProgram.getMyIf().checkConditions(newProgram.getProgramExpressions(), newProgram.getProgramVariables(), statements.get(i)));
                        } else {
                            statements.addAll(i, newProgram.getMyIf().getExecuteOrder(newProgram.getProgramExpressions(), newProgram.getProgramVariables(), statements.get(i)));
                            i--;
                        }
                        break;
                    default:
                        Error.checkInvalidOperations(line);
                }
            }
        }
    }

    public List<String> outputExecutionOrder(String programName, Program newProgram){
        Tokens statementType;
        List<String> statements = newProgram.setProgramExpression(programName);
        List<String> temp = new ArrayList<>();
        statements.add(0,programName);
        statements.add(1,newProgram.getProgramExpressions().getContents(programName).get(2).getInputString());
        for(int i = 2; i < statements.size(); i++){
            if(!newProgram.getProgramExpressions().containsExpr(statements.get(i))){
                Error.checkInvalidExpr();
            }
            else {
                int line = newProgram.getProgramExpressions().getContents(statements.get(i)).get(0).getLine();
                statementType = newProgram.getProgramExpressions().getContents(statements.get(i)).get(0).getType();
                switch (statementType) {
                    case BLOCK:
                        //statements.add(i,statements.get(i));
                        statements.addAll(newProgram.getBlock().getBasicMethods(newProgram.getProgramExpressions(), statements.get(i)));
                    case VARDEF: //done
                        break;
                    case BINEXPR:
                        temp = CheckExpression.checkBothSides(newProgram.getProgramExpressions(), statements.get(i));
                        statements.addAll(temp);
                        break;
                    case UNEXPR:
                    case ASSIGN:
                        temp = CheckExpression.checkOneSide(newProgram.getProgramExpressions(), statements.get(i));
                        statements.addAll(temp);
                        break;
                    case PRINT:
                    case SKIP:
                        break;
                    case WHILE:
                        String whileCondition = newProgram.getProgramExpressions().getContents(statements.get(i)).get(2).getInputString();
                        String whileBody = newProgram.getProgramExpressions().getContents(statements.get(i)).get(3).getInputString();
                        if (newProgram.getProgramExpressions().containsExpr(whileCondition)) {
                            statements.add(whileCondition);
                        }
                        if (newProgram.getProgramExpressions().containsExpr(whileBody)) {
                            statements.add(whileBody);
                        }
                        break;
                    case IF:
                        String ifCondition = newProgram.getProgramExpressions().getContents(statements.get(i)).get(2).getInputString();
                        String trueBody = newProgram.getProgramExpressions().getContents(statements.get(i)).get(3).getInputString();
                        String falseBody = newProgram.getProgramExpressions().getContents(statements.get(i)).get(4).getInputString();
                        if (newProgram.getProgramExpressions().containsExpr(trueBody)) {
                            statements.add(trueBody);
                        }
                        if (newProgram.getProgramExpressions().containsExpr(falseBody)) {
                            statements.add(falseBody);
                        }
                        if (newProgram.getProgramExpressions().containsExpr(ifCondition)) {
                            statements.add(ifCondition);
                        }
                        break;
                    default:
                        Error.checkInvalidOperations(line);
                }
            }
        }
        return statements;
    }
}
