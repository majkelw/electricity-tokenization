package com.example.mobileapp.api.model.request;

import com.google.gson.annotations.SerializedName;

public class ReceptionCodeRequestModel {
    @SerializedName("user_id")
    private String userId;

    public ReceptionCodeRequestModel(String userId) {
        this.userId = userId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }
}
