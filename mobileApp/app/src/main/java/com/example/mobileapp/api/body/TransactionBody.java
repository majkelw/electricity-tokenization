package com.example.mobileapp.api.body;

import com.google.gson.annotations.SerializedName;

public class TransactionBody {
    @SerializedName("user_id_from")
    private String userIdFrom;
    @SerializedName("user_id_to")
    private String userIdTo;
    private int amount;

    public TransactionBody(String userIdFrom, String userIdTo, int amount) {
        this.userIdFrom = userIdFrom;
        this.userIdTo = userIdTo;
        this.amount = amount;
    }

    public String getUserIdFrom() {
        return userIdFrom;
    }

    public void setUserIdFrom(String userIdFrom) {
        this.userIdFrom = userIdFrom;
    }

    public String getUserIdTo() {
        return userIdTo;
    }

    public void setUserIdTo(String userIdTo) {
        this.userIdTo = userIdTo;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
}
