from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=100,pady=100)

My_label = Label(text="Miles", font=("Arial",15,"bold"))
My_label.grid(column=2,row=0)

my_label1 = Label(text="is equal to", font=("Arial",15,"bold"))
my_label1.grid(column=0,row=1)

label_km = Label(text="Km", font=("Arial",15,"bold"))
label_km.grid(column=2,row=1)

def converter():
    user_data = int(input.get())
    ans = round(user_data*1.60,2)
    result.config(text=ans)

result = Label(text="", font=("Arial",15,"bold"))
result.grid(column=1,row=1)

input = Entry(width=20)
input.grid(column=1,row=0)


button = Button(text="Calculate", command=converter)
button.grid(column=1,row=2)







window.mainloop()