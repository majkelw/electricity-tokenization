package com.example.mobileapp.api.service;

import com.example.mobileapp.api.body.SignInBody;
import com.example.mobileapp.api.response.UserResponse;

import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface UserService {

    @POST("/users/signup")
    Call<UserResponse> signUp(@Body RequestBody requestBody);

    @POST("/users/signin")
    Call<UserResponse> signIn(@Body SignInBody signInBody);

}
