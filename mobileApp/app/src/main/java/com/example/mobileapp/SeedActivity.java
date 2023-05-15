package com.example.mobileapp;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class SeedActivity extends AppCompatActivity {

    public TextView seedTextView;
    public Button btn_seed_ok;

    //@SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.seed_output_layout);

        //seedTextView = findViewById(R.id.seed_output);
        btn_seed_ok = findViewById(R.id.btn_seed_ok);
        //seedShow();
    }



    public String seedGenerator()
    {
        String str = "";

        for(int i = 0; i<100;i++)
        {
            str = str + " seed";
        }
        return str;
    }

    public void seedShow()
    {
       seedTextView.setText(seedGenerator());
    }

    public void openWalletLayout(View view)
    {
        try {


            Intent intent2 = new Intent(this, WalletActivity.class);
            startActivity(intent2);
        }catch (Exception exception)
        {
            Log.d("SeedActivity","Msg "+exception.getMessage());
        }
    }


}
