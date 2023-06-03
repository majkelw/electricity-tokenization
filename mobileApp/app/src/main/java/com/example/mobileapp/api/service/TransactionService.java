package com.example.mobileapp.api.service;


import com.example.mobileapp.api.model.request.TransactionRequestModel;
import com.example.mobileapp.api.model.response.TransactionResponseModel;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface TransactionService {

    @POST("/transactions")
    Call<TransactionResponseModel> makeTransaction(@Body TransactionRequestModel transactionBody);
}
