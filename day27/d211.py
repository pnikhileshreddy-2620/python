from tkinter import *

main = Tk()
main.title(string="TKINTER")
main.minsize(height=300,width=500)
# main.config(padx=200,pady=200)
main.config(padx=20,pady=20)
# Label

label =Label(text='LABEL')
label.config(text='LABEL CHANGED')
# label.pack()
# label.place(x=0,y=0)
label.grid(column=0,row=0)
label.config(padx=10,pady=10)
# Button

button =Button(main,text='click me')
# button.pack()
# button.place(x=0,y=33)
button.grid(row=1,column=1)
button.config(pady=10,padx=10)


button1 =Button(main,text='new button me')
button1.grid(row=0,column=2)
button1.config(padx=10,pady=10)


# Entry

entry =Entry(width=10)

# entry.place(x=0,y=70)
entry.grid(column=3,row=3)

print(entry.get())
# entry.pack()


''''
Tk,BUTTON,ENTRY,LABEL,PACK,PLACE,GRID

get()

'''
















main.mainloop()