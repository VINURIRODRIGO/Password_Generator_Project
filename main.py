import csv
import json
import random
import smtplib
import time
from tkinter import *
from tkinter import messagebox
import pandas
import re

from change_password import ChangePassword
from forgot_password import secret_code, save_to_csv
from new_account import NewAccount, crate_new_account
from password import password_checker
from password_entry_field import PasswordData
from help_frame import help
from all_password_frame import all_passwords

pressed_time = 0.0
NOW = 0.0
times_out = False
ok_clicked = False
varif_code = False
all_records = {}
frame_5 = ""
frame_4 = ""
user_name_entry = ""
login_entry = ""
password_entry = ""
web_entry = 0
new_account = ""
user_password_entry = ""
conform_password_entry = ""
email = ""

small_font = ("Arial", 10, "bold")
FONT = ("Arial", 12, "bold")
Title_FONT = ("Arial", 30, "bold")
SUB_TITLE = ("Arial", 18, "bold")
background_colour = "#000000"
foreground_colour = "#ffffff"
DARK_GREEN = "#007500"
BUTTON_FONT = ("Arial", 10, "bold")
gray = "#808080"

first_n = ""
last_n = ""


def password_field(email_address):
    global about_image, first_n, last_n
    PasswordData(frame=frame_2, image=about_image, f_name=first_n, l_name=last_n, email_address=email_address)


def customer_user_name(username, password):
    try:
        with open("Json_files/customer_data.json") as text_file:
            json_data = json.load(text_file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="No Data File Found.")
        return "error"
    else:
        if username in json_data:
            if json_data[username]["Password"] == password:
                return True, json_data[username]["First Name"], json_data[username]["Last Name"], username
            else:
                return "password Error"
        if username not in json_data:
            return "not found"


