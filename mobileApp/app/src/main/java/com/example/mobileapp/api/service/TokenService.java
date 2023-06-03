package com.example.mobileapp.api.service;

import com.example.mobileapp.api.model.request.ReceptionCodeRequestModel;
import com.example.mobileapp.api.model.response.ReceptionCodeResponseModel;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface TokenService {

    @POST("/tokens/reception-code")
    Call<ReceptionCodeResponseModel> generateReceptionCode(@Body ReceptionCodeRequestModel receptionCodeRequestModel);
}
