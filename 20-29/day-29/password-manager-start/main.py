from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip  # type: ignore
import json
# ---------------------------- SEARCH ------------------------------- #
def find_password(): 
    website = website_input.get()
    
    if website:
        try:
            with open("data.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showwarning(text="Unreal", message="No Data File Found")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(message=f'Email: {email}\nPassword: {password}')
            else:
                messagebox.showwarning(title="Error", message=f"No details for {website} exists.")
                
        
    
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = eu_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not website or not password:
        messagebox.showwarning(title="oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open ("data.json", 'r') as f:
                data=json.load(f)
                data.update(new_data)
        except:
            data = new_data

        with open ("data.json", 'w') as f:
            json.dump(new_data, f, indent=4)
    
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(column=2, row=1)

website = Label(text="Website:")
website.grid(column=1, row=2)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=2, row=2)

search = Button(text="Search", width=12, font=("Segoe UI", 10, "normal"), command=find_password)
search.grid(column=3, row=2)

eu = Label(text="Email/Username:")
eu.grid(column=1, row=3)

eu_input = Entry(width=35)
eu_input.insert(0, "kp25.online@gmail.com")
eu_input.grid(column=2, row=3, columnspan=2)

password = Label(text="Password:")
password.grid(column=1, row=4)

password_input = Entry(width=21)
password_input.grid(column=2, row=4)

g_pass = Button(text="Generate Password", width=12, font=("Segoe UI", 10, "normal"), command=generate_password)
g_pass.grid(column=3, row=4)

add = Button(text="Add", width=33, command=save)
add.grid(column=2, row=5, columnspan=2)

window.mainloop()