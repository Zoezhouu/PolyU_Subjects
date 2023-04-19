package hk.edu.polyu.comp.comp2022.assignment1;

public class ScientificNotation {

    public static double getValueFromAeB(String strSequence){

        int exponent = 0;
        double significand = 0.0;
        double retValue;

        // TODO:To parse significand and exponent from strSequence.

        int idx = strSequence.indexOf('e');
        // get significand and exponent in string form
        String strSignificand = "" + strSequence.subSequence(0, idx-1);
        // significand number
        if (strSignificand.startsWith("-")){
            // if significand < 0;
            double sig = strSignificand.charAt(1) - '0';
            for (int i = 3; i < strSignificand.length(); i++){
                char n = strSignificand.charAt(i);
                double sigTemp = n - '0';
                sig = sig + sigTemp/(Math.pow(10,i-2));
            }
            significand = -sig;
        }
        else {
            // if significand >= 0;
            double sig = strSignificand.charAt(0) - '0';
            for (int i = 2; i < strSignificand.length(); i++){
                char n = strSignificand.charAt(i);
                double sigTemp = n - '0';
                sig = sig + sigTemp/(Math.pow(10,i-1));
            }
            significand = sig;

        }


        String strExponent = "" + strSequence.subSequence(idx+1, strSequence.length());
        // exponent number

        if (strExponent.startsWith("-")){
            // if exponent <0;
            int exp = strExponent.charAt(1) - '0';
            for (int i = 2; i < strExponent.length(); i++){
                char n = strExponent.charAt(i);
                int expTemp = n - '0';
                exp = exp * 10 + expTemp;
            }
            exponent = -exp;
        }
        else{
            // if exponent >= 0;
            int exp = strExponent.charAt(0) - '0';
            for (int i = 1; i < strExponent.length(); i++){
                char n = strExponent.charAt(i);
                int expTemp = n - '0';
                exp = exp * 10 + expTemp;
            }
            exponent = exp;
        }



    retValue = significand * Math.pow(10, exponent);
    return retValue;

    }


}
