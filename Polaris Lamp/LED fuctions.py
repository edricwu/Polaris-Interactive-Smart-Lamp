import RPi.GPIO as GPIO
from time import *
from firebase import firebase
import threading

button = 24
check_led = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(check_led,GPIO.OUT)

blue = GPIO.PWM(16,100)
green = GPIO.PWM(20,100)
red = GPIO.PWM(21,100)

pause_time = 0.02 

color_array = [0,0,0]

red.start(100)
blue.start(100)
green.start(100)

t1=0
count=1

color_timer=0
color_time_now=0
mode_timer=0
mode_time_now=0
status_timer=0
status_time_now=0

color=1
status=False
mode="normal"
button_end=False
button_count=0
on=False
change_mode=False
first=False
enter=False

Jane = '/Jane'
John = '/John'
Me = John
You = Jane
My_mode = '/John_mode'
Your_mode = '/Jane_mode'
My_status = '/John_status'
Your_status = '/Jane_status'

url='https://chat-d2fb5.firebaseio.com'
firebase = firebase.FirebaseApplication(url,None)

def check_color(timing,old):
    global color_timer
    global color_time_now
    color_time_now=time()
    if color_time_now-color_timer>timing:
        color_timer=color_time_now
        #GPIO.output(check_led,1)    
        new = firebase.get(Me,None)
        if new != old:
            #GPIO.output(check_led,0)
            return new
        #GPIO.output(check_led,0)
        return old
    return old

def check_mode(timing,old):
    global mode_timer
    global mode_time_now
    mode_time_now=time()
    if mode_time_now-mode_timer>timing:
        mode_timer=mode_time_now
        GPIO.output(check_led,1)    
        new = firebase.get(My_mode,None)
        if new != old:
            GPIO.output(check_led,0)
            return new
        GPIO.output(check_led,0)
        return old
    return old

def check_status(timing,old):
    global status_timer
    global status_time_now
    status_time_now=time()
    if status_time_now-status_timer>timing:
        status_timer=status_time_now
        #GPIO.output(check_led,1)    
        new = firebase.get(Your_status,None)
        if new != old:
            #GPIO.output(check_led,0)
            return new
        #GPIO.output(check_led,0)
        return old
    return old

def change_rgb(color_array):
    red.ChangeDutyCycle(color_array[0])
    green.ChangeDutyCycle(color_array[1])
    blue.ChangeDutyCycle(color_array[2])
    
def convert_rgb(color):
    rVal = 65536
    gVal = 256
    bVal = 1
    color_array[0] = change_range(int(color/rVal))
    color_array[1] = change_range(int((color%rVal)/gVal))
    color_array[2] = change_range(int(((color%rVal)%gVal)/bVal))
    return color_array

def change_range(num):
    oldMax = 255
    oldMin = 0
    newMax = 0
    newMin = 100
    oldRange = (oldMax - oldMin)
    newRange = (newMax - newMin)
    return (((num - oldMin)*newRange)/oldRange) + newMin

def play_pattern(s):
    if(type(s)!=int):
        if(s=='default'):
            default()
        elif(s=='angry'):
            angry()
        elif(s=='cry'):
            cry()
        elif(s=='busy'):
            busy()
        elif(s=='love'):
            love()
        elif(s=='party'):
            party()
        elif(s=='sick'):
            sick()
        elif(s=='sleepy'):
            sleepy()
        elif(s=='happy'):
            happy()
        elif(s=='1'):
            state_1()
        elif(s=='2'):

            state_2()
        elif(s=='3'):
            state_3()
        else:
            default()
    else:
        print(s)
        change_rgb(convert_rgb(s))
        
def default():
    if(default.state):
        default.color += 1
        default.color *= 4
        default.color -= 1
        if (default.color == 65280 or default.color == 16711680):
            default.color2 = default.color
            default.color=0
        if(default.color == 16777215):
            default.state = False
    else:
        default.color += 1
        default.color /= 4
        default.color -= 1
        if(default.color == 0):
            default.state = True
    print(default.color)
    change_rgb(convert_rgb(default.color+default.color2))
        
default.color = 0
default.color2 = 0
default.state = True
                
def angry():
    if(angry.state):
        change_rgb(convert_rgb(angry.color1))
        angry.state = False
    else:
        change_rgb(convert_rgb(angry.color2))
        angry.state = True
    print("angry")
angry.color1= 16138303
angry.color2= 13767443

angry.state = True
    
def cry():
    if(cry.state):
        change_rgb(convert_rgb(cry.color))
        cry.state = False
    else:
        change_rgb(convert_rgb(0))
        cry.state = True
    print("cry")
cry.color= 149336
cry.state = True
    
def busy():
    change_rgb(convert_rgb(busy.color))
    print("busy")
busy.color= 16097024

def love():
    change_rgb(convert_rgb(love.color))
    print("love")
