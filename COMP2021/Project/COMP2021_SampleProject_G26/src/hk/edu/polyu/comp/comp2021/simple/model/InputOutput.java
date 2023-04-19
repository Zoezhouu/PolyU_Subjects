package hk.edu.polyu.comp.comp2021.simple.model;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

public class InputOutput {
    public static void printExpressions(expressionMap expressions, List<String> statements){
        //Set<String> uniqueStatements = new HashSet<>(statements);
        List<IndividualToken> tokenList;
        for(String statement:statements){
            tokenList = expressions.getContents(statement);
            for(int j = 0; j < tokenList.size(); j++){
                System.out.print(tokenList.get(j).toSting() + " ");
            }
            System.out.println();
        }
    }

    public static void storeExpressions(expressionMap expressions,List<String> statements,String path){
        List<IndividualToken> tokenList;
        OutputStream out = null;
        try {
            out = new FileOutputStream(path);
        } catch (FileNotFoundException e) {
            System.out.println("Path not found");
            System.exit(1);
        }
        for (String statement : statements) {
            tokenList = expressions.getContents(statement);
            StringBuilder newStatement = new StringBuilder();
            for (int j = 0; j < tokenList.size(); j++) {
                newStatement.append(tokenList.get(j).toSting()).append(" ");
            }
            try {
                newStatement.append("\n");
                byte[] dataBytes = newStatement.toString().getBytes();
                if(out != null){
                    out.write(dataBytes);
                }
                else {
                    System.out.println("Cannot read file");
                    System.exit(1);
                }
            } catch (IOException ignored) {
                System.out.println("Output not successful");
                System.exit(1);
            }
        }
        try {
            out.close();
        } catch (IOException e) {
            System.out.println("cannot close file");
            System.exit(1);
        }
    }

    public static expressionMap loadProgram(String path, String programName){
        expressionMap expressions = new expressionMap();
        Scanning scanner = new Scanning();
        Path fileName = Path.of(path);
        String tempExpr;
        Scanner sc = null;
        try {
            sc = new Scanner(fileName);
        } catch (IOException e) {
            System.out.println("read file not successful");
            System.exit(1);
        }
        if(sc == null){
            System.out.println("read file not successful");
            System.exit(1);
        }
        while (sc.hasNext()) {
            tempExpr = sc.nextLine();
            expressions.addToExprs(scanner.parseToTokens(tempExpr));
        }
        if(expressions.containsExpr(expressions.getOrder().get(0))){
            List<IndividualToken> programBody = expressions.getContents(expressions.getOrder().get(0));
            IndividualToken newProgram = new IndividualToken(Tokens.IDENTIFIER,programName,null,1);
            if(programBody.size() == 3){
                programBody.set(1,newProgram);
            }
            else {
                Error.noDefinedProgram(programName);
            }
            expressions.getExpressions().remove(expressions.getOrder().get(0));
            expressions.getOrder().remove(0);
            expressions.getExpressions().put(programName,programBody);
            expressions.getOrder().add(0,programName);
        }
        return expressions;
    }
}
