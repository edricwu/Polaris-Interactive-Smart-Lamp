# Polaris-Interactive-Smart-Lamp
A night lamp with additional communicative features designed to ease and encourage trivial communications with loved ones.

Polaris Set-up Instructions

App set-up:
1.	Install the app on your android device.
2.	Open the app and go to change user tab to “select users tab”
3.	Select which user you want to be. If you select “John” then messages will be set to Lamp “Jane” and you’ll be able to control the Lamp “John”. Vice-versa.
4.	Choose a user name and then click on save button. 
5.	You’ll be redirected to “See My Messages” tab. Here you can either send text message or send emoji but clicking on the emoji button on top right corner which will be reflected on other user’s lamp or select a customized color but click on the color pallet button also on the top right corner.
6.	Press back button to go to the main menu. 
7.	Click on “Set My Lamp” tab control the lamp settings.

Lamp set-up:
1.	To test the lamp, you’ll need 2 Raspberry Pi, 2 common cathode RGB led and 1 push button.
2.	One terminal of the button will be connected to ground and the other will be connect to GPIO 24 of RPi.
3.	Common terminal of RGB led will be connected to 3.3v of RPi, red green and blue terminal of RGB led will be connected to GPIO 21, 20 and 16 of RPi respectively. 
4.	To use the lamp as either Jane or John, we need to make minor changes to the code itself. 
•	Read Set-up instructions for further details
5.	After Turning on the Lamp, the lamp can detect 4 different states. 
•	Single press: Changes the other lamps color to red.
•	Double press: Changes the other lamps color to green.
•	Triple press: Changes the other lamps color to blue.
•	Long press (2 sec): Change to Lamp to recording mode and other Lamp to Listening mode. So, if Lamp in listening mode will follow the button presses of the Lamp in recording mode. To exit the mode, either the Lamp in recording mode  Long press again or the Lamp in listening mode press the button once.  

