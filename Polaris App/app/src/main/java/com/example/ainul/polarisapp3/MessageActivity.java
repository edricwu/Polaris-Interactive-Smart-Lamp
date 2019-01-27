package com.example.ainul.polarisapp3;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.crashlytics.android.Crashlytics;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import io.fabric.sdk.android.Fabric;

public class MessageActivity extends AppCompatActivity {


    private ChatAdapter adapter;
    private ListView listView;
    private EditText message;
    public  String username;
    private TextView namedisplay;
    private DatabaseReference reference;
    private SharedPreferences pref;
    private SharedPreferences prefname;
    private String firebaseNode;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat_menu);




        //pref=getSharedPreferences(Constants.FILEEMOJI,MODE_PRIVATE);
        pref=getSharedPreferences(Constants.FILEEMOJI,MODE_PRIVATE);
        prefname=getSharedPreferences(Constants.FILE,MODE_PRIVATE);


        username=prefname.getString(Constants.TAG,"message username");
        firebaseNode=pref.getString(Constants.FirebaseUser,"Jane");
        //Log.d("TESTNAME","getting username, in message page///////////////////"+username);



        Toolbar toolbar = findViewById(R.id.toolbar);
        toolbar.setNavigationIcon(R.drawable.back);//image drawable for backbutton);

        setSupportActionBar(toolbar);
        getSupportActionBar().setDisplayShowTitleEnabled(false);

        toolbar.setNavigationOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(MessageActivity.this,MainMenu.class);
                startActivity(i);

            }
        });


        listView = findViewById(R.id.list);
        message = findViewById(R.id.message);

        namedisplay=findViewById(R.id.usernamedisplay);
        namedisplay.setText("Chat Room");

        ImageButton send = findViewById(R.id.send_message);


        adapter = new ChatAdapter(this, R.id.list);
        listView.setAdapter(adapter);



        ////////////////////////////////////////////////////////firebase initiating....///////////////////////////////////////////////////////////////////////
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        reference = database.getReference("chat");
            //Log.d("TEST","get user name from last page");
        reference.addChildEventListener(new ChildEventListener() {
            @Override
            public void onChildAdded(DataSnapshot dataSnapshot, String s) {
                ChatMessage msg = dataSnapshot.getValue(ChatMessage.class);
                adapter.add(msg);
                scrollToBottom();
            }
            public void onChildChanged(DataSnapshot dataSnapshot, String s) {}
            public void onChildRemoved(DataSnapshot dataSnapshot) {}
            public void onChildMoved(DataSnapshot dataSnapshot, String s) {}
            public void onCancelled(DatabaseError databaseError) {}
        });

            //Log.d("TEST","get user name from last page");
        send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                ChatMessage msg = new ChatMessage(username, message.getText().toString());
                reference.push().setValue(msg);
                message.setText("");
                scrollToBottom();
            }
        });


    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.chat_extras_send, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.xtra_colour) {
            startActivity(new Intent(this, OtherColourMenu.class));


            return true;
        }
        if (id == R.id.xtra_emoji) {
            startActivity(new Intent(this, XtraEmojiMenu.class));

            return true;
        }

        return super.onOptionsItemSelected(item);
    }


    protected void onPause(){
        super.onPause();




    }

    private void scrollToBottom() {
        listView.post(new Runnable() {
            @Override
            public void run() {
                listView.setSelection(adapter.getCount() - 1);
            }
        });
    }
}

