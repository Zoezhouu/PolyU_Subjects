package hk.edu.polyu.comp.comp2022.assignment1;

public class LDLettersRemoval {

    public static String removeLDLetters(String str){
        // TODO: Add your code here
        String strNew = "";
        int l = str.length();
        for (int i = 0; i < l; i++){
            char c1 = str.charAt(i);
            if (str.indexOf(c1) == str.lastIndexOf(c1)) {
                strNew += c1 ;
            }
            else {
                if (str.indexOf(c1) == i){
                    strNew += c1;
                }
            }
        }
        String strLDL = "";
        if (str.lastIndexOf(strNew) == -1) {
            int originIndex = str.lastIndexOf(strNew.charAt(0));
            for (int i = 0; i < strNew.length();i++){
                char c2 = strNew.charAt(i);
                int index = str.lastIndexOf(c2);
                if (originIndex > index){
                    originIndex = index;
                }
            }
            strLDL += str.subSequence(originIndex, str.length());
        }
        else{
            strLDL += strNew;
        }

        return strLDL;
    }
    public static void main(String[] args){
        System.out.println(removeLDLetters("aabbbb"));
    }
}
