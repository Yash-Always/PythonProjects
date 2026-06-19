import tkinter as tk
import time
import math

# window and clock dimensions
WIDTH , HEIGHT = 500 , 500
CENTER_X , CENTER_Y = WIDTH//2 , HEIGHT//2
RADIUS = 225


def update_clock():
    canvas.delete("hands") #to clear the previous hands position 

    current_time = time.localtime()
    hours = current_time.tm_hour % 12    # %operator to convert 24-hr system into 12-hr system
    minutes = current_time.tm_min 
    seconds = current_time.tm_sec 

    # coverting time into angles (radians) for the hands of the clock
    sec_angle = math.radians(90- (seconds * 6)) # 360/60 = 6 degree movement per second
    min_angle = math.radians(90 - (minutes *6 + seconds* 0.1)) # 360/60 = 6 degree movement per min and 6/60 =0.1 degree movement per sec 
    hour_angle = math.radians(90 - (hours * 30 + minutes * 0.5)) # 360/12 = 30 degree movement per hour and 30/60 = 0.5 movement per minute 
    

    # for second hand
    sec_x = CENTER_X + (RADIUS -40)* math.cos(sec_angle)
    sec_y = CENTER_Y - (RADIUS -40)* math.sin(sec_angle)
    canvas.create_line(CENTER_X , CENTER_Y , sec_x , sec_y , width=3 , fill="red" , tags= "hands")



    # for minute hand
    min_x = CENTER_X + (RADIUS - 60)* math.cos(min_angle)
    min_y = CENTER_Y - (RADIUS - 60)* math.sin(min_angle)
    canvas.create_line(CENTER_X , CENTER_Y , min_x , min_y , width=4 , fill="blue" , tags="hands")


    # for hour hand
    hour_x = CENTER_X +(RADIUS - 90)* math.cos(hour_angle)
    hour_y = CENTER_Y -(RADIUS - 90)* math.sin(hour_angle)
    canvas.create_line(CENTER_X , CENTER_Y , hour_x , hour_y , width=6 , fill="black" , tags="hands")


    root.after( 1000 , update_clock) # tells program to call the function update_clock after every 1000 milliseconds


# WINDOW LAYOUT/CREATION
root =tk.Tk() #creates main window , root is our window's variable name 
root.title("Analog clock") 
root.geometry(f"{WIDTH}x{HEIGHT}") # size of the window
root.resizable( False , False) # to prevent resizing of the window
    
# setting canvas for drawing the clock
canvas = tk.Canvas( root , width=WIDTH , height=HEIGHT , bg="white")
canvas.pack()


# outer rim 
canvas.create_oval( CENTER_X - RADIUS , CENTER_Y - RADIUS , CENTER_X + RADIUS , CENTER_Y + RADIUS , width = 4 , fill="yellow")


# to display the numbers on the clock
for i in range(1,13):
    angle = math.radians(90 - (i*30))  # as 30 degree movement per hour
    num_x = CENTER_X + (RADIUS - 50)* math.cos(angle)
    num_y = CENTER_Y - (RADIUS - 50)* math.sin(angle)
    canvas.create_text(num_x , num_y , text=str(i) , font=( "Arial" , 26 , "bold"))
    

# the centre of the clock that's holding the hands
canvas.create_oval(CENTER_X - 10 , CENTER_Y - 10 , CENTER_X+ 10, CENTER_Y + 10, fill="grey")


update_clock()  # to start the clock and update it every second 
root.mainloop() #to keep the window running



    