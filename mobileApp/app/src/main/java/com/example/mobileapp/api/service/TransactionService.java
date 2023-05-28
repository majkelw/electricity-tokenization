package com.example.mobileapp.api.service;


import com.example.mobileapp.api.body.TransactionBody;
import com.example.mobileapp.api.response.TransactionResponse;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface TransactionService {

    @POST("/transactions")
    Call<TransactionResponse> makeTransaction(@Body TransactionBody transactionBody);
}
