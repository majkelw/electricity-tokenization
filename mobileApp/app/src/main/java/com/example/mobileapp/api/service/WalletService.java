package com.example.mobileapp.api.service;

import com.example.mobileapp.api.response.WalletInfoResponse;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface WalletService {

    @GET("/wallet")
    Call<WalletInfoResponse> getWallet(@Query("user_id") String userId);
}
