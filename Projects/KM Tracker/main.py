# Import Required Library
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import pandas as pd
from datetime import date, datetime


def open_popup():
    top = Toplevel(root)
    top.title("Toplam KM")
    top.minsize()
    Label(top, text=f"YTD Toplam {round(sum(df.KM))} km", font='Arial 18 bold').pack(padx=10, pady=5)
    Label(top, text=f"Son kayit {df.iloc[-1].Date} tarihinde {df.iloc[-1].KM} km",
          font='Arial 18 bold').pack(padx=10, pady=5)
    Button(top, text="Exit", command=top.destroy).pack(padx=10, pady=20)


def travel_date():
    if entry_km.get() == "":
        result.config(text=f"Mesafe girilmedi. Kayit yapilmadi.")
    elif entry_km.get() and reason_entry.get() == "":
        date_to_be_used = datetime.strptime(cal.get_date(), '%m/%d/%y')
        date_format = date_to_be_used.strftime("%d/%m/%Y")
        result.config(text=f"Sebepsiz bir {entry_km.get()} km kaydedildi. Tarih: {date_format}")
        entry_to_df = float(entry_km.get())
        reason_entry_to_df = reason_entry.get()
        df.loc[len(df.index)] = [date_format, entry_to_df, "Diger"]
        df.to_csv('data.csv', index=False)
    else:
        date_to_be_used = datetime.strptime(cal.get_date(), '%m/%d/%y')
        date_format = date_to_be_used.strftime("%d/%m/%Y")
        result.config(text=f"{reason_entry.get()} icin {entry_km.get()} km kaydedildi. Tarih: {date_format}")
        entry_to_df = float(entry_km.get())
        reason_entry_to_df = reason_entry.get()
        df.loc[len(df.index)] = [date_format, entry_to_df, reason_entry_to_df]
        df.to_csv('data.csv', index=False)


today = date.today()
df = pd.read_csv("data.csv")
# Create Object
root = Tk()
root.title("Mesafe kayit")
root.minsize()

# Creating Menubar
menubar = Menu(root)

# Adding Menu
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=menu)
menu.add_command(label='Toplam km', command=open_popup)
menu.add_separator()
menu.add_command(label='Exit', command=root.destroy)

# Add Calendar
cal = Calendar(root, selectmode='day', year=today.year, month=today.month, day=today.day)
cal.grid(column=0, row=0, columnspan=3, pady=20, )

# KM Label
km_label = Label(text="Mesafe (km)", font=("Arial", 12, "bold"))
km_label.grid(row=1, column=0)
km_label.config(padx=10)

# Miles Label
reason_label = Label(text="Sebep", font=("Arial", 12, "bold"))
reason_label.grid(row=1, column=1)
reason_label.config(padx=10)

# KM entry
entry_km = Entry(width=10, font='Verdana 12')
entry_km.grid(row=2, column=0, padx=10, pady=10)

# Reason for entry
reason_entry = ttk.Combobox(values=["Depo", "Paket teslimi", "Muhasebeci", "Etkinlik", "Diger"], font='Verdana 10')
reason_entry.grid(row=2, column=1, padx=10, pady=10)

# Add Button
Button(root, text="Kaydet", command=travel_date).grid(row=2, column=2, padx=10, pady=10)

# Result output below
result = Label(root, text="", font='Verdana 12')
result.grid(row=3, column=0, columnspan=3, pady=10)

root.config(menu=menubar)

# Execute Tkinter
root.mainloop()
