package com.example.mobileapp;


import java.util.List;

import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;


public interface serverApi {

   /// @POST("users")
   // Call<User> getUser();


    @POST("/users")
    Call<UsersResponse> usersRes(@Body RequestBody request);




}
