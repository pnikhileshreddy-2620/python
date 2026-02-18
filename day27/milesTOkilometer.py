from tkinter import *

''''
This code about converting miles to kilometer
'''

""""
used class in this code.

TK,BUTTON,LABEL,ENTRY,

user function to convert the miles to kilometer.

User need to entry only numeric value.

if user entry any string. Exception is not handled in program. It will crash code.

"""


def calculate_km():
    mile=entry.get()
    final =float(mile)*1.609
    print(final)
    
    

miles = Tk()
miles.minsize(height=100,width=100)
miles.title('Miles To kilometer Converter')
miles.config(padx=20,pady=20)
# miles.config(background='red')

entry =Entry(width=14)
entry.grid(column=14,row=10)
entry.config(bg='lightblue')
print(entry.get())

label =Label(text="Miles")
label.grid(column=18,row=10)

label1= Label(text="Equals to ")
label1.grid(row=15,column=4)

final_output =Label(width=10,text='0')
final_output.grid(column=14,row=15)

final_output.config(bg='lightblue')

label2 =Label(text='KM')
label2.grid(row=15,column=18)

def calculate_km():
    mile=entry.get()
    final =float(mile)*1.609
    # print(final)
    final_output.config(text=str(final))


button =Button(text="Calculate",command=calculate_km)
button.grid(row=17,column=14)










miles.mainloop()
