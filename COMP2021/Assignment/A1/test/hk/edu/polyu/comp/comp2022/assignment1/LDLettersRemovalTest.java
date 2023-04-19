package hk.edu.polyu.comp.comp2022.assignment1;
import org.junit.Test;
import static org.junit.Assert.*;

public class LDLettersRemovalTest {
    @Test(timeout = 2000)
    public void test1() {
        assertEquals("dabc", LDLettersRemoval.removeLDLetters("abcadabc"));
    }
    @Test(timeout = 2000)
    public void test2() {
        assertEquals("a", LDLettersRemoval.removeLDLetters("a"));
    }
    @Test(timeout = 2000)
    public void test3() {
        assertEquals("b", LDLettersRemoval.removeLDLetters("bbbbbbb"));
    }
    @Test(timeout = 2000)
    public void test4() {
        assertEquals("cf", LDLettersRemoval.removeLDLetters("cffcfccffccfcffcfccfcffccffcfccf"));
    }

}
