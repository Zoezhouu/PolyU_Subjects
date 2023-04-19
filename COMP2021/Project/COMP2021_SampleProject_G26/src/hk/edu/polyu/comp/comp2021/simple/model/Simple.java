package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.*;

public class Simple {
    public void runSimple() {
        Scanner input = new Scanner(System.in);
        String source = "";
        Scanning parsing = new Scanning();
        expressionMap expressions = new expressionMap();
        Runner interpreter = new Runner();
        While myWhile = new While();
        If myIf = new If();
        Block block = new Block();
        Execute exe = new Execute();
        String programName;
        List<String> outputStatements;
        while (true) {
            System.out.print("> ");
            source = input.nextLine();
            List<IndividualToken> list = parsing.parseToTokens(source);
            if (source.equals("quit")) {
                System.exit(0);
            }
            else if (source.trim().isEmpty()) {
                continue;
            }
            else if (list.get(0).getInputString().equals("execute")) {
                if(list.size() == 2){
                    programName = list.get(1).getInputString();
                    exe.executeProgram(programName, new Program(expressions,myWhile,myIf,interpreter,block,programName));
                    System.out.println();
                }
                else{
                    System.out.println("no defined program");
                    continue;
                }
            }
            else if(list.get(0).getInputString().equals("list")){
                if(list.size() == 2){
                    programName = list.get(1).getInputString();
                    outputStatements = exe.outputExecutionOrder(programName,new Program(expressions,myWhile,myIf,interpreter,block,programName));
                    InputOutput.printExpressions(expressions,outputStatements);
                }
                else{
                    System.out.println("no defined program here");
                    continue;
                }
            }
            else if(list.get(0).getInputString().equals("store")){
                if(list.size() == 3){
                    programName = list.get(1).getInputString();
                    outputStatements = exe.outputExecutionOrder(programName,new Program(expressions,myWhile,myIf,interpreter,block,programName));
                    InputOutput.storeExpressions(expressions,outputStatements,list.get(2).getInputString());
                }
                else {
                    System.out.println("no defined program here");
                    continue;
                }
            }
            else if(list.get(0).getInputString().equals("load")){
                if(list.size() == 3){
                    programName = list.get(2).getInputString();
                    expressions = InputOutput.loadProgram(list.get(1).getInputString(),programName);
                }
                else {
                    System.out.println("no path find to load program");
                    continue;
                }
            }
            else{
                expressions.addToExprs(list);
            }
        }
    }
}
