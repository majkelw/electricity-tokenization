package com.example.mobileapp.api.service;

import com.example.mobileapp.api.model.request.SignInRequestModel;
import com.example.mobileapp.api.model.response.UserResponseModel;

import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface UserService {

    @POST("/users/signup")
    Call<UserResponseModel> signUp(@Body RequestBody requestBody);

    @POST("/users/signin")
    Call<UserResponseModel> signIn(@Body SignInRequestModel signInRequestModel);

}
