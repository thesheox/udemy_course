from tkinter import *

#new window
window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=400,height=150)
window.config(padx=10,pady=10)



#labels
label1=Label(text="Miles")
label1.config(padx=10,pady=10)
label1.grid(row=0,column=2)

#labels
label2=Label(text="is equal to")
label2.config(padx=10,pady=10)
label2.grid(row=1,column=0)

value=Label(text="0")
value.config(padx=10,pady=10)
value.grid(row=1,column=1)

label4=Label(text="Km")
label4.config(padx=10,pady=10)
label4.grid(row=1,column=2)

#buttons




#text
text=Text(height=1,width=10)
text.focus()
text.config(padx=10,pady=10)
#text start from line 1 and character 0 ->> 1.0

text.grid(row=0,column=1)

def action():
    data = text.get("1.0", END).strip()
    km=int(data)*1.6
    value.config(text=km)
button=Button(text="Calculate",command=action)
button.grid(row=2,column=1)






window.mainloop()