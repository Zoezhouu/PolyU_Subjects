package hk.edu.polyu.comp.comp2021.assignment3.inheritance;

import org.junit.Test;
import static org.junit.Assert.*;

public class InheritanceRelationTest {

    A a;
    B b;
    C c;
    D d;

    @Test
    public void testConstructorB(){
        b = new B("b");
        assertEquals(b.getName(), "b");
    }

    @Test
    public void testSendMsgB(){
        b = new B("b");
        assertEquals(b.sendMsg("1"), "bB1");
    }

    @Test
    public void testConstructorC(){
        c = new C("c");
        assertEquals(c.getName(), "c");
    }

    @Test
    public void testSendMsgC(){
        c = new C("c");
        assertEquals(c.sendMsg("2"), "c2");
    }

    @Test
    public void testConstructorD(){
        d = new D("d");
        assertEquals(d.getName(), "dD");
    }

    @Test
    public void testSendMsgD(){
        d = new D("d");
        assertEquals(d.sendMsg("3"), "ddD3");
    }

    @Test
    public void testSendMsgB1(){
        b = new B("bb");
        assertEquals(b.sendMsg("b1"), "bbBb1");
    }

    @Test
    public void testSendMsgC1(){
        c = new C("cc");
        assertEquals(c.sendMsg("c2"), "ccc2");
    }

    @Test
    public void testConstructorD1(){
        d = new D("dd");
        assertEquals(d.getName(), "ddD");
    }

    @Test
    public void testSendMsgD1(){
        d = new D("dd");
        assertEquals(d.sendMsg("d3"), "ddddDd3");
    }

}
