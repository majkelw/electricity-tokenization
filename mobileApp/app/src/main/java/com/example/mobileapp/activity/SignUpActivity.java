package com.example.mobileapp.activity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.mobileapp.R;
import com.example.mobileapp.api.RetrofitHandler;
import com.example.mobileapp.api.model.response.UserResponseModel;
import com.example.mobileapp.api.service.UserService;

import okhttp3.MediaType;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class SignUpActivity extends AppCompatActivity {

    private SharedPreferences preferences;
    private UserService userService;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        preferences = getSharedPreferences("sharedPreferences", Context.MODE_PRIVATE);
        super.onCreate(savedInstanceState);
        if (preferences.getString("user_id", null) != null) {
            Intent intent = new Intent(this, WalletActivity.class);
            startActivity(intent);
            finish();
        } else {
            setContentView(R.layout.signup_layout);
            userService = RetrofitHandler.getInstance().create(UserService.class);
        }
    }

    private void saveKeyValuePair(String key, String value) {
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString(key, value);
        editor.apply();
    }

    public void signUp(View view) {

        Call<UserResponseModel> call = userService.signUp(RequestBody.create(MediaType.parse("application/json"), ""));
        call.enqueue(new Callback<UserResponseModel>() {
            @Override
            public void onResponse(Call<UserResponseModel> call, Response<UserResponseModel> response) {
                if (response.isSuccessful()) {
                    UserResponseModel userResponse = response.body();
                    saveKeyValuePair("user_id", userResponse.getUserId());
                    saveKeyValuePair("private_key", userResponse.getPrivateKey());
                    Toast.makeText(SignUpActivity.this, userResponse.getMessage(), Toast.LENGTH_LONG).show();
                    saveKeyValuePair("seed", userResponse.getWords()); // save to show in WalletActivity
                    startActivity(new Intent(SignUpActivity.this, WalletActivity.class));
                    finish();
                }
            }

            @Override
            public void onFailure(Call<UserResponseModel> call, Throwable t) {
                Toast.makeText(SignUpActivity.this, t.toString(), Toast.LENGTH_LONG).show();
            }
        });
    }

    public void changeToSignInActivity(View view) {
        Intent intent = new Intent(this, SignInActivity.class);
        startActivity(intent);
        finish();
    }


}
