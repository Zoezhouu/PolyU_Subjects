package hk.edu.polyu.comp.comp2021.simple.model;

import java.util.HashMap;

public class KeywordsMap implements HashMaps {
    private static final HashMap<String,Tokens> keywords = new HashMap<>();

    static{
        keywords.put("vardef",Tokens.VARDEF);
        keywords.put("binexpr",Tokens.BINEXPR);
        keywords.put("unexpr",Tokens.UNEXPR);
        keywords.put("assign",Tokens.ASSIGN);
        keywords.put("print",Tokens.PRINT);
        keywords.put("skip",Tokens.SKIP);
        keywords.put("block",Tokens.BLOCK);
        keywords.put("if",Tokens.IF);
        keywords.put("while",Tokens.WHILE);
        keywords.put("program",Tokens.PROGRAM);
        keywords.put("execute",Tokens.EXECUTE);
        keywords.put("list",Tokens.LIST);
        keywords.put("store",Tokens.STORE);
        keywords.put("load",Tokens.LOAD);
        keywords.put("quit",Tokens.QUIT);
        keywords.put("debug",Tokens.DEBUG);
        keywords.put("togglebreakpoint",Tokens.TOGGLEBREAKPOINT);
        keywords.put("inspect",Tokens.INSPECT);
        keywords.put("instrument",Tokens.INSTRUMENT);
    }

    @Override
    public Tokens getFromMap(String key) {
        return keywords.get(key);
    }
}
