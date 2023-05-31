package com.example.mobileapp.activity;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.mobileapp.R;
import com.example.mobileapp.api.RetrofitHandler;
import com.example.mobileapp.api.model.request.TransactionRequestModel;
import com.example.mobileapp.api.model.response.TransactionResponseModel;
import com.example.mobileapp.api.service.TransactionService;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class TransactionActivity extends AppCompatActivity {

    private SharedPreferences preferences;

    private EditText toUserIdEditText;
    private EditText tokensNumberEditText;
    private TransactionService transactionService;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.transaction_layout);
        toUserIdEditText = findViewById(R.id.toUserIdEditText);
        tokensNumberEditText = findViewById(R.id.tokensNumberEditText);
        preferences = getSharedPreferences("sharedPreferences", Context.MODE_PRIVATE);
        transactionService = RetrofitHandler.getInstance().create(TransactionService.class);
    }

    public void makeTransaction(View view) {

        TransactionRequestModel transactionBody = new TransactionRequestModel(preferences.getString("user_id", null), toUserIdEditText.getText().toString(), Integer.parseInt(tokensNumberEditText.getText().toString()));
        Call<TransactionResponseModel> call = transactionService.makeTransaction(transactionBody);
        call.enqueue(new Callback<TransactionResponseModel>() {
            @Override
            public void onResponse(Call<TransactionResponseModel> call, Response<TransactionResponseModel> response) {
                if (response.isSuccessful()) {
                    TransactionResponseModel userResponse = response.body();
                    Toast.makeText(TransactionActivity.this, userResponse.getMessage(), Toast.LENGTH_LONG).show();
                    finish();
                } else {
                    try {
                        JSONObject errorResponseObject = new JSONObject(response.errorBody().string());
                        Toast.makeText(TransactionActivity.this, errorResponseObject.getString("message"), Toast.LENGTH_LONG).show();
                    } catch (IOException | JSONException e) {
                        throw new RuntimeException(e);
                    }
                }
            }

            @Override
            public void onFailure(Call<TransactionResponseModel> call, Throwable t) {
                Toast.makeText(TransactionActivity.this, t.toString(), Toast.LENGTH_LONG).show();
            }
        });
    }


}
