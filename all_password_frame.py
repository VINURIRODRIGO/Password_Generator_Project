import json
from tkinter import *
from tkinter import ttk, messagebox
import password

my_list = []
FONT = ("Arial", 12, "bold")
small_font = ("Arial", 10, "bold")
background_colour = "#000000"
foreground_colour = "#ffffff"
DARK_GREEN = "#007500"
BUTTON_FONT = ("Arial", 16, "bold")
gray = "#808080"
RED = "red"
ROWS, COLS = 100, 4  # Size of grid.
ROWS_LENGTH = 100  # Number of rows to display.
COLS_LENGTH = 4  # Number of columns to display.
p = ""
buttons_frame = ""
num = ""
f_name = ""
l_name = ""
sv = ""
count = 0
brake = False


def get_selected(event):
    selected = drop.get()
    if selected == "Auto-fill Password":
        password_box.config(fg=DARK_GREEN)
        password_box.delete(0, END)
        auto_password = password.Password().password()
        password_box.insert(0, auto_password)
    if selected == "Manual Password":
        password_box.delete(0, END)


# Displaying the records
def add_cells():
    global count, my_list
    my_list = []
    customer()
    update_button.config(state="normal")
    delete_button.config(state="normal")
    my_tree.tag_configure('odd_row', background="white", font=FONT)
    my_tree.tag_configure('even_row', background="lightblue", font=FONT)

    for record in my_list:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],
                                                                               record[3]),
                           tags=('even_row',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],
                                                                               record[3]),
                           tags=('odd_row',))
        count += 1


