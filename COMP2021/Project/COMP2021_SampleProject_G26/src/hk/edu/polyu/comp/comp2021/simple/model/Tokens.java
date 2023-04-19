package hk.edu.polyu.comp.comp2021.simple.model;

public enum Tokens {
    //+-*/#%
    MINUS, PLUS, MULTIPLY, DIVISION, SIGNPLUS, NEGATION,MODULO,

    // operator
    GREATER,GREATER_EQUAL, SMALLER, SMALLER_EQUAL, EQUAL,
    NOT_EQUAL, AND, OR, NOT,

    //keywords
    VARDEF, BINEXPR, UNEXPR, ASSIGN, PRINT, SKIP,
    BLOCK, IF, WHILE, PROGRAM, EXECUTE, LIST, STORE, LOAD,
    QUIT, DEBUG, TOGGLEBREAKPOINT, INSPECT, INSTRUMENT,

    //types
    BOOL,INT,

    //identifier
    IDENTIFIER,

    //values
    INTVALUE,BOOLVALUE
}
