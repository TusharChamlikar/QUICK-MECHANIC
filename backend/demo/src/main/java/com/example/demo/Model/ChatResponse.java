package com.example.demo.Model;

public class ChatResponse {
    private String response;

    public ChatResponse(){}

    public ChatResponse(String response){
        this.response =response;
    }
    public String getResponse(){
        return response;
    }
    public void setResponse(String response){
        this.response=response;
    }
}
