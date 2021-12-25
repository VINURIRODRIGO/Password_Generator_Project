import csv
import json
from tkinter import messagebox

small_font = ("Arial", 10, "bold")
FONT = ("Arial", 12, "bold")
background_colour = "#000000"
foreground_colour = "#ffffff"
DARK_GREEN = "#007500"
BUTTON_FONT = ("Arial", 10, "bold")
pressed_time = 0.0
NOW = 0.0
times_out = False
ok_clicked = False
varif_code = False
all_records = {}
frame_5 = ""
about_image = ""
frame_4 = ""


def secret_code(email_address):
    try:
        with open("Json_files/customer_data.json") as text_file:
            json_data = json.load(text_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found.")
        return "error"
    else:
        if email_address in json_data:
            return True, json_data[email_address]["First Name"]
        else:
            return False


def save_to_csv(email, code, started_time):
        with open("Json_files/otp_data.csv", mode="a") as text:
            text.write(f"{code},{email},{started_time}\n")