love.color= 15895474
    
def party():
    change_rgb(convert_rgb(party.color))
    print("party")
party.color= 10513131
    
def sick():
    change_rgb(convert_rgb(sick.color))
    print("sick")
sick.color= 8421376

def sleepy():
    change_rgb(convert_rgb(sleepy.color))
    print("sleepy")
sleepy.color= 4416472

def happy():
    change_rgb(convert_rgb(happy.color))
    print("happy")
happy.color= 16240432

def state_1():
    change_rgb(convert_rgb(state_1.color))
    print("state_1")
state_1.color= 16711680

def state_2():
    change_rgb(convert_rgb(state_2.color))
    print("state_2")
state_2.color= 65280

def state_3():
    change_rgb(convert_rgb(state_3.color))
    print("state_3")
state_3.color= 255

def normal_press():
    global t1
    global count
    global button_end
    global button_count
    global change_mode
    state=0
    while True:
        button_state = GPIO.input(button)
        if button_state == GPIO.LOW:
            if state==0:
                t=time()
                if t1!=0:
                    if t-t1<0.3:
                        if count<3:
                            count+=1
                    else:
                        count=1
                t=time()
                state=1
        else:
            if state==1:
                t1=time()
                button_end=True
                print (t1-t)
                if t1-t>2:
                    change_mode = True
                    button_count = 4
                    count = 1
                else:
                    button_count = count
                print (button_count)
            break

def recording_pressx(colorx):
    state=0
    global mode
    global change_mode
    while True:
        button_state=GPIO.input(button)
        if button_state == GPIO.LOW:
            if state==0:
                trec=time()
                #play_pattern(1111)
                print ("AAA")
                state=1
        else:
            if state==1:
                if time()-trec>2:
                    mode="normal"
                    change_mode=True
                state=0
                break

def recording_press():
    global t1
    global on
    global button_end
    global change_mode
    global first
    state=0
    while True:
        button_state = GPIO.input(button)
        if button_state == GPIO.LOW:
            if state==0:
                t=time()
                on=True
                first=True
                state=1
        else:
            if state==1:
                on=False
                print ("X")
                first=True
                t1=time()
                if t1-t>2:
                    change_mode=True
            break

def listening_press():
    global change_mode
    if GPIO.input(button) == GPIO.LOW:
        change_mode = True

def button_mode(true):
    global mode
    global color
    if mode == "normal":
        normal_press()
    elif mode == "record":
        recording_press()
    elif mode == "listen":
        listening_press()
        
def normal_mode():
    global color
    global button_end
    global change_mode
    global mode
    global enter
    color = check_color(0,color)
    play_pattern(color)
    if button_end:
        if change_mode:
            mode="record"
            change_mode=False
            enter=True
            firebase.put('',My_mode,mode)
            firebase.put('',Your_mode,"listen")
        if time()-t1>1:
            button_end=False
            GPIO.output(check_led,1)  
            print ("Sending to Firebase")
            if button_count != 4:
                firebase.put('',You,str(button_count))
            GPIO.output(check_led,0)
            
def recording_mode():
    global mode
    global change_mode
    global first
    global on
    global enter

    global color
    print (on,first)
    if enter:
        color = "happy"
        enter=False
        play_pattern(0)
        print (11)
    if not on and first:
        play_pattern(0)
        first=False
        firebase.put('',My_status,on)
    if on and first:
        play_pattern(color)
        first=False
        firebase.put('',My_status,on)
    if change_mode:
        mode="normal"
        change_mode = False
        firebase.put('',My_mode,mode)
        firebase.put('',Your_mode,mode)

def listening_mode():
    global change_mode
    global color
    global status
    #color = check_color(5,color)
    status = check_status(0,status)
    print (status)
    
    if status:
        play_pattern("happy")
    elif not status:
        play_pattern(0)
    if change_mode:
        mode="normal"
        change_mode = False
        firebase.put('',My_mode,mode)
        firebase.put('',Your_mode,mode)
        
GPIO.add_event_detect(button, GPIO.BOTH, callback=button_mode, bouncetime=300)
    
try:
    firebase.put('',Me,'default')
    firebase.put('',My_mode,'normal')
    firebase.put('',Your_mode,'normal')
    GPIO.output(check_led,0)
    while True:
        if mode == "normal" or mode == "listen":
            mode = check_mode(1,mode)
            if mode=="normal":
                normal_mode()
            elif mode=="record":
                recording_mode()
            elif mode=="listen":
                listening_mode()
        else:
            mode = check_mode(5,mode)
            if mode=="normal":
                normal_mode()
            elif mode=="record":
                recording_mode()
            elif mode=="listen":
                listening_mode()

except KeyboardInterrupt:
    GPIO.cleanup()          # clean up GPIO on CTRL+C exitwhile True:


