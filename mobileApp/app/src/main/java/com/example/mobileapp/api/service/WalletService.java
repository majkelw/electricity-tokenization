package com.example.mobileapp.api.service;

import com.example.mobileapp.api.model.response.WalletInfoResponseModel;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface WalletService {

    @GET("/wallet")
    Call<WalletInfoResponseModel> getWallet(@Query("user_id") String userId);
}
