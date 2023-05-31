package com.example.mobileapp.api.model.request;

public class SignInRequestModel {
    private String words;

    public SignInRequestModel(String words) {
        this.words = words;
    }

    public String getWords() {
        return words;
    }

    public void setWords(String words) {
        this.words = words;
    }
}
