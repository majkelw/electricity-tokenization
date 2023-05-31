package com.example.mobileapp.activity;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.mobileapp.R;
import com.example.mobileapp.api.RetrofitHandler;
import com.example.mobileapp.api.model.request.ReceptionCodeRequestModel;
import com.example.mobileapp.api.model.response.ReceptionCodeResponseModel;
import com.example.mobileapp.api.service.TokenService;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class EnergyReceptionActivity extends AppCompatActivity {

    private TokenService tokenService;
    private SharedPreferences preferences;
    private TextView receptionCodeTextView;
    private TextView validDurationTextView;
    private String userId;
    private ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();
    private Handler handler;
    private Runnable timerRunnable;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.energy_reception_layout);
        receptionCodeTextView = findViewById(R.id.receptionCodeTextView);
        validDurationTextView = findViewById(R.id.validDurationTextView);
        tokenService = RetrofitHandler.getInstance().create(TokenService.class);
        preferences = getSharedPreferences("sharedPreferences", Context.MODE_PRIVATE);
        userId = preferences.getString("user_id", null);
        generateEnergyReceptionCode();
    }


    private void generateEnergyReceptionCode() {
        Call<ReceptionCodeResponseModel> call = tokenService.generateReceptionCode(new ReceptionCodeRequestModel(userId));
        call.enqueue(new Callback<ReceptionCodeResponseModel>() {
            @Override
            public void onResponse(Call<ReceptionCodeResponseModel> call, Response<ReceptionCodeResponseModel> response) {
                if (response.isSuccessful()) {
                    ReceptionCodeResponseModel receptionCodeResponseModel = response.body();
                    receptionCodeTextView.setText(receptionCodeResponseModel.getEnergyReceptionCode());
                    validDurationTextView.setText(Integer.toString(receptionCodeResponseModel.getValidDurationSeconds()));
                    handler = new Handler(Looper.getMainLooper());
                    timerRunnable = new Runnable() {
                        int duration = receptionCodeResponseModel.getValidDurationSeconds();
                        @Override
                        public void run() {
                            if (duration == 0) {
                                validDurationTextView.setText(String.valueOf(0));
                                finish();
                                return;
                            }
                            validDurationTextView.setText(String.valueOf(duration));
                            duration--;
                            handler.postDelayed(this, 1000);
                        }
                    };
                    timerRunnable.run();
                }
            }

            @Override
            public void onFailure(Call<ReceptionCodeResponseModel> call, Throwable t) {
                Toast.makeText(EnergyReceptionActivity.this, t.toString(), Toast.LENGTH_LONG).show();
            }

        });


    }


}
