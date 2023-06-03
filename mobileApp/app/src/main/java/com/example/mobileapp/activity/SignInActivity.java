package com.example.mobileapp.activity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.mobileapp.R;
import com.example.mobileapp.api.RetrofitHandler;
import com.example.mobileapp.api.model.response.UserResponseModel;
import com.example.mobileapp.api.service.UserService;
import com.example.mobileapp.api.model.request.SignInRequestModel;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class SignInActivity extends AppCompatActivity {

    private EditText seedEditText;
    private SharedPreferences preferences;
    private UserService userService;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.signin_layout);
        seedEditText = findViewById(R.id.seedEditText);
        preferences = getSharedPreferences("sharedPreferences", Context.MODE_PRIVATE);
        userService = RetrofitHandler.getInstance().create(UserService.class);

    }

    private void saveKeyValuePair(String key, String value) {
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString(key, value);
        editor.apply();
    }


    public void signIn(View view) {
        Call<UserResponseModel> call = userService.signIn(new SignInRequestModel(seedEditText.getText().toString()));
        call.enqueue(new Callback<UserResponseModel>() {
            @Override
            public void onResponse(Call<UserResponseModel> call, Response<UserResponseModel> response) {
                if (response.isSuccessful()) {
                    UserResponseModel userResponse = response.body();
                    saveKeyValuePair("user_id", userResponse.getUserId());
                    saveKeyValuePair("private_key", userResponse.getPrivateKey());
                    Toast.makeText(SignInActivity.this, "Zalogowano", Toast.LENGTH_LONG).show();
                    saveKeyValuePair("seed", userResponse.getWords()); // save to show in WalletActivity
                    startActivity(new Intent(SignInActivity.this, WalletActivity.class));
                    finish();
                } else {
                    try {
                        JSONObject errorResponseObject = new JSONObject(response.errorBody().string());
                        Toast.makeText(SignInActivity.this, errorResponseObject.getString("message"), Toast.LENGTH_LONG).show();
                    } catch (IOException | JSONException e) {
                        throw new RuntimeException(e);
                    }

                }

            }

            @Override
            public void onFailure(Call<UserResponseModel> call, Throwable t) {
                Toast.makeText(SignInActivity.this, t.toString(), Toast.LENGTH_LONG).show();

            }

        });
    }


    public void changeToSignUpActivity(View view) {
        Intent intent = new Intent(this, SignUpActivity.class);
        startActivity(intent);
        finish();
    }
}
