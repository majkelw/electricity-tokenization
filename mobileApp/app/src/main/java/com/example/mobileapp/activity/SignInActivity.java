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

public class SignInActivity extends AppCompatActivity {

    private EditText seedEditText;
    private SharedPreferences preferences;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.signin_layout);
        seedEditText = findViewById(R.id.seedEditText);
        preferences = getSharedPreferences("sharedPreferences", Context.MODE_PRIVATE);
    }


    public void signIn(View view) {
        Toast.makeText(SignInActivity.this, "Logowanie jeszcze nie działa", Toast.LENGTH_LONG).show();
    }


    public void changeToSignUpActivity(View view) {
        Intent intent = new Intent(this, SignUpActivity.class);
        startActivity(intent);
        finish();
    }
}
