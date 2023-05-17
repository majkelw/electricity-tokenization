package com.example.mobileapp.api.response;

import com.google.gson.annotations.SerializedName;

public class SignUpResponse {
    @SerializedName("user_id")
    private String userId;
    @SerializedName("private_key")
    private String privateKey;
    private String words;
    private String message;

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getPrivateKey() {
        return privateKey;
    }

    public void setPrivateKey(String privateKey) {
        this.privateKey = privateKey;
    }

    public String getWords() {
        return words;
    }

    public void setWords(String words) {
        this.words = words;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
