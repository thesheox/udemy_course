import json
from random import choice,randint,shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_letter=[choice(letters) for a in range(randint(8, 10))]
    password_symbol=[choice(symbols) for a in range(randint(2, 4))]
    password_numbers=[choice(numbers) for a in range(randint(2, 4))]

    password_list=password_letter+password_numbers+password_symbol
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_for_account():
    website=website_entry.get()
    try:
        with open("data.json", mode="r") as writer:
            data = json.load(writer)
    except FileNotFoundError:
        messagebox.showinfo(title="data not found", message=f"there isnt any saved password")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="data not found",message=f"there isnt any password for this account ")




def save_data():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data={
        website_data:{
            "email":email_data,
            "password":password_data,
        }
    }

    if len(password_data)==0 or len(email_data)==0:
        messagebox.showinfo(title="nothing entered",message="you entered nothing")
    else:
        try:
            with open("data.json",mode="r") as writer:
                #json.dump(new_data,writer,indent=4)
                data=json.load(writer)

        except FileNotFoundError:
            with open("data.json", mode="w") as writer:
                json.dump(new_data,writer,indent=4)

        else:
            data.update(new_data)
            with open("data.json", mode="w") as writer:
                json.dump(data,writer,indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.config(padx=20,pady=50)
window.title("Pasword Manager")
canvas=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

#labels
website_label=Label(text="Website")
website_label.grid(row=1,column=0)

#labels
email_label=Label(text="Email/Username")
email_label.grid(row=2,column=0)

#labels
password_label=Label(text="Password")
password_label.grid(row=3,column=0)






#entry
website_entry=Entry(width=36)
website_entry.insert(END,string="")
website_entry.focus()
website_entry.grid(row=1,column=1)

#entry
email_entry=Entry(width=55)
email_entry.insert(END,string="thesheox@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

#entry
password_entry=Entry(width=36)
password_entry.grid(row=3,column=1)


#buttons
def generate_action():
    generate_password()
generate_button=Button(text="Generate Password",command=generate_action)
generate_button.grid(row=3,column=2)

#buttons
def search_action():
    search_for_account()
search_button=Button(text="Search",command=search_action,width=15)
search_button.grid(row=1,column=2)

#buttons
def add_action():
    save_data()

add_button=Button(text="Add",command=add_action,width=47)
add_button.grid(row=4,column=1,columnspan=2)










window.mainloop()
