package com.example.mobileapp;

import java.io.IOException;

import okhttp3.HttpUrl;
import okhttp3.Interceptor;
import okhttp3.Request;
import okhttp3.Response;

class BaseUrlInterceptor implements Interceptor {

    private HttpUrl baseUrl;

    public BaseUrlInterceptor(String baseUrl) {
        this.baseUrl = HttpUrl.parse(baseUrl);
    }

    @Override
    public Response intercept(Chain chain) throws IOException {
        Request request = chain.request();
        HttpUrl url = request.url();

        // Skip URL reconstruction if we're hitting a local endpoint
        if (url.host().equals("10.0.2.2")) {
            return chain.proceed(request);
        }

        // Reconstruct the URL with the new base URL
        Request newRequest = request.newBuilder()
                .url(baseUrl.newBuilder()
                        .addEncodedPathSegments(url.encodedPath())
                        .build())
                .build();
        return chain.proceed(newRequest);
    }
}