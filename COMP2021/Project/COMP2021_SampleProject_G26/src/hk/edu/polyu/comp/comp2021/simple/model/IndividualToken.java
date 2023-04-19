package hk.edu.polyu.comp.comp2021.simple.model;


public class IndividualToken {
    private final Tokens type;

    private final String inputString;
    private final Object variable;
    private final int line;

    IndividualToken(Tokens type, String inputString, Object variable, int line){
        this.type = type;
        this.inputString = inputString;
        this.variable = variable;
        this.line = line;
    }

    public Tokens getType() {
        return type;
    }

    public Object getVariable() {
        return variable;
    }



    public String getInputString() {
        return inputString;
    }

    @Override
    public boolean equals(Object obj) {
        if(obj instanceof IndividualToken){
            return ((IndividualToken) obj).getType() == this.getType()
                    && ((IndividualToken) obj).getInputString().equals(this.getInputString())
                    && ((IndividualToken) obj).getVariable() == this.getVariable()
                    && ((IndividualToken) obj).getLine() == this.getLine();
        }
        return false;
    }
    public int getLine(){return line;}
    public String toSting(){
        return inputString;
    }
}

