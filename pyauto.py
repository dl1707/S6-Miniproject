from pyautogui import *
from time import *

#Display screen width,height and current mouse position
'''w,h=size()
x,y=position()
print("Height=",h," Width=",w)
print("Initially at X=",x," Y=",y)'''

#Automatic cursoring
'''print("Your mouse cursor will move in 10 seconds")
sleep(5)
moveTo(500,500)'''

#Automatic write
'''sleep(5)
write("Hello.....Mummy Mary D'Silva...Automated by python",interval=0.25)'''

#alert('Hello Mummy')

#Automatic drag
'''distance = 200
x=0
while distance > 0 and x<5:
    drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    drag(0, distance, duration=0.5)   # move down
    drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    drag(0, -distance, duration=0.5)  # move up
    x+=1'''

#Prompting
prompt("This is automatic python prompt")


