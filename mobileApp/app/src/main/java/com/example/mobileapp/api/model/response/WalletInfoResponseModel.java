package com.example.mobileapp.api.model.response;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class WalletInfoResponseModel {

    private int bilance;
    @SerializedName("energy_consumpted")
    private int energyConsumpted;
    @SerializedName("energy_produced")
    private int energyProduced;
    @SerializedName("total_transactions")
    private int totalTransactions;
    @SerializedName("total_operations")
    private int totalOperations;

    @SerializedName("transactions")
    private List<TransactionsHistoryResponseModel> transactionsHis;

    private String transctionStr;

    public int getBilance() {
        return bilance;
    }

    public void setBilance(int bilance) {
        this.bilance = bilance;
    }

    public int getEnergyConsumpted() {
        return energyConsumpted;
    }

    public void setEnergyConsumpted(int energyConsumpted) {
        this.energyConsumpted = energyConsumpted;
    }

    public int getEnergyProduced() {
        return energyProduced;
    }

    public void setEnergyProduced(int energyProduced) {
        this.energyProduced = energyProduced;
    }

    public int getTotalTransactions() {
        return totalTransactions;
    }

    public void setTotalTransactions(int totalTransactions) {
        this.totalTransactions = totalTransactions;
    }

    public int getTotalOperations() {
        return totalOperations;
    }

    public void setTotalOperations(int totalOperations) {
        this.totalOperations = totalOperations;
    }

    public String getTransactionsStr(){return transctionStr;}

    public List<TransactionsHistoryResponseModel> getTransactionsHis()
    {
        return transactionsHis;
    }

}
