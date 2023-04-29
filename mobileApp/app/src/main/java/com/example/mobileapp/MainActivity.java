package com.example.mobileapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class MainActivity extends AppCompatActivity {

    private serverApi sApi;
    Retrofit retrofit;
    String serverUrl = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



    }


    public void connectToServer()
    {

        retrofit = new Retrofit.Builder()
                .baseUrl(serverUrl).addConverterFactory(GsonConverterFactory.create())
                .build();

        sApi = retrofit.create(serverApi.class);



    }






}