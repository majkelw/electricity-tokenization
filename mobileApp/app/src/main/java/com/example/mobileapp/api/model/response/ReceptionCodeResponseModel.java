package com.example.mobileapp.api.model.response;

import com.google.gson.annotations.SerializedName;

public class ReceptionCodeResponseModel {

    @SerializedName("energy_reception_code")
    private String energyReceptionCode;
    private String message;
    @SerializedName("valid_duration_seconds")
    private int validDurationSeconds;


    public String getEnergyReceptionCode() {
        return energyReceptionCode;
    }

    public void setEnergyReceptionCode(String energyReceptionCode) {
        this.energyReceptionCode = energyReceptionCode;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public int getValidDurationSeconds() {
        return validDurationSeconds;
    }

    public void setValidDurationSeconds(int validDurationSeconds) {
        this.validDurationSeconds = validDurationSeconds;
    }
}
