import tkinter
window = tkinter.Tk()
window.title("shayan program")
window.minsize(500,300)


#label
label=tkinter.Label(text="hi im shayan",font=("Arial",24,"bold"))
label["text"]="new text"

label.pack()

#button
input=tkinter.Entry(width=100)
input.pack()
def button_clicked():
    label.config(text=input.get())
button=tkinter.Button(text="click button",command=button_clicked)
button.pack()

#entry
input=tkinter.Entry(width=100)
input.pack()
text=input.get()

#text entry
text_entry=tkinter.Text()
text_entry.pack()












window.mainloop()
