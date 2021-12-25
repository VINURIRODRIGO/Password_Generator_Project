import json
from tkinter import *
from tkinter import messagebox
import pyperclip
from password import Password
from save_password import SavePassword

FONT = ("Arial", 12, "bold")
background_colour = "#000000"
foreground_colour = "#ffffff"
DARK_GREEN = "#007500"
BUTTON_FONT = ("Arial", 10, "bold")


class PasswordData:
    def __init__(self, frame, image, f_name, l_name, email_address):
        self.frame_2 = frame
        self.image = image
        self.email = email_address
        self.copied_password = Label(self.frame_2, text="", justify="center", fg=background_colour, font=FONT,
                                     bg=background_colour)
        self.web_entry = Entry(self.frame_2, width=20, font=FONT)
        self.email_entry = Entry(self.frame_2, width=35, font=FONT)
        self.password_entry = Entry(self.frame_2, width=20, font=FONT)
        self.first_name = f_name
        self.L_name = l_name
        self.entry_data_ui()

    def entry_data_ui(self):
        # ---------------------------- UI SETUP ------------------------------- #
        canvas_1 = Canvas(self.frame_2, width=200, height=200, highlightthickness=0, bg=background_colour)
        canvas_1.create_image(100, 100, image=self.image)
        canvas_1.grid(column=1, row=1)

        welcome_label = Label(self.frame_2, text=f"Hello {self.first_name} {self.L_name}", justify="left",
                              fg="red", font=FONT, bg=background_colour)
        welcome_label.grid(column=2, row=0)

        web_label = Label(self.frame_2, text="Website:", justify="left", fg=foreground_colour, font=FONT,
                          bg=background_colour)
        web_label.grid(column=0, row=2, pady=(0, 5), ipady=5)

        password_label = Label(self.frame_2, text="Password:", justify="left", fg=foreground_colour, font=FONT,
                               bg=background_colour)
        password_label.grid(column=0, row=4, pady=(0, 5), ipady=5)

        email_label = Label(self.frame_2, text="Email/Username:", justify="left", fg=foreground_colour, font=FONT,
                            bg=background_colour)
        email_label.grid(column=0, row=3, pady=(0, 5), ipady=5)

        self.copied_password.grid(column=1, row=6, pady=(0, 5), ipady=5)

        self.web_entry.grid(column=1, row=2, sticky="ew", ipady=5)
        self.web_entry.focus()

        self.email_entry.grid(column=1, row=3, columnspan=2, sticky="ew", ipady=5)
        self.email_entry.insert(0, self.email)

        self.password_entry.grid(column=1, row=4, sticky="ew", ipady=5)

        generate_password = Button(self.frame_2, text="Generate Password", justify="left", fg="white", font=BUTTON_FONT,
                                   bg="#808080",
                                   command=self.generating_password)
        generate_password.grid(column=2, row=4, padx=5, ipady=1, sticky="ew", pady=5)

        add = Button(self.frame_2, text="Add", width=35, justify="left", fg="white", font=BUTTON_FONT, bg="#808080",
                     command=self.save)
        add.grid(column=1, row=5, columnspan=2, sticky="ew")

        find = Button(self.frame_2, text="Find", justify="left", fg="white", font=BUTTON_FONT, bg="#808080",
                      command=self.find_password)
        find.grid(column=2, row=2, padx=5, ipady=1, sticky="ew", pady=5)

        clear = Button(self.frame_2, text="Clear", justify="left", fg="white", font=BUTTON_FONT, bg="#808080",
                       command=self.clear_all)
        clear.grid(column=1, row=7, padx=5, ipady=1, sticky="ew", pady=5)

    def generating_password(self):
        old_password = self.password_entry.get()
        if len(old_password) != 0:
            self.password_entry.delete(0, END)
        password_generator = Password()
        new_password = password_generator.password()
        self.password_entry.insert(0, new_password)
        pyperclip.copy(new_password)
        self.copied_password.config(text="✔  Password copied", fg=DARK_GREEN)

    # ----------------------------- FIND ---------------------------------------- #
    def find_password(self):
        website = self.web_entry.get().capitalize()
        try:
            with open(f"Json_files/{self.first_name}_{self.L_name}.json") as text_file:
                json_data = json.load(text_file)
        except FileNotFoundError:
            messagebox.showinfo(title="ERROR", message="No Data File Found.")
        else:
            if website in json_data:
                email = json_data[website]["Email"]
                old_password = json_data[website]["Password"]
                self.email_entry.delete(0, END)
                self.email_entry.insert(0, email)
                self.password_entry.insert(0, old_password)
                pyperclip.copy(old_password)
                self.copied_password.config(text="✔  Password copied", fg=DARK_GREEN)
                messagebox.showinfo(title=website, message=f"Email: {email}\n\nPassword: {old_password}")
            else:
                messagebox.showinfo(title="ERROR", message=f"No Details for {website} exists.")

    def clear_all(self):
        self.web_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.email_entry.insert(0, self.email)
        self.copied_password.config(text="", fg=background_colour)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save(self):
        website = self.web_entry.get().capitalize()
        username = self.email_entry.get()
        check_password = self.password_entry.get()
        save_password = SavePassword(website=website, username=username, password=check_password,
                                     first_name=self.first_name, last_name=self.L_name)
        save_password.json_data()
