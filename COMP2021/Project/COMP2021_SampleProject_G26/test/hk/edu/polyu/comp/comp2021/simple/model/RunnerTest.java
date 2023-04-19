package hk.edu.polyu.comp.comp2021.simple.model;

import org.junit.Before;
import org.junit.Test;
import org.junit.jupiter.api.BeforeEach;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

public class RunnerTest {

//    private Map<String, Boolean> definedBool = new HashMap<>();
//    private Map<String,Integer> definedInt = new HashMap<>();
//    Runner runner = new Runner();



    @Test
   public void BinTest(){
        Runner testRunner = new Runner();
        //expressionMap testExpr = new expressionMap();
        variableMaps variables = new variableMaps();
        List<IndividualToken> testList = new ArrayList<>();
        String input1 = "binexpr expr1 3 + 5";
//       String input2 = "binexpr expr2 4 * 5";
//       String input3 = "binexpr expr3 10 / 2";
//       String input4 = "binexpr expr4 4 - 5";
//       String input5 = "binexpr expr6 true && false";
//       String input6 = "binexpr expr7 false || true";
//       String input7 = "binexpr expr8 10 % 4";
        testList.add(0, new IndividualToken(Tokens.BINEXPR,"binexpr",null,1));
        testList.add( 1, new IndividualToken(Tokens.BINEXPR,"binexpr",null,1));
        testRunner.runBinexpr();


   }

    @Test
    public void UnTest(){
        String input1 = "unexpr expr1 ~ 5";
        String input2 = "unexpr expr2 # -4";
        String input3 = "unexpr expr3 ! true";
        String input4 = "unexpr expr4 ! false";

    }

    @Test
    public void defTest(){
        Map<String, Boolean> definedBool = new HashMap<>();
        Map<String,Integer> definedInt = new HashMap<>();
        String input1 = "vardef def1 bool x true";
        String input2 = "vardef def2 int y 20";
        String input3 = "vardef def3 asdf x 30"; //type error checking test
        //runner.runVardef(input1);
        //runner.runVardef(input2);
        //for(String name:runner.getDefinedBool().keySet()){
            //System.out.println(name + " " + runner.getDefinedInt().get(name).toString());
            //System.out.println(name + " " + runner.getDefinedBool().get(name).toString());
        //}
//        for(String name:runner.getDefinedInt().keySet()){
//            System.out.println(name + " " + runner.getDefinedInt().get(name).toString());
//            //System.out.println(name + " " + runner.getDefinedBool().get(name).toString());
//        }
    }

    @Test
    public void assignTest(){
        String input1 = "assign ass1 x false";
        String input2 = "assign ass1 y true";

        //runner.runAssign(input1);
        //runner.runAssign(input2);
//        for(String name:runner.getDefinedBool().keySet()){
//            //System.out.println(name + " " + runner.getDefinedInt().get(name).toString());
//            System.out.println(name + " " + runner.getDefinedBool().get(name).toString());
//        }
//        for(String name:runner.getDefinedInt().keySet()){
//            System.out.println(name + " " + runner.getDefinedInt().get(name).toString());
//            //System.out.println(name + " " + runner.getDefinedBool().get(name).toString());
//        }
    }




}