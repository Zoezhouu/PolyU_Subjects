package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class expressionMap {
    private final HashMap<String, List<IndividualToken>> expressions = new HashMap<>();
    private final List<String> inputOrder = new ArrayList<>();   //keep the order of input variable names
    private final List<String> alreadyRun = new ArrayList<>();
    public void addToExprs(List<IndividualToken> list){
        if(list.size() >= 2){
            if(!(list.get(0).getType() == Tokens.PROGRAM)){
                Runner.varNameValid(list.get(1).getInputString(),list.get(0).getLine());
            }
            if(!expressions.containsKey(list.get(1).getInputString()))
            {
                inputOrder.add(list.get(1).getInputString());
                expressions.put(list.get(1).getInputString(),list);
            }
            else {
                Error.checkExprAlreadyDefined(list.get(0).getLine());
            }
        }
        else {
            Error.checkInvalidExpr();
        }
    }

    public List<String> getOrder(){
        return inputOrder;
    }
    public HashMap<String, List<IndividualToken>> getExpressions() {
        return expressions;
    }
    public List<IndividualToken> getContents(String key){
        return expressions.get(key);
    }



    public boolean alreadyContainsExpr(String exprName){
        return alreadyRun.contains(exprName);
    }

    public boolean containsExpr(String exprName){
        return expressions.containsKey(exprName);
    }


}