def login_data():
    global user_name_entry, login_entry, first_n, last_n

    # validation
    if len(user_name_entry.get()) == 0 or len(login_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        login_customer = customer_user_name(user_name_entry.get(), login_entry.get())
        if login_customer != "error" and login_customer != "not found":
            if login_customer == "password Error":
                messagebox.showinfo(title="Oops", message="Wrong password! try again")
                login_entry.delete(0, END)
            elif login_customer[0]:
                frame_1.destroy()
                frame_2.grid(column=0, row=0)
                first_n = login_customer[1]
                last_n = login_customer[2]
                all_passwords(destroyable_frame=frame_1,
                              first_name=first_n,
                              my_screen=my_screen,
                              last_name=last_n, email=login_customer[3])
        if login_customer == "not found":
            login_entry.delete(0, END)
            user_name_entry.delete(0, END)
            messagebox.showerror(title="Not Found", message="Invalid login or password. Please try again.")


def register_data():
    frame_1.destroy()
    register()


def email_checker(email_address):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if not EMAIL_REGEX.match(email_address):
        return False
    return True


def password_confirmation():
    global frame_1, new_account
    user_name = new_account.email_address_entry.get()
    password = new_account.user_password_entry.get()
    conformation = new_account.conform_password_entry.get()
    first_name = new_account.F_name_entry.get()
    last_name = new_account.L_name_entry.get()

    if len(user_name) == 0 or len(conformation) == 0 or \
            len(password) == 0 or len(first_name) == 0 or len(last_name) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        invalid_data = Label(frame_3, text="",
                             justify="right", fg="red", font=FONT, bg=background_colour)
        invalid_data.grid(column=0, row=8, padx=5, sticky="ew", pady=10, columnspan=2)
        invalid = Label(frame_3, text="",
                        justify="right", fg="red", font=FONT, bg=background_colour)
        invalid.grid(column=1, row=9, padx=5, sticky="ew", pady=10, columnspan=2)
        if email_checker(email_address=user_name):
            if password == conformation:
                if password_checker(password):
                    status = crate_new_account(user_password=password,
                                               email_address=user_name,
                                               F_name=first_name.title(), L_name=last_name.title())
                    if status == "clear":
                        new_account.conform_password_entry.delete(0, END)
                        new_account.user_password_entry.delete(0, END)
                        new_account.email_address_entry.delete(0, END)
                        new_account.F_name_entry.delete(0, END)
                        new_account.L_name_entry.delete(0, END)
                    if status != "clear":
                        frame_3.destroy()
                        login_field()
                else:
                    invalid.config(text="")
                    invalid_data.config(text="Password Is Not Strong Enough. Try Again")
                    new_account.conform_password_entry.delete(0, END)
                    new_account.user_password_entry.delete(0, END)
            else:
                invalid.config(text="")
                invalid_data.config(text="Mismatching Passwords. Try Again")
                new_account.conform_password_entry.delete(0, END)
                new_account.user_password_entry.delete(0, END)

        else:
            invalid_data.config(text="")
            invalid.config(text="Invalid Email Address. Try Again")
            new_account.email_address_entry.delete(0, END)


def cancel():
    global frame_1
    frame_3.destroy()
    login_field()


def register():
    global frame_3
    frame_3 = Frame(my_screen, bg=background_colour, width=400, height=400)
    frame_3.grid(column=0, row=0)
    global about_image, conform_password_entry, user_password_entry, email, new_account

    # Creating new account screen
    new_account = NewAccount(image=about_image, frame=frame_3, main_screen=my_screen)
    new_account.registration_data()

    # Buttons for the new account
    sign_in__button = Button(frame_3, text="Next", command=password_confirmation, font=FONT, width="20"
                             )
    sign_in__button.grid(column=1, row=7, padx=5, sticky="ew", pady=10)
    sign_in__button = Button(frame_3, text="<< Back", command=cancel, font=FONT, width="20"
                             )
    sign_in__button.grid(column=0, row=7, padx=5, sticky="ew", pady=10)


def about():
    global about_image
    window = Toplevel(my_screen)
    # set the titlebar icon of the toplevel window
    photoImg = PhotoImage(file="images/new_logo_resize.png")
    window.iconphoto(False, photoImg)
    window.title("About PassReg")
    window.config(padx=20, pady=20, bg=background_colour)
    window.resizable(width=False, height=False)
    canvas = Canvas(window, width=189, height=189, highlightthickness=0, bg=background_colour)
    canvas.create_image(95, 95, image=about_image)
    canvas.grid(column=0, row=0)
    web_label = Label(window, text="PassReg\n\nBuild by Vinuri Rodrigo, built on July 27, 2021\nVersion: "
                                   "1.0.0\nWindows 10 Pro", justify="left", fg=foreground_colour, font=FONT,
                      bg=background_colour)
    web_label.grid(column=0, row=1, pady=(0, 5), ipady=5)
    reserved = Label(window, text="Copyright © 2021 PassReg. All rights reserved.\n", justify="left",
                     fg=foreground_colour, font=FONT, bg=background_colour)
    reserved.grid(column=0, row=2, pady=5)

    ok_button = Button(window, text="Exit", command=window.destroy, font=FONT)
    ok_button.grid(column=1, row=3, pady=30)


my_screen = Tk()
my_screen.title("PassReg")
my_screen.geometry("450x480")
my_screen.resizable(width=False, height=False)
my_screen.config(padx=20, pady=20, bg=background_colour)
menu_bar = Menu(my_screen)
frame_1 = Frame(my_screen, bg=background_colour, width=400, height=400)
frame_2 = Frame(my_screen, bg=background_colour, width=400, height=400)
frame_3 = Frame(my_screen, bg=background_colour, width=400, height=400)
view_frame = Frame(my_screen, bg=background_colour, width=400, height=400)
frame_1.grid(column=0, row=0)
about_image = PhotoImage(file="images/new_logo_resize.png")
join = PhotoImage(file="images/1st_step.png")
form = PhotoImage(file="images/password_record_screen.png")
# set the titlebar icon of tkinter window
photo = PhotoImage(file="images/new_logo_resize.png")
my_screen.iconphoto(False, photo)
# Creating Menu
file = Menu(menu_bar, tearoff=False)
# File section in the top bar menu
menu_bar.add_cascade(label='File', menu=file)
file.add_command(label='Exit', command=my_screen.quit)
help_ = Menu(menu_bar, tearoff=0)
# Help section in the top bar menu
menu_bar.add_cascade(label='Help', menu=help_)

# Documentation
help_.add_command(label='?Help', command=lambda: help(about_image=about_image, join=join, password_record_screen=form,
                                                      my_screen=my_screen))
help_.add_separator()

# About Us
help_.add_command(label='About', command=about)
my_screen.config(menu=menu_bar)


# Creating Forgot password Screen
def forgot():
    global frame_4, about_image, frame_5
    frame_1.destroy()
    frame_4 = Frame(my_screen, bg=background_colour, width=400, height=400)
    frame_5 = Frame(my_screen, bg=background_colour, width=400, height=400)
    Forgot(frame=frame_4, image=about_image, conform_frame=frame_5)


# Going to the login Screen
def go_back():
    global frame_4
    frame_4.destroy()
    login_field()


def change_go_back(email_address, conf_pass, password):
    global frame_5
    user_password = password.get()
    if conf_pass.get() == user_password:
        if password_checker(user_password):
            try:
                with open(f"Json_files/customer_data.json", mode="r") as text:
                    # getting the old data
                    json_data = json.load(text)
            except FileNotFoundError:
                messagebox.showerror(title="ERROR", message="System Error")
            else:
                if email_address in json_data:
                    json_data[email_address]["Password"] = user_password
                    with open(f"Json_files/customer_data.json", mode="w") as text_data:
                        # getting the updated data
                        json.dump(json_data, text_data, indent=4)
                        frame_5.destroy()
                        login_field()
        else:
            messagebox.showwarning(title="warning", message=f"The password is not strong enough.\n\n"
                                                            f"Please change the password....")
            conf_pass.delete(0, END)
            password.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Passwords are not matching")
        conf_pass.delete(0, END)
        password.delete(0, END)


def pressed(entry_code, user_email):
    global all_records, pressed_time, ok_clicked, frame_4

    # Getting the email address and the code entries
    input_entry_code = entry_code.get()
    input_email = user_email.get()

    data = pandas.read_csv("Json_files/otp_data.csv")
    customer_records = data.to_dict(orient="records")
    for _ in customer_records:
        all_records[_["secret code"]] = {"email address": _["email address"], "time": _["time"]}
    try:
        if all_records[int(input_entry_code)]["time"] + 2.00 >= float(time.strftime("%M:%S").replace(":", ".")) \
                and times_out is False and all_records[int(input_entry_code)]["email address"] == input_email:
            ok_clicked = True
            data = data.set_index("secret code")
            data = data.drop([int(input_entry_code)], axis=0)
            data.to_csv("otp_data.csv")
            frame_4.destroy()
            new_pass = ChangePassword(frame=frame_5, image=about_image, main_screen=my_screen)
            change_button = Button(frame_5, text="Save Password", width=13, justify=LEFT,
                                   command=lambda: change_go_back(email_address=input_email,
                                                                  conf_pass=new_pass.conf_new_password_entry,
                                                                  password=new_pass.new_password_entry), font=FONT)

            change_button.grid(column=1, row=4, pady=10)
    except KeyError:
        messagebox.showinfo(title="Oops", message="Invalid Code")
        entry_code.delete(0, END)
    if times_out is True:
        messagebox.showinfo(title="Times out", message="Time is Out")
        entry_code.delete(0, END)
        user_email.delete(0, END)


class Forgot:
    def __init__(self, frame, image, conform_frame):
        super().__init__()
        global frame_5, about_image, frame_4
        frame_4 = frame
        frame_5 = conform_frame
        about_image = image
        self.send = ""
        self.code_entry = ""
        self.user_name_entry = ""
        self.time_limit = ""
        self.verification_details()
        self.secret_code = 0

    # Generating a Verification code
    def generating_secret_code(self):
        code = random.randint(100000, 999999)

        # Adding the code number, email address and the current time to a csv file
        try:
            data = pandas.read_csv("Json_files/otp_data.csv")
            while code not in data.get("secret code").tolist():
                self.secret_code = code
                break
        except FileNotFoundError:
            with open("Json_files/otp_data.csv", mode="w", newline='') as a:
                data = csv.writer(a)
                data.writerow(["secret code", "email address", "time"])
            self.secret_code = code

    # Creating the email-body
    def letter_body(self, customer, user_email):
        with open("Json_files/Verification Code email.txt", mode="r") as letter:
            letter = letter.readlines()
            letter[0] = letter[0].replace("[name]", customer)
            letter[2] = letter[2].replace("[email]", user_email)
            self.generating_secret_code()
            letter[5] = letter[5].replace("[code]", f"{self.secret_code}")
            letter[10] = letter[10].replace("[email]", user_email)
            return letter

    def verification_details(self):
        global frame_4, verification_code, next_button

        # Frames
        frame_4.grid(column=0, row=0)
        canvas = Canvas(frame_4, width=189, height=189, highlightthickness=0, bg=background_colour)
        # Display Logo
        canvas.create_image(95, 95, image=about_image)
        canvas.grid(column=0, row=0, columnspan=2)

        # Labels
        user_name = Label(frame_4, text="Enter Email*: ", fg=foreground_colour, font=FONT, bg=background_colour,
                          justify="left")
        user_name.grid(column=0, row=1, pady=(0, 5), ipady=5)
        forgot_button = Button(frame_4, text="Send Code", command=self.waiting_list,
                               font=small_font)
        forgot_button.grid(column=2, row=1, padx=5, ipady=1, sticky="ew", pady=5)
        self.send = Label(frame_4, text="", fg=DARK_GREEN, font=FONT, bg=background_colour, justify="left")
        self.send.grid(column=0, row=2, pady=(0, 5), ipady=5, columnspan=2)
        verification_code = Label(frame_4, text="Enter code*: ", fg=foreground_colour, font=FONT,
                                  bg=background_colour, justify="left")
        verification_code.grid(column=0, row=4, pady=(0, 5), ipady=5)

        # Entries
        self.user_name_entry = Entry(frame_4, font=small_font)
        self.user_name_entry.grid(column=1, row=1, sticky="ew", ipady=5, pady=5)
        self.user_name_entry.focus()
        self.code_entry = Entry(frame_4, width=5, font=FONT)
        self.code_entry.config(state=DISABLED)
        self.code_entry.grid(column=1, row=4, sticky="ew", ipady=5, pady=5)

        # Buttons
        next_button = Button(frame_4, text="Next>>",
                             command=lambda: pressed(entry_code=self.code_entry,
                                                     user_email=self.user_name_entry),
                             font=small_font)
        next_button.config(state=DISABLED)
        next_button.grid(column=2, row=4, padx=5, ipady=1, sticky="ew", pady=5)
        cancel_button = Button(frame_4, text="<< Back", command=go_back, font=small_font)
        cancel_button.grid(column=0, row=5, padx=5, sticky="ew", pady=21)

    def waiting_list(self):
        global frame_4
        self.send.config(text="Please Wait....")
        frame_4.after(ms=1, func=lambda: self.code(self.user_name_entry.get()))

    def code(self, email_address):
        global NOW
        # ------------------------ Add your email address & the password---------------------------#
        # ----------- NOTE: Disable the less secure app access section of your email before sending emails. ---------- #
        my_email = 'your email address'
        password = "Email password"
        validate = secret_code(email_address)
        if validate != "error" and validate != False:
            if validate[0]:
                customer = secret_code(email_address)[1]
                msg = ""
                letter = self.letter_body(customer, email_address)
                for _ in letter:
                    msg += _
                # Sending the email to the user
                with smtplib.SMTP("smtp.gmail.com") as conf:
                    conf.starttls()
                    conf.login(user=my_email, password=password)
                    conf.sendmail(from_addr=my_email, to_addrs=email_address,
                                  msg=f"Subject:PassReg Verification Code\n\n{msg}")
                self.send.config(text="Email sent successfully")

                # Activate the next button  and code entry box
                next_button.config(state=NORMAL)
                self.code_entry.config(state=NORMAL)
                messagebox.showinfo(title="Time Limit", message="Please enter the verification code within 02 minutes")
                now = time.strftime("%M:%S")
                NOW = float(now.replace(":", "."))
                save_to_csv(email=email_address, code=self.secret_code, started_time=NOW)
                self.is_time_up()
        if validate is False:
            self.send.config(text="")
            messagebox.showerror(title="No Account", message=f"Sorry!\n\n{email_address} has no Account")
            self.user_name_entry.delete(0, END)

    def is_time_up(self):
        global times_out, NOW
        if float(time.strftime("%M:%S").replace(":", ".")) <= NOW + 2.00 and ok_clicked == False:
            times_out = False
            self.check_timer()
        # When time is out
        else:
            times_out = True
            self.send.config(text="")
            messagebox.showerror(title="Time is Out", message="Sorry the time is out please try again!")
            # deleting the record from the csv file
            data = pandas.read_csv("Json_files/otp_data.csv")
            data = data.set_index("secret code")
            data = data.drop([int(self.secret_code)], axis=0)
            data.to_csv("Json_files/otp_data.csv")
            self.user_name_entry.delete(0, END)
            self.code_entry.delete(0, END)

    # Check the time
    def check_timer(self):
        global frame_4
        frame_4.after(ms=1, func=self.is_time_up)


def login_field():
    global user_name_entry, login_entry, about_image, frame_1
    frame_1 = Frame(my_screen, bg=background_colour)
    my_screen.geometry("450x480")
    frame_1.grid(column=0, row=0, padx=20, pady=20)
    canvas = Canvas(frame_1, width=189, height=189, highlightthickness=0, bg=background_colour)
    canvas.create_image(94.5, 94.5, anchor=CENTER, image=about_image)
    canvas.grid(column=0, row=0, columnspan=2)

    # Labels
    user_name = Label(frame_1, text="Enter Username*: ", fg=foreground_colour, font=FONT, bg=background_colour)
    user_name.grid(column=0, row=1, pady=(0, 5), ipady=5)
    password = Label(frame_1, text="Password*: ", fg=foreground_colour, font=FONT, bg=background_colour)
    password.grid(column=0, row=2, pady=(0, 5), ipady=5)
    new_comers = Label(frame_1, text="New to PassReg?", fg=foreground_colour, font=FONT, bg=background_colour)
    new_comers.grid(column=0, row=4)

    # Entries
    user_name_entry = Entry(frame_1, font=FONT)
    user_name_entry.grid(column=1, row=1, sticky="ew", ipady=5, pady=5)
    user_name_entry.focus()
    login_entry = Entry(frame_1, font=FONT, show="*")
    login_entry.grid(column=1, row=2, sticky="ew", ipady=5, pady=5)

    # Buttons
    login_button = Button(frame_1, text="Sign In", command=login_data, font=small_font)
    login_button.place(x=270, y=286)
    forgot_button = Button(frame_1, text="Forgot Password", command=forgot, font=small_font)
    forgot_button.grid(column=0, row=3, pady=10)
    register_button = Button(frame_1, text="Join now", command=register,
                             font=small_font, fg="#FEFBF3", bg="#3282B8")
    register_button.place(x=180, y=320)


login_field()
my_screen.mainloop()
