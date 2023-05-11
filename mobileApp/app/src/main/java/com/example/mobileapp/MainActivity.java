package com.example.mobileapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.SharedPreferences;
import android.content.res.Configuration;
import android.content.res.Resources;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class MainActivity extends AppCompatActivity {

    private serverApi sApi;
    TextView testTextView;

    // Configure OkHttpClient with base URL interceptor
    OkHttpClient client = new OkHttpClient.Builder()
            .addInterceptor(new BaseUrlInterceptor("http://10.0.2.2:8000"))
            .build();

    Retrofit retrofit;
        String serverUrl = "http://10.0.2.2";
      //  String serverUrl = "http://127.0.0.1:8080/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        connectToServer();
    }
    public void connectToServer()
    {
        retrofit = new Retrofit.Builder()
                .baseUrl(serverUrl).addConverterFactory(GsonConverterFactory.create())
                .build();
        sApi = retrofit.create(serverApi.class);
    }

    public void regist(View view)
    {
        RequestBody request = RequestBody.create(MediaType.parse("application/json"), "");
        Call<UsersResponse> call = sApi.usersRes(request);
        call.enqueue(new Callback<UsersResponse>() {
            @Override
            public void onResponse(Call<UsersResponse> call, Response<UsersResponse> response) {
                if (!response.isSuccessful()) {
                    UsersResponse usersResponse = response.body();
                    Toast.makeText(MainActivity.this, "Code: " + usersResponse.getData(), Toast.LENGTH_LONG).show();
                    return;
                } else
                {
                    Toast.makeText(MainActivity.this, "Code"+ response.code(), Toast.LENGTH_LONG);
                }
            }
            @Override
            public void onFailure(Call<UsersResponse> call, Throwable t) {
                Toast.makeText(MainActivity.this, t.getMessage(),Toast.LENGTH_LONG).show();
            }
        });
    }

    SharedPreferences preferences;
    public void setNewUserId(String str_id) {
        preferences = getSharedPreferences("userId", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString("userId", str_id);
        editor.apply();
    }

    public String getUserId()
        {
            preferences = getSharedPreferences("userId", Context.MODE_PRIVATE);
            String userId = preferences.getString("userId", "domyślna_wartość");
            return userId;
        }


}