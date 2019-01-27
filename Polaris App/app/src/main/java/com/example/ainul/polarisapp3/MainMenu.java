package com.example.ainul.polarisapp3;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import com.example.ainul.polarisapp3.Constants.*;

public class MainMenu extends AppCompatActivity {
    private String username="";
    private Button SwitchUser;

    private SharedPreferences pref;
    private SharedPreferences p;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu);

        p=getSharedPreferences(Constants.FILE,MODE_PRIVATE);

        pref=getSharedPreferences(Constants.FILE,MODE_PRIVATE);
        username=pref.getString(Constants.TAG,"");
        Log.d("TESTNAME",username+"/////////////");


        SwitchUser=findViewById(R.id.SwitchUser);
        SwitchUser.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(MainMenu.this,ChooseUser.class);
                startActivity(intent);
            }
        });

///////////////////////
        Button SetMyLampButton = findViewById(R.id.SetMyLampButton);
        SetMyLampButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainMenu.this, MyLampSettings.class);
                startActivity(intent);
            }
        });

        Button SeeMyMessagesButton = findViewById(R.id.SeeMyMessagesButton);
        SeeMyMessagesButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(username==""){
                    Toast.makeText(MainMenu.this, "Please give your lamp a name...", Toast.LENGTH_SHORT).show();
                    Intent intent = new Intent(MainMenu.this, UserNameSettingActivity.class);
                    startActivity(intent);
                }else{
                    Intent intent=new Intent(MainMenu.this,MessageActivity.class);
                    startActivity(intent);
                }

            }
        });
    }

    protected void onPause(){
        super.onPause();
        SharedPreferences.Editor preferencesEditor=pref.edit();
        preferencesEditor.putString(Constants.TAG,username);
        preferencesEditor.apply();
    }
}
