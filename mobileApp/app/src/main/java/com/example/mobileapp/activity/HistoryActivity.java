package com.example.mobileapp.activity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.mobileapp.R;
import com.example.mobileapp.api.RetrofitHandler;
import com.example.mobileapp.api.model.response.TransactionsHistoryResponseModel;
import com.example.mobileapp.api.model.response.WalletInfoResponseModel;
import com.example.mobileapp.api.service.WalletService;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HistoryActivity extends AppCompatActivity {


    String transaction_json_str = "[\n" +
            "    {\n" +
            "        \"id\": \"0\",\n" +
            "        \"from\": \"e61f2885\",\n" +
            "        \"to\": \"4c94f6\",\n" +
            "        \"amount\": \"1.0\",\n" +
            "        \"direction\": \"IN\",\n" +
            "        \"time\": \"2023-05-31 20:29:38.2820479\"\n" +
            "    },\n" +
            "    {\n" +
            "        \"id\": \"1\",\n" +
            "        \"from\": \"e61f2885\",\n" +
            "        \"to\": \"4c94f6\",\n" +
            "        \"amount\": \"3.0\",\n" +
            "        \"direction\": \"IN\",\n" +
            "        \"time\": \"2023-05-29 15:29:38.2820479\"\n" +
            "    },\n" +
            "    {\n" +
            "        \"id\": \"2\",\n" +
            "        \"from\": \"e61f2885\",\n" +
            "        \"to\": \"4c94f6\",\n" +
            "        \"amount\": \"3.0\",\n" +
            "        \"direction\": \"OUT\",\n" +
            "        \"time\": \"2023-05-25 12:39:58.2820479\"\n" +
            "    }\n" +
            "]";

    public ListView historyView;

    private ArrayList<String> output;
    private ArrayAdapter<String> adapter;
    public TextView hisTextView;
    private WalletService walletService;
    private String userId;
    private SharedPreferences preferences;

    private List<TransactionsHistoryResponseModel> transHistory;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history);
        historyView = findViewById(R.id.historyView);
        hisTextView = findViewById(R.id.hisTextView);
        walletService = RetrofitHandler.getInstance().create(WalletService.class);
       // getWalletInfo();
        output = new ArrayList<String>();
         adapter = new ArrayAdapter<String>(this,android.R.layout.simple_list_item_1,output);
        historyView.setAdapter(adapter);

        //showListBasedOnJSONString() 
        getWalletInfo();
    }
    private void showListBasedOnJSONString()
    {
        try{
            JSONArray array = new JSONArray(transaction_json_str);
            int length =array.length();
            for ( int i = 0 ; i < length; i++){
                JSONObject obj = array.getJSONObject(i);

                String id = obj.getString("id");
                String from = obj.getString("from");
                String to = obj.getString("to");
                String amount =  obj.getString("amount");
                String direction = obj.getString("direction");
                String time = obj.getString("time");

                String firstLine = "";
                if(direction.equals("IN"))
                {
                    firstLine ="Transakcja przychodząca \n " +"Od: " + from;
                }
                else if(direction.equals("OUT"))
                {
                    firstLine ="Transakcja wychodząca \n"+ "Do: " +to;
                }

                String output_item = firstLine + "\n Id: "+ id+ "\n" + "Ilość "+ amount+ " \n"+ time+ "\n";
                output.add(output_item);
            }
        }catch (JSONException e) {
            e.printStackTrace();
        }
        adapter.notifyDataSetChanged();
    }
    private void showHistoryList()
    {

        int length = transHistory.size();
        for ( int i = 0 ; i < length; i++){
           TransactionsHistoryResponseModel obj = transHistory.get(i);

            int id = obj.getId();
            String from = obj.getFrom();
            String to = obj.getTo();
            float amount = obj.getAmount();
            String direction = obj.getDirection();
            String time = obj.getTime();

            String firstLine = "";
            if(direction.equals("IN"))
            {
                firstLine ="Transakcja przychodząca \n " +"Od: " + from;
            }
            else if(direction.equals("OUT"))
            {
                firstLine ="Transakcja wychodząca \n"+ "Do: " +to;
            }

            String output_item = firstLine + "\n Id: "+ id+ "\n" + "Ilość "+ amount+ " \n"+ time+ "\n";
            output.add(output_item);
        }
    }

    private void getWalletInfo() {
        userId = preferences.getString("user_id", null);
        Call<WalletInfoResponseModel> call = walletService.getWallet(userId);
        call.enqueue(new Callback<WalletInfoResponseModel>() {
            @Override
            public void onResponse(Call<WalletInfoResponseModel> call, Response<WalletInfoResponseModel> response) {
                if (response.isSuccessful()) {
                    WalletInfoResponseModel userResponse = response.body();
                    transHistory = userResponse.getTransactionsHis();
                    showHistoryList();
                }
            }

            @Override
            public void onFailure(Call<WalletInfoResponseModel> call, Throwable t) {
                Toast.makeText(HistoryActivity.this, t.toString(), Toast.LENGTH_LONG).show();
            }
        });
    }

    public void goBackTWalletActivity(View view){
        Intent intent = new Intent(this, WalletActivity.class);
        startActivity(intent);
        finish();
    }

}