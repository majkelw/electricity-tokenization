package com.example.mobileapp.activity;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.mobileapp.R;
import com.example.mobileapp.api.RetrofitHandler;
import com.example.mobileapp.api.model.response.TransactionsHistoryResponseModel;
import com.example.mobileapp.api.model.response.WalletInfoResponseModel;
import com.example.mobileapp.api.service.WalletService;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HistoryActivity extends AppCompatActivity {

    private ListView historyView;
    private ArrayList<String> output;
    private ArrayAdapter<String> adapter;
    private WalletService walletService;
    private String userId;
    private SharedPreferences preferences;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.transactions_history_layout);
        historyView = findViewById(R.id.historyView);
        preferences = getSharedPreferences("sharedPreferences", Context.MODE_PRIVATE);
        walletService = RetrofitHandler.getInstance().create(WalletService.class);
        output = new ArrayList<>();
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, output);
        historyView.setAdapter(adapter);
        getWalletInfo();
    }

    private void showHistoryList(List<TransactionsHistoryResponseModel> transactionsHistory) {
        for (int i = transactionsHistory.size() - 1; i >= 0; i--) {
            TransactionsHistoryResponseModel transaction = transactionsHistory.get(i);
            StringBuilder out = new StringBuilder();
            String direction = transaction.getDirection();
            if (direction.equals("IN")) {
                out.append("Transakcja przychodząca\nOd: ").append(transaction.getFrom());
            } else if (direction.equals("OUT")) {
                out.append("Transakcja wychodząca\nDo: ").append(transaction.getTo());
            }
            out.append("\nID: ").append(transaction.getId()).append("\nLiczba tokenów: ")
                    .append(transaction.getAmount()).append("\n").append(transaction.getTime()).append("\n");

            output.add(out.toString());
        }
        adapter.notifyDataSetChanged();
    }

    private void getWalletInfo() {
        userId = preferences.getString("user_id", null);
        Call<WalletInfoResponseModel> call = walletService.getWallet(userId);
        call.enqueue(new Callback<WalletInfoResponseModel>() {
            @Override
            public void onResponse(Call<WalletInfoResponseModel> call, Response<WalletInfoResponseModel> response) {
                if (response.isSuccessful()) {
                    WalletInfoResponseModel userResponse = response.body();
                    showHistoryList(userResponse.getTransactions());
                }
            }

            @Override
            public void onFailure(Call<WalletInfoResponseModel> call, Throwable t) {
                Toast.makeText(HistoryActivity.this, t.toString(), Toast.LENGTH_LONG).show();
            }
        });
    }


}