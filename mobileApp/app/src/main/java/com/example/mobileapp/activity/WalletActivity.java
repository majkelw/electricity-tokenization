package com.example.mobileapp.activity;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.example.mobileapp.R;

public class WalletActivity extends AppCompatActivity {

    private SharedPreferences preferences;
    private TextView userIdTextView;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.wallet_layout);
        userIdTextView = findViewById(R.id.userIdTextView);
        preferences = getSharedPreferences("sharedPreferences", Context.MODE_PRIVATE);
        String userId = preferences.getString("user_id", null);
        if (userId != null) {
            userIdTextView.setText(userId);
        }
        // shows seed dialog only once after sign up, then clear seed
        String seed = preferences.getString("seed", null);
        if (seed != null) {
            showSeedInDialog();
            preferences.edit().remove("seed").apply();
        }
    }

    private void showSeedInDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("ZAPISZ WYGENEROWANE SŁOWA!");
        builder.setMessage("visual boring fluid gloom robot strike twist risk leisure piano foster movie green net lift oxygen snack flight fame tail scissors they word imitate"
                + "\n\nTe 24 słowa będą potrzebne, gdy będziesz chciał zalogować się na innym urządzeniu\nKliknij OK, aby je automatycznie skopiować");
        builder.setPositiveButton("OK", (dialog, which) -> {
            ClipboardManager clipboardManager = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
            ClipData clipData = ClipData.newPlainText("Label", "visual boring fluid gloom robot strike twist risk leisure piano foster movie green net lift oxygen snack flight fame tail scissors they word imitate");
            clipboardManager.setPrimaryClip(clipData);
        });
        AlertDialog dialog = builder.create();
        dialog.show();
    }

    public void backToMainActivity(View view) {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(true);
        builder.setMessage("Czy na pewno chcesz się wylogować?\nJeżeli nie posiadasz zapisanych seedów dostęp do portfela zostanie utracony");
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

}
