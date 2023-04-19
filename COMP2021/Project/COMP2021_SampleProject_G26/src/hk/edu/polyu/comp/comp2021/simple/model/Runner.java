package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.*;



public class Runner {

    private final int POSITIVE_MAX = 99999;
    private final int NEGATIVE_MAX = -99999;
    private final int ABNORMAL = -100000;
    public void runBinexpr(List<IndividualToken> tokenList, variableMaps definedVar) {
        if(tokenList.size() == 5) {
            int line = tokenList.get(0).getLine();
            int numResult = 0;
            boolean boolResult = false;
            IndividualToken operand1, operand2;
            Tokens operator;
            operand1 = tokenList.get(2);
            operand2 = tokenList.get(4);
            operator = tokenList.get(3).getType();
            String exprName = tokenList.get(1).getInputString();
            switch (operator) {
                case PLUS:
                    //two numbers
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {       //all int values
                        numResult = rounding((int) operand1.getVariable() + (int) operand2.getVariable());
                        definedVar.addToTempInt("temp" + exprName, numResult);
                    }
                    //two variables or two expressions
                    else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            numResult = var1 + var2;
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            numResult = rounding(var1 + (int) operand2.getVariable());
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            numResult = rounding((int) operand1.getVariable() + var2);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case MINUS:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        numResult = rounding((int) operand1.getVariable() - (int) operand2.getVariable());
                        definedVar.addToTempInt("temp" + exprName, numResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            numResult = var1 - var2;
                            numResult = rounding(numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            numResult = var1 - (int) operand2.getVariable();
                            numResult = rounding(numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            numResult = (int) operand1.getVariable() - var2;
                            numResult = rounding(numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                //else
                case MULTIPLY:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        numResult = (int) operand1.getVariable() * (int) operand2.getVariable();
                        numResult = rounding(numResult);
                        definedVar.addToTempInt("temp" + exprName, numResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            numResult = var1 * var2;
                            numResult = rounding(numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            numResult = var1 * (int) operand2.getVariable();
                            numResult = rounding(numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            numResult = (int) operand1.getVariable() * var2;
                            numResult = rounding(numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                //else
                case DIVISION:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        if ((int) operand2.getVariable() != 0) {
                            numResult = (int) operand1.getVariable() / (int) operand2.getVariable();
                            numResult = rounding(numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        } else {
                            Error.checkDivisionByZero(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            if (var2 != 0) {
                                numResult = var1 / var2;
                                numResult = rounding(numResult);
                                definedVar.addToTempInt("temp" + exprName, numResult);
                            } else {
                                Error.checkDivisionByZero(line);
                            }
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            if ((int) operand2.getVariable() != 0) {
                                numResult = var1 / (int) operand2.getVariable();
                                numResult = rounding(numResult);
                                definedVar.addToTempInt("temp" + exprName, numResult);
                            } else {
                                Error.checkDivisionByZero(line);
                            }
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            if(var2 != 0) {
                                numResult = (int) operand1.getVariable() / var2;
                                numResult = rounding(numResult);
                                definedVar.addToTempInt("temp" + exprName, numResult);
                            }
                            else {
                                Error.checkDivisionByZero(line);
                            }
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case MODULO:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        if ((int) operand2.getVariable() != 0) {
                            numResult = (int) operand1.getVariable() % (int) operand2.getVariable();
                            numResult = rounding(numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                            break;
                        } else {
                            Error.checkDivisionByZero(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            if ((int) operand2.getVariable() != 0) {
                                numResult = var1 % (int) operand2.getVariable();
                                numResult = rounding(numResult);
                                definedVar.addToTempInt("temp" + exprName, numResult);
                            } else {
                                Error.checkDivisionByZero(line);
                            }
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            if(var2 != 0){
                                numResult = (int) operand1.getVariable() % var2;
                                numResult = rounding(numResult);
                                definedVar.addToTempInt("temp" + exprName, numResult);
                            }
                            else {
                                Error.checkDivisionByZero(line);
                            }
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case GREATER:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        boolResult = (int) operand1.getVariable() > (int) operand2.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            boolResult = var1 > var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            boolResult = var1 > (int) operand2.getVariable();
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            boolResult = (int) operand1.getVariable() > var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case SMALLER:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        boolResult = (int) operand1.getVariable() < (int) operand2.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            boolResult = var1 < var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            boolResult = var1 < (int) operand2.getVariable();
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            boolResult = (int) operand1.getVariable() < var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkExpressionNotDefinedError(line);
                    }
                    break;
                case GREATER_EQUAL:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        boolResult = (int) operand1.getVariable() >= (int) operand2.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            boolResult = var1 >= var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            boolResult = var1 >= (int) operand2.getVariable();
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            boolResult = (int) operand1.getVariable() >= var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case SMALLER_EQUAL:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        boolResult = (int) operand1.getVariable() <= (int) operand2.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            boolResult = var1 <= var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            boolResult = var1 <= (int) operand2.getVariable();
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            boolResult = (int) operand1.getVariable() <= var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                //else
                case EQUAL:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        boolResult = (int) operand1.getVariable() == (int) operand2.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            boolResult = var1 == var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            boolResult = var1 == (int) operand2.getVariable();
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            boolResult = (int) operand1.getVariable() == var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case NOT_EQUAL:
                    if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.INTVALUE) {
                        boolResult = (int) operand1.getVariable() != (int) operand2.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        int var2 = specialBinUnInt(operand2.getInputString(), definedVar);
                        if (var1 != ABNORMAL && var2 != ABNORMAL) {
                            boolResult = var1 != var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.INTVALUE) {
                        int var1 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var1 != ABNORMAL) {
                            boolResult = var1 != (int) operand2.getVariable();
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.INTVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        int var2 = specialBinUnInt(operand1.getInputString(), definedVar);
                        if (var2 != ABNORMAL) {
                            boolResult = (int) operand1.getVariable() != var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case AND:
                    if (operand1.getType() == Tokens.BOOLVALUE && operand2.getType() == Tokens.BOOLVALUE) {
                        boolResult = (boolean) operand1.getVariable() && (boolean) operand2.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        boolean var1;
                        boolean var2;
                        if (definedVar.containsVariable(operand1.getInputString()) && definedVar.containsVariable(operand2.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand1.getInputString());
                            var2 = definedVar.getFromDefinedBool(operand2.getInputString());
                            boolResult = var1 && var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.containsVariable(operand1.getInputString()) && definedVar.tempBoolContains("temp" + operand2.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand1.getInputString());
                            var2 = definedVar.getFromTempBool("temp" + operand2.getInputString());
                            boolResult = var1 && var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.containsVariable(operand2.getInputString()) && definedVar.tempBoolContains("temp" + operand1.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand2.getInputString());
                            var2 = definedVar.getFromTempBool("temp" + operand1.getInputString());
                            boolResult = var1 && var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.tempBoolContains("temp" + operand1.getInputString()) && definedVar.containsVariable("temp" + operand2.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand2.getInputString());
                            var2 = definedVar.getFromTempBool("temp" + operand1.getInputString());
                            boolResult = var1 && var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.BOOLVALUE) {
                        boolean var1;
                        if (definedVar.containsVariable(operand1.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand1.getInputString());
                            boolResult = (boolean) operand2.getVariable() && var1;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.tempBoolContains(operand1.getInputString())) {
                            var1 = definedVar.getFromTempBool(operand1.getInputString());
                            boolResult = (boolean) operand2.getVariable() && var1;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.BOOLVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        boolean var2;
                        if (definedVar.containsVariable(operand2.getInputString())) {
                            var2 = definedVar.getFromDefinedBool(operand2.getInputString());
                            boolResult = (boolean) operand1.getVariable() && var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        }
                        else if (definedVar.tempBoolContains(operand2.getInputString())) {
                            var2 = definedVar.getFromTempBool(operand2.getInputString());
                            boolResult = (boolean) operand1.getVariable() && var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        }
                        else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                //else
                case OR:
                    if (operand1.getType() == Tokens.BOOLVALUE && operand2.getType() == Tokens.BOOLVALUE) {
                        boolResult = (boolean) operand1.getVariable() || (boolean) operand2.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.IDENTIFIER) {
                        boolean var1;
                        boolean var2;
                        if (definedVar.containsVariable(operand1.getInputString()) && definedVar.containsVariable(operand2.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand1.getInputString());
                            var2 = definedVar.getFromDefinedBool(operand2.getInputString());
                            boolResult = var1 || var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.containsVariable(operand1.getInputString()) && definedVar.tempBoolContains("temp" + operand2.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand1.getInputString());
                            var2 = definedVar.getFromTempBool("temp" + operand2.getInputString());
                            boolResult = var1 || var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.containsVariable(operand2.getInputString()) && definedVar.tempBoolContains("temp" + operand1.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand2.getInputString());
                            var2 = definedVar.getFromTempBool("temp" + operand1.getInputString());
                            boolResult = var1 || var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.tempBoolContains("temp" + operand1.getInputString()) && definedVar.containsVariable("temp" + operand2.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand2.getInputString());
                            var2 = definedVar.getFromTempBool("temp" + operand1.getInputString());
                            boolResult = var1 || var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.IDENTIFIER && operand2.getType() == Tokens.BOOLVALUE) {
                        boolean var1;
                        if (definedVar.containsVariable(operand1.getInputString())) {
                            var1 = definedVar.getFromDefinedBool(operand1.getInputString());
                            boolResult = (boolean) operand1.getVariable() || var1;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.tempBoolContains(operand1.getInputString())) {
                            var1 = definedVar.getFromTempBool(operand1.getInputString());
                            boolResult = (boolean) operand1.getVariable() || var1;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    } else if (operand1.getType() == Tokens.BOOLVALUE && operand2.getType() == Tokens.IDENTIFIER) {
                        boolean var2;
                        if (definedVar.containsVariable(operand2.getInputString())) {
                            var2 = definedVar.getFromDefinedBool(operand2.getInputString());
                            boolResult = (boolean) operand1.getVariable() || var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.tempBoolContains(operand2.getInputString())) {
                            var2 = definedVar.getFromTempBool(operand2.getInputString());
                            boolResult = (boolean) operand1.getVariable() || var2;
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    }
                    else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                default:
                    Error.checkInvalidOperations(line);
            }
        }
        else {
            Error.checkInvalidExpr();
        }
    }
    public void runUnexpr(List<IndividualToken> tokenList,variableMaps definedVar){
        if(tokenList.size() == 4){
            int line = tokenList.get(0).getLine();
            IndividualToken operand;
            Tokens operator;
            operator = tokenList.get(2).getType();
            operand = tokenList.get(3);
            int numResult = 0;
            boolean boolResult = false;
            String exprName = tokenList.get(1).getInputString();
            switch (operator) {
                case NOT:
                    if (operand.getType() == Tokens.BOOLVALUE) {
                        boolResult = !(boolean) operand.getVariable();
                        definedVar.addToTempBool("temp" + exprName, boolResult);
                    } else if (operand.getType() == Tokens.IDENTIFIER) {
                        if (definedVar.containsVariable(operand.getInputString())) {
                            boolResult = !definedVar.getFromDefinedBool(operand.getInputString());
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        } else if (definedVar.tempIntContains("temp" + operand.getInputString())) {
                            boolResult = !definedVar.getFromTempBool("temp" + operand.getInputString());
                            definedVar.addToTempBool("temp" + exprName, boolResult);
                        }
                        else{
                            Error.checkExpressionNotDefinedError(line);
                        }
                    }
                    else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case SIGNPLUS:
                    if (operand.getType() == Tokens.INTVALUE) {
                        numResult = +(int) operand.getVariable();
                        numResult = rounding(numResult);
                        definedVar.addToTempInt("temp" + exprName, numResult);
                    } else if (operand.getType() == Tokens.IDENTIFIER) {
                        numResult = specialBinUnInt(operand.getInputString(), definedVar);
                        if(numResult != ABNORMAL){
                            numResult = rounding(+numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        }
                        else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    }
                    else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                case NEGATION:
                    if (operand.getType() == Tokens.INTVALUE) {
                        numResult = -(int) operand.getVariable();
                        numResult = rounding(numResult);
                        definedVar.addToTempInt("temp" + exprName, numResult);
                    } else if (operand.getType() == Tokens.IDENTIFIER) {
                        numResult = specialBinUnInt(operand.getInputString(), definedVar);
                        if(numResult != ABNORMAL){
                            numResult = rounding(-numResult);
                            definedVar.addToTempInt("temp" + exprName, numResult);
                        }
                        else {
                            Error.checkExpressionNotDefinedError(line);
                        }
                    }
                    else {
                        Error.checkUnsupportedTypeOperation(line);
                    }
                    break;
                default:
                    Error.checkUnsupportedTypeOperation(line);
            }
        }
        else {
            Error.checkInvalidExpr();
        }
    }

    public void runVardef(List<IndividualToken> tokenList,variableMaps definedVar,expressionMap expressions){
        if(tokenList.size() == 5){
            int line = tokenList.get(0).getLine();
            Tokens variableType = tokenList.get(2).getType();
            Tokens valueType = tokenList.get(4).getType();
            Tokens AnotherExprType;
            String variableName = tokenList.get(3).getInputString();
            varNameValid(variableName,line);
            switch (variableType) {
                case BOOL:
                    switch (valueType) {
                        case BOOLVALUE:
                            definedVar.addToDefinedBool(tokenList.get(3).getInputString(), (boolean) tokenList.get(4).getVariable(),line);
                            definedVar.addToVariables(tokenList.get(3).getInputString());
                            break;
                        case IDENTIFIER:
                            if (expressions.alreadyContainsExpr(tokenList.get(4).getInputString())) {
                                AnotherExprType = expressions.getContents(tokenList.get(4).getInputString()).get(0).getType();
                                if (AnotherExprType == Tokens.BINEXPR || AnotherExprType == Tokens.UNEXPR) {
                                    definedVar.addToDefinedBool(tokenList.get(3).getInputString(), definedVar.getFromTempBool("temp" + tokenList.get(4).getInputString()),line);
                                    definedVar.addToVariables(tokenList.get(3).getInputString());
                                }
                            } else if (definedVar.containsVariable(tokenList.get(4).getInputString())) {
                                Boolean var = definedVar.getFromDefinedBool(tokenList.get(4).getInputString());
                                definedVar.addToDefinedBool(tokenList.get(3).getInputString(), var,line);
                                definedVar.addToVariables(tokenList.get(3).getInputString());
                            }
                    }
                    break;
                case INT:
                    switch (valueType) {
                        case INTVALUE:
                            if ((int) tokenList.get(4).getVariable() <= POSITIVE_MAX && (int) tokenList.get(4).getVariable() >= NEGATIVE_MAX) {
                                definedVar.addToDefinedInt(tokenList.get(3).getInputString(), (int) tokenList.get(4).getVariable(),line);
                                definedVar.addToVariables(tokenList.get(3).getInputString());
                            } else {
                                Error.checkIntegerOutofRangeError(line);
                            }
                            break;
                        case IDENTIFIER:
                            if (expressions.alreadyContainsExpr(tokenList.get(4).getInputString())) {
                                AnotherExprType = expressions.getContents(tokenList.get(4).getInputString()).get(0).getType();
                                if (AnotherExprType == Tokens.BINEXPR || AnotherExprType == Tokens.UNEXPR) {
                                    definedVar.addToDefinedInt(tokenList.get(3).getInputString(), definedVar.getFromTempInt("temp" + tokenList.get(4).getInputString()),line);
                                    definedVar.addToVariables(tokenList.get(3).getInputString());
                                }
                                else{
                                    Error.checkUnsupportedTypeOperation(line);
                                }
                            } else if (definedVar.containsVariable(tokenList.get(4).getInputString())) {
                                Integer var = definedVar.getFromDefinedInt(tokenList.get(4).getInputString());
                                definedVar.addToDefinedInt(tokenList.get(3).getInputString(), var,line);
                                definedVar.addToVariables(tokenList.get(3).getInputString());
                            } else {
                                Error.checkExpressionNotDefinedError(line);
                            }
                    }
                    break;
                default:
                    Error.checkTypeDefError(line);
            }
        }
        else{
            Error.checkInvalidExpr();
        }
    }


    public void runAssign(List<IndividualToken> tokenList, variableMaps definedVar){
        if(tokenList.size() == 4) {
            int line = tokenList.get(0).getLine();
            String varName = tokenList.get(2).getInputString();
            Object newValue = tokenList.get(3).getVariable();
            Tokens type = tokenList.get(3).getType();
            if (definedVar.containsVariable(varName)) {
                if (type != Tokens.IDENTIFIER) {
                    switch (type) {
                        case BOOLVALUE:
                            definedVar.updateDefinedBool(varName, (Boolean) newValue,line);
                            break;
                        case INTVALUE:
                            if ((Integer) newValue >= NEGATIVE_MAX && (Integer) newValue <= POSITIVE_MAX) {
                                definedVar.updateDefinedInt(varName, (Integer) newValue,line);
                            } else {
                                Error.checkIntegerOutofRangeError(line);
                            }
                            break;
                        default:
                            Error.checkUnsupportedTypeOperation(line);
                    }
                } else if (type == Tokens.IDENTIFIER) {
                    if (definedVar.definedBoolContains(tokenList.get(3).getInputString())) {
                        newValue = definedVar.getFromDefinedBool(tokenList.get(3).getInputString());
                        definedVar.updateDefinedBool(varName, (Boolean) newValue,line);
                    } else if (definedVar.tempBoolContains("temp" + tokenList.get(3).getInputString())) {
                        newValue = definedVar.getFromTempBool("temp" + tokenList.get(3).getInputString());
                        definedVar.updateDefinedBool(varName, (Boolean) newValue,line);
                    } else if (definedVar.definedIntContains(tokenList.get(3).getInputString())) {
                        newValue = specialBinUnInt(tokenList.get(3).getInputString(), definedVar);
                        definedVar.updateDefinedInt(varName, (Integer) newValue,line);
                    } else if (definedVar.tempIntContains("temp" + tokenList.get(3).getInputString())) {
                        newValue = specialBinUnInt(tokenList.get(3).getInputString(), definedVar);
                        definedVar.updateDefinedInt(varName, (Integer) newValue,line);
                    } else {
                        Error.checkExpressionNotDefinedError(line);
                    }

                } else {
                    Error.checkUnsupportedTypeOperation(line);
                }
            } else {
                Error.checkExpressionNotDefinedError(line);
            }
        }
        else {
            Error.checkInvalidExpr();
        }
    }

    public void runPrint(List<IndividualToken> tokenList,variableMaps definedVar){
        if(tokenList.size() == 3) {
            int line = tokenList.get(0).getLine();
            String target = tokenList.get(2).getInputString();
            int printInt;
            printInt = specialBinUnInt(target, definedVar);
            if (printInt != ABNORMAL) {
                System.out.print('[');
                System.out.print(printInt);
                System.out.print(']');
            } else if (definedVar.definedBoolContains(target)) {
                System.out.print('[');
                System.out.print(definedVar.getFromDefinedBool(target));
                System.out.print(']');
            } else if (definedVar.tempBoolContains("temp" + target)) {
                System.out.print('[');
                System.out.print(definedVar.getFromTempBool("temp" + target));
                System.out.print(']');
            } else {
                Error.checkExpressionNotDefinedError(line);
            }
        }
        else{
            Error.checkInvalidExpr();
        }
    }

    public static void varNameValid(String name,int line){
        //not keywords, length <= 8, contains digits and English character only
        if(name.isEmpty()){
            Error.checkInvalidVarName(line);
        }
        if(name.length() > 8){      //check length
            Error.checkTooLongName(line);
        }
        for(Tokens keyword:Tokens.values()){    //check keywords.
            if(keyword.toString().equals(name)){
                Error.checkKeyword(line);
            }
        }
        if(Character.isDigit(name.charAt(0))){  //check starting with number
            Error.checkInvalidVarName(line);
        }
        if(!name.matches("[a-zA-Z0-9]+")){  //check only contains number and English Character
            Error.checkInvalidVarName(line);
        }
    }

    private int specialBinUnInt(String operand1, variableMaps definedVar) {
        int var;
        if (definedVar.containsVariable(operand1)) {
            var = definedVar.getFromDefinedInt(operand1);
            return var;
        }
        else if(definedVar.tempIntContains("temp" + operand1)){
            var = definedVar.getFromTempInt("temp"+ operand1);
            return var;
        }
        else {
            return var = ABNORMAL;
        }

    }

    private int rounding(int numResult){
        if(numResult < NEGATIVE_MAX) {
            numResult = NEGATIVE_MAX;
        }
        else if(numResult > POSITIVE_MAX){
            numResult = POSITIVE_MAX;
        }
        return numResult;
    }




}