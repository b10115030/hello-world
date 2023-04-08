
import Private
import requests
# EventName='button_press'
# url=f'https://maker.ifttt.com/trigger/{EventName}/with/key/{Private.ifttt}?value1=25c&value2=70%&EventName={EventName}'

# r=requests.get(url)
# if r.status_code==200:
#     print('發送成功')



from gpiozero import Button
from signal import pause
from gpiozero import RGBLED,Buzzer

state = False
counter=0
EventName='button_press'

def user_press():
    global state,counter
    state = not state
    buzzer.on()
    if state == True:
        counter+=1
        print("開燈")
        led.color=(counter % 3 ==0 ,counter % 3 ==1,counter % 3 ==2)
        if counter % 3==0:
            
            url=f'https://maker.ifttt.com/trigger/{EventName}/with/key/{Private.ifttt}?value1=danger!!c&value2=100%&EventName={EventName}'

            r=requests.get(url)
            if r.status_code==200:
                print('發送成功')
    else:
        print("關燈")
        led.color=(0,0,0)


def user_release():
    buzzer.off()

button = Button(18)
buzzer= Buzzer(25)
led = RGBLED(red=17, green=27, blue=22)

button.when_pressed = user_press
button.when_released = user_release

pause()