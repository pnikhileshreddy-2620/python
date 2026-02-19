from operator import concat
from tkinter import *
import time
import  math



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
TEXT='✔️'
timer=None

reps=0

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer,text='00:00')
    title_label.config(text='Timmer')
    checkmark.config(text=" ")
    global  reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps+=1

    long_break =LONG_BREAK_MIN*60
    short_break =SHORT_BREAK_MIN*60
    work_min =WORK_MIN*60

    if reps%8==0:
        title_label.config(text='LONG BREAK', fg=RED)
        count_down(long_break)

    elif reps%2==0:
        title_label.config(text='SHORT BREAK',fg=GREEN)
        count_down(short_break)
    else:
        title_label.config(text='WORKING ON TASK',fg=PINK)
        count_down(work_min)

    # if reps in[1,3,5,7]:
    #     count_down(WORK_MIN*60)
    #     reps +=1
    # elif reps in[2,4,6]:
    #     count_down(SHORT_BREAK_MIN*60)
    #     reps += 1
    # else:
    #     count_down(LONG_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """Dynamic typing in Python means that the type of a variable is determined at runtime,
     not during compilation, and can change throughout the program's execution."""
    count_min =math.floor(count/60)
    count_second =count%60
    if count_second<10:
        count_second =f'0{count_second}'
    # if count_second==0 or len(str(count_second))==1 :
    #     count_second='0'+str(count_second)
    canvas.itemconfig(text_timer,text=f'{count_min} : {count_second}')
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()

        mark=''
        working_session = math.floor(reps/2)
        for _ in range(working_session):
            mark +=TEXT

        checkmark.config(text=mark)

        # if reps==2:
        #     checkmark.grid(row=4, column=1)
        # elif reps==4:
        #     checkmark.grid(row=4, column=2)
        # elif reps==6:
        #     checkmark.grid(row=4, column=3)




# ---------------------------- UI SETUP ------------------------------- #
# canvas ,TK,PhotoImage,
window =Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)
fg=GREEN






title_label=Label(text=' Timer ',font=('Serif',25,'bold'),fg=fg,bg=YELLOW)

title_label.grid(row=0,column=1)

canvas =Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photoImage =PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=photoImage)

text_timer=canvas.create_text(103,130,text='00:00',fill='white',font=('Serif',35,'bold'))

canvas.grid(row=2,column=1)


start_button= Button(text='start',command=start_timer)
start_button.grid(row=4,column=0)

checkmark =Label(text=TEXT,fg=GREEN,bg=YELLOW)
checkmark.grid(row=4,column=1)

reset_button= Button(text='Reset',command=reset)
reset_button.grid(row=4,column=6)






window.mainloop()