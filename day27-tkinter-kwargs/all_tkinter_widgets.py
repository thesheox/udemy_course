from tkinter import *

#new window
window=Tk()
window.title("widget examples")
window.minsize(width=500,height=500)
window.config(padx=100,pady=100)

#labels
label=Label(text="this is old text")
label.config(text="this is the new text")
label.grid(row=0,column=0)

#buttons
def action():
    print("do sth")

button=Button(text="click me",command=action)
button.grid(row=1,column=1)

#entry
entry=Entry(width=30)
entry.insert(END,string="some text")
print(entry.get())
entry.grid(row=4,column=4)
#text
text=Text(height=5,width=30)
text.focus()
text.insert(END,"this is the new text")
#text start from line 1 and character 0 ->> 1.0
print(text.get("1.0",END))
text.grid(row=1,column=2)

#spinbox
def spin_box():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10,width=5,command=spin_box)
# spinbox.pack()


#scale
def scale_data(value):
    print(value)

scale=Scale(from_=0,to=100,command=scale_data)
# scale.pack()


#checkbox
def check_box_data():
    print(check_state.get())

check_state=IntVar()
checkbutton=Checkbutton(text="is it on?",variable=check_state,command=check_box_data)
check_state.get()
# checkbutton.pack()

#radiobutton

def radio_data():
    print(radio_state.get())

radio_state=IntVar()
rd1=Radiobutton(text="option1",value=1,variable=radio_state,command=radio_data)
rd2=Radiobutton(text="option2",value=2,variable=radio_state,command=radio_data)
# rd1.pack()
# rd2.pack()


#listbox
def listbox_data(event):
    print(listbox.get(listbox.curselection()))
listbox=Listbox(height=4)
fruits=["apple","banana","orange","pear"]
for item in fruits:
    listbox.insert(fruits.index(item),item )
listbox.bind("<<ListboxSelect>>",listbox_data)
listbox.place(x=0,y=400)

window.mainloop()