package com.example.mobileapp.api.body;

public class SignInBody {
    private String words;

    public SignInBody(String words) {
        this.words = words;
    }

    public String getWords() {
        return words;
    }

    public void setWords(String words) {
        this.words = words;
    }
}
