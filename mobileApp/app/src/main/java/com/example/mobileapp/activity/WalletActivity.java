package com.example.mobileapp.activity;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import com.example.mobileapp.R;
import com.example.mobileapp.api.RetrofitHandler;
import com.example.mobileapp.api.model.response.WalletInfoResponseModel;
import com.example.mobileapp.api.service.WalletService;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class WalletActivity extends AppCompatActivity {

    private WalletService walletService;
    private SharedPreferences preferences;
    private SwipeRefreshLayout swipeRefreshLayout;
    private TextView userIdTextView;
    private TextView tokensNumberTextView;
    private String userId;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.wallet_layout);
        userIdTextView = findViewById(R.id.userIdTextView);
        tokensNumberTextView = findViewById(R.id.tokensNumberTextView);
        swipeRefreshLayout = findViewById(R.id.swipeRefreshLayout);

        preferences = getSharedPreferences("sharedPreferences", Context.MODE_PRIVATE);
        walletService = RetrofitHandler.getInstance().create(WalletService.class);

        // shows seed dialog only once after sign up, then clear seed
        String seed = preferences.getString("seed", null);
        if (seed != null) {
            showSeedInDialog(seed);
            preferences.edit().remove("seed").apply();
        }
        userId = preferences.getString("user_id", null);
        if (userId != null) {
            userIdTextView.setText(userId);
            getWalletInfo();
        }

        handleRefresh();
    }

    private void showSeedInDialog(String seed) {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("ZAPISZ WYGENEROWANE SŁOWA!");
        builder.setMessage(seed + "\n\nTe 24 słowa będą potrzebne, gdy będziesz chciał zalogować się na innym urządzeniu\n" +
                "Kliknij OK, aby je automatycznie skopiować");
        builder.setPositiveButton("OK", (dialog, which) -> {
            ClipboardManager clipboardManager = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
            ClipData clipData = ClipData.newPlainText("Label", seed);
            clipboardManager.setPrimaryClip(clipData);
        });
        AlertDialog dialog = builder.create();
        dialog.show();
    }

    private void getWalletInfo() {
        Call<WalletInfoResponseModel> call = walletService.getWallet(userId);
        call.enqueue(new Callback<WalletInfoResponseModel>() {
            @Override
            public void onResponse(Call<WalletInfoResponseModel> call, Response<WalletInfoResponseModel> response) {
                if (response.isSuccessful()) {
                    WalletInfoResponseModel userResponse = response.body();
                    String tokensNumberText = tokensNumberTextView.getText().toString().split("\n")[0]
                            + "\n" + userResponse.getBilance();
                    tokensNumberTextView.setText(tokensNumberText);
                }
            }

            @Override
            public void onFailure(Call<WalletInfoResponseModel> call, Throwable t) {
                Toast.makeText(WalletActivity.this, t.toString(), Toast.LENGTH_LONG).show();
            }

        });
    }

    public void backToMainActivity(View view) {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(true);
        builder.setMessage("Czy na pewno chcesz się wylogować?\n" +
                "Jeżeli nie posiadasz zapisanych seedów dostęp do portfela zostanie utracony");
        builder.setPositiveButton("Wyloguj", (dialog, which) -> {
            preferences.edit().remove("user_id").remove("private_key").apply();
            Intent intent = new Intent(this, SignInActivity.class);
            startActivity(intent);
            finish();
        });
        builder.setNegativeButton(android.R.string.cancel, (dialog, which) -> {
        });
        AlertDialog dialog = builder.create();
        dialog.show();
    }

    public void changeToTransactionActivity(View view) {
        Intent intent = new Intent(this, TransactionActivity.class);
        startActivity(intent);
    }

    public void changeToEnergyReceptionActivity(View view) {
        Intent intent = new Intent(this, EnergyReceptionActivity.class);
        startActivity(intent);
    }

    private void handleRefresh() {
        swipeRefreshLayout.setOnRefreshListener(() -> {
            getWalletInfo();
            swipeRefreshLayout.setRefreshing(false);
        });
    }

}
