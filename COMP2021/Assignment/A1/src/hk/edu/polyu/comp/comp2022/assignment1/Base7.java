package hk.edu.polyu.comp.comp2022.assignment1;

import static java.lang.Math.abs;
import static java.lang.Math.pow;

public class Base7 {

    public static String convertToBase7(int num) {
        // TODO: Add your code here

        String strBase7 = "";
        //string of number in base 7;
        //string to store number calculated by dividing(reversed);

        if (num > 0 ){
            while (num > 0){
                strBase7 = (num%7) + strBase7;
                num /= 7;
            }

        }
        else {
            int numTemp = -num;
            while(numTemp > 0) {
                strBase7 = (numTemp%7) +strBase7;
                numTemp /= 7;
            }
            strBase7 = "-" + strBase7;
        }

        return strBase7;
    }
}
