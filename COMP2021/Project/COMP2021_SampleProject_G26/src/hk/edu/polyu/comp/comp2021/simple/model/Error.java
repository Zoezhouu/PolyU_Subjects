package hk.edu.polyu.comp.comp2021.simple.model;

import java.lang.reflect.Member;

public class Error extends RuntimeException{
    //general check: statement lab/expression name/variable name
    // not keywords, length <= 8, contains digits and English character only

    //check for vardef: -99999 <= int value <= 99999
    //check for binexpr, left and right are same type, if exp, exp must exist, if variable, variable must be defined and
    //of same type as value, or expression calculation result
    //check for unexpr, right exp, exp must exist, right variable, variable must be defined,
    //right value, must correspond to the operations
    //assign: variable must be defined, exp must be defined, value must same type as left variable

    Error(String message){
        super(message);
    }
    //vardef errors
    public static void checkTypeDefError(int line){
        String message = "line " + line + ": " + "Unsupported Type";
        throw new Error(message);
    }
    public static void checkIntegerOutofRangeError(int line){
        String message = "line " + line + ": " + "Integer out of Range";
        throw new Error(message);}
    public static void checkExpressionNotDefinedError(int line){
        String message = "line " + line + ": " + "Expression not defined";
        throw new Error(message);}
    public static void checkVarAlreadyDefinedError(int line){
        String message = "line " + line + ": " + "Variable already defined";
        throw new Error(message);
    }

    public static void checkTooLongName(int line){
        String message = "line " + line + ": " + "Length of Variable or Expression Name exceeds 8";
        throw new Error(message);
    }

    public static void checkKeyword(int line){
        String message = "line " + line + ": " + "Defined variable name or expression name is SIMPLE keyword";
        throw new Error(message);
    }
    public static void checkInvalidVarName(int line){
        String message = "line " + line + ": " + "Invalid Variable Name";
        throw new Error(message);
    }

    public static void checkInvalidExpr(){
        String message = "Expression not defined properly";
        throw new Error(message);
    }

    public static void checkInvalidOperations(int line){
        String message = "line " + line + ": " + "Invalid Operation";
        throw new Error(message);
    }

    public static void checkUnsupportedTypeOperation(int line){
        String message = "line " + line + ": " + "Type of right or left operands are not supported in this operation";
        throw new Error(message);
    }
    public static void checkDivisionByZero(int line){
        String message = "line " + line + ": " + "Division by zero";
        throw new Error(message);
    }

    public static void checkExprAlreadyDefined(int line){
        String message = "line " + line + "Expression already defined";
        throw new Error(message);
    }

    public static void noDefinedProgram(String programName){
        String message = "Program  " + programName + ": " + "is not defined.";
        throw new Error(message);
    }

}
