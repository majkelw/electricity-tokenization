package com.example.mobileapp.api;

import com.example.mobileapp.api.response.SignUpResponse;

import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface UserService {

    @POST("/users")
    Call<SignUpResponse> signUp(@Body RequestBody request);

}
