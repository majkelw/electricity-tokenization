package com.example.mobileapp.api.model.response;

public class TransactionsHistoryResponseModel {

    private String id;
    private String from;
    private String to;
    private String amount;
    private String direction;
    private String time;

    public String getId(){
        return id;
    }
    public String getFrom() {
        return from;
    }

    public String getTo (){
        return to;
    }
    public String getAmount()
    {
        return amount;
    }
    public String getDirection()
    {
        return direction;
    }
    public String getTime()
    {
        return time;
    }

}
/*
   \"id\": \"0\",\n" +
            "        \"from\": \"e61f2885\",\n" +
            "        \"to\": \"4c94f6\",\n" +
            "        \"amount\": \"1.0\",\n" +
            "        \"direction\": \"IN\",\n" +
            "        \"time\": \"2023-05-31 20:29:38.2820479\"\n" +
 */