def all_passwords(destroyable_frame, my_screen, first_name, last_name, email):
    global f_name, l_name, my_list, my_tree, drop, \
        Email, website_box, email_box, password_box, no_box, drop, search_bar, update_button, delete_button
    f_name = first_name
    l_name = last_name
    my_list = []
    Email = email
    destroyable_frame.destroy()
    my_screen.geometry("950x650")

    # main Frame
    window = Frame(my_screen, bg=background_colour, width=400, height=400)
    window.grid(column=0, row=0)

    # Frame to Display button and entries
    add_frame = Frame(my_screen, bg=background_colour)

    # Add some style
    style = ttk.Style()
    # Pick a theme
    style.theme_use("default")
    # Configure our treeview colours

    style.configure("Treeview",
                    background=background_colour,
                    foreground=background_colour,
                    rowheight=25,
                    fieldbackground=background_colour,
                    font=FONT,
                    highlightthickness=0
                    )
    # Change selected colour
    style.map('Treeview',
              background=[('selected', 'blue')])
    first_frame = Frame(window, bg=background_colour)
    first_frame.pack(pady=20, ipadx=250)

    # Create a search bar
    search_bar = Entry(first_frame, font=FONT)
    search_bar.focus()
    search_bar.pack(side=RIGHT)
    search_label = Label(first_frame, text="Search", bg=background_colour, fg=foreground_colour, font=FONT)
    search_label.pack(side=RIGHT)

    # Create Treeview Frame
    main_frame = Frame(window)
    main_frame.pack(pady=20)

    tree_scroll = Scrollbar(main_frame)

    # Create Treeview
    my_tree = ttk.Treeview(main_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

    # Pack to the screen
    my_tree.pack()
    # Configure the scrollbar
    tree_scroll.config(command=my_tree.yview)
    my_tree['columns'] = ("No", "Website", "Email", "Password")
    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("No", anchor=CENTER, width=80)
    my_tree.column("Website", anchor=CENTER, width=130)
    my_tree.column("Email", anchor=CENTER, width=300)
    my_tree.column("Password", anchor=CENTER, width=180)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("No", text="No", anchor=CENTER)
    my_tree.heading("Website", text="Website", anchor=CENTER)
    my_tree.heading("Email", text="Email", anchor=CENTER)
    my_tree.heading("Password", text="Password", anchor=CENTER)

    # Buttons
    add_button = Button(add_frame, text="Add Record", command=add_record, font=small_font)
    add_button.grid(row=2, column=1, pady=50)

    update_button = Button(add_frame, text="Update Record", command=update_record, font=small_font)
    update_button.grid(row=2, column=2, pady=50)

    delete_button = Button(add_frame, text="Delete Record", command=delete_record, font=small_font)
    delete_button.grid(row=2, column=3, pady=50)

    back_button = Button(add_frame, text="Clear Records", command=clear_entries, font=small_font)
    back_button.grid(row=2, column=0, pady=50, padx=5)

    # Add data
    add_cells()

    add_frame.grid(column=0, row=1)

    # Entry boxes Labels
    nl = Label(add_frame, text="Website", bg=background_colour, fg=foreground_colour, font=FONT)
    nl.grid(row=0, column=0)
    il = Label(add_frame, text="Email", bg=background_colour, fg=foreground_colour, font=FONT)
    il.grid(row=0, column=1)
    tl = Label(add_frame, text="Password", bg=background_colour, fg=foreground_colour, font=FONT)
    tl.grid(row=0, column=2)

    # Entry boxes
    website_box = Entry(add_frame, font=FONT, justify=CENTER)
    website_box.grid(row=1, column=0, padx=10)
    email_box = Entry(add_frame, font=FONT, justify=CENTER)
    email_box.insert(0, Email)
    email_box.grid(row=1, column=1, padx=10, ipadx=40)
    email_box.config(state="disabled")
    password_box = Entry(add_frame, font=FONT, justify=CENTER)
    password_box.grid(row=1, column=2, padx=10)

    # Drop down Box
    drop = ttk.Combobox(add_frame, value=["Manual Password", "Auto-fill Password"], justify=LEFT, font=small_font,
                        width=17)
    drop.current(0)
    drop.grid(row=1, column=3, padx=10)
    drop.bind("<<ComboboxSelected>>", get_selected)

    # change the status of the update button and the delete button
    activate_and_deactivate_update_delete_buttons()

    my_tree.bind("<ButtonRelease-1>", clicker)
    note1 = Label(add_frame, text="* Green - Strong Password", bg=background_colour, fg=DARK_GREEN, font=FONT)
    note1.grid(row=3, column=0)
    note2 = Label(add_frame, text="* Red - Weak Password", bg=background_colour, fg=RED, font=FONT)
    note2.grid(row=4, column=0)
    # Displaying the current records
    get_data()
    # Adding and Displaying new records
    add_data()


# State of the update and delete buttons
def activate_and_deactivate_update_delete_buttons():
    customer()
    if len(my_list) != 0:
        update_button.config(state="normal")
        delete_button.config(state="normal")
    # when no records are available
    else:
        update_button.config(state="disabled")
        delete_button.config(state="disabled")


# display updated record
def update_record():
    if len(password_box.get()) > 0 and len(website_box.get()) > 0 and len(password_box.get()) > 0:
        # Grab record number
        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')
        # displaying the new data
        my_tree.item(selected, text="", values=(values[0], values[1], values[2], password_box.get()))
        # Update the file
        with open(f"Json_files/{f_name}_{l_name}.json", mode="r") as text:
            # getting the old data
            json_data = json.load(text)
        json_data[values[1]]["Email"] = values[2]
        json_data[values[1]]["Password"] = password_box.get()
        with open(f"Json_files/{f_name}_{l_name}.json", mode="w") as text_data:
            # getting the updated data
            json.dump(json_data, text_data, indent=4)
        # clear the entry boxes
        clear_entries()


def delete_record():
    # Grab record number
    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')
    try:
        # Update the file
        with open(f'Json_files/{f_name}_{l_name}.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        pass
    else:
        try:
            data.pop(values[1], None)
        except IndexError:
            pass
        else:
            with open(f'Json_files/{f_name}_{l_name}.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

            # Clear the entries
            website_box.configure(state="normal")
            website_box.delete(0, END)
            password_box.delete(0, END)
            data = my_tree.get_children()
            # Update the records
            for record in data:
                my_tree.delete(record)
            add_cells()
            add_data()
            # update the state of the update and delete button
            activate_and_deactivate_update_delete_buttons()


def search(data):
    c = 0
    # Clear all records
    for record in my_tree.get_children():
        my_tree.delete(record)
    my_tree.tag_configure('odd_row', background="white", font=FONT)
    my_tree.tag_configure('even_row', background="lightblue", font=FONT)
    for item in data:
        if item[0] % 2 == 0:
            my_tree.insert(parent='', index='end', iid=c, text="", values=(item[0], item[1], item[2],
                                                                           item[3]),
                           tags=('even_row',))
        else:
            my_tree.insert(parent='', index='end', iid=c, text="", values=(item[0], item[1], item[2],
                                                                           item[3]),
                           tags=('odd_row',))
        c += 1


def customer():
    try:
        with open(f'Json_files/{f_name}_{l_name}.json', 'r') as text_file:
            json_data = json.load(text_file)
    except FileNotFoundError:
        pass
    else:
        number = 0
        for key in json_data.keys():
            number += 1
            my_list.append([number, key, json_data[key]['Email'], json_data[key]['Password']])


# get the Selected Record to the entry boxes
def select_record():
    # Clear entry boxes
    password_box.config(fg=background_colour)
    # clear the entry boxes
    clear_entries()

    # Grab record number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # output to entry boxes

    website_box.insert(0, values[1])
    website_box.config(state="disabled")
    email_box.insert(0, values[2])
    email_box.config(state="disabled")
    password_box.insert(0, values[3])


def clicker(event):
    try:
        if len(my_list) != 0:
            select_record()
    except IndexError:
        pass


# Create function to check entry is in the cells
def search_bar_check(event):
    # grab what was typed
    my_list.clear()
    customer()
    typed = search_bar.get()
    if typed == "":
        for record in my_tree.get_children():
            my_tree.delete(record)
        add_cells()
    else:
        data = []
        for items in my_list:
            if typed.title() in items[1] and items not in data:
                data.append(items)
        search(data)


# Update list box with selected items
def get_data():
    customer()
    all_web_data = []
    for da in my_list:
        all_web_data.append(da)
    search_bar.bind("<KeyRelease>", search_bar_check)


def check_pass(event):
    typed = password_box.get()
    if typed != 0:
        if password.password_checker(typed):
            password_box.config(fg=DARK_GREEN)
        else:
            password_box.config(fg=RED)


# Add new data to the file
def add_data():
    password_box.bind("<KeyRelease>", check_pass)


# Add new records
def add_record():
    activate_and_deactivate_update_delete_buttons()
    website = website_box.get().capitalize()
    Password = password_box.get()
    data = {website: {
        "Email": Email,
        "Password": Password
    }}
    try:
        with open(f"Json_files/{f_name}_{l_name}.json", mode="r") as text:
            # getting the old data
            json_data = json.load(text)
        if len(Password) != 0 and len(website) != 0:
            if website not in json_data:
                # getting old data and adding the new data
                json_data.update(data)
                with open(f"Json_files/{f_name}_{l_name}.json", mode="w") as text_data:
                    # getting the updated data
                    json.dump(json_data, text_data, indent=4)
                # Delete all the existing records
                for record in my_tree.get_children():
                    my_tree.delete(record)
                # Update the records
                add_cells()
                # clear the entry boxes
                clear_entries()
            else:
                messagebox.showwarning(title="Duplicate websites", message="This website already exists")
                website_box.configure(state="normal")
                website_box.delete(0, END)
                password_box.delete(0, END)
                drop.current(0)
        else:
            messagebox.showerror(title="Missing fields", message="Please don't keep any filed empty")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # when the file is not created or when the file is empty
        with open(f"Json_files/{f_name}_{l_name}.json", mode="w") as text:
            json.dump(data, text, indent=4)
        # Update the records
        add_cells()
        # clear the entry boxes
        clear_entries()


# clear the entry boxes
def clear_entries():
    website_box.configure(state="normal")
    website_box.delete(0, END)
    website_box.focus()
    password_box.delete(0, END)
    drop.current(0)
