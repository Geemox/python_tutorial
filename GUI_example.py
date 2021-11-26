import tkinter as tk
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename

inputs = []

# Create an event handler
def increase():
    """Increase the displayed value by 1"""
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    """decrease the displayed value by 1"""
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

def clear():
    """clear all inputs"""
    ent_in1.delete(0, tk.END)
    ent_in2.delete(0, tk.END)
    ent_directory.delete(0, tk.END)
    ent_costInEuro.delete(0, tk.END)

def submit():
    """Save inputs and exit"""
    inputs.append(ent_in1.get())
    inputs.append(ent_in2.get())
    inputs.append(ent_directory.get())
    ROOT.destroy()

def dollar2euro():
    """Convert the value for dollars to euros and insert the
    result into lbl_result.
    """
    euros = ent_costInEuro.get()
    dollars = 1.12*float(euros)
    lbl_result["text"] = f"{round(dollars, 2)}" +' ' + u'\u0024'

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    ent_directory.insert(0, filepath)

# GUI setup
ROOT = tk.Tk()
ROOT.title("GUI example")
ROOT.columnconfigure(0, minsize=300, weight=1)

frm_info = tk.Frame(master=ROOT, relief=tk.SUNKEN, width=100, borderwidth=3)

lbl_in1 = tk.Label(text="input 1:", master=frm_info)
lbl_in1.grid(row=0, column=0, padx=2, pady=2, sticky="e")
ent_in1 = tk.Entry(width=50, master=frm_info)
ent_in1.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")

lbl_in2 = tk.Label(text="input 2:", master=frm_info)
lbl_in2.grid(row=1, column=0, padx=2, pady=2, sticky="e")
ent_in2 = tk.Entry(width=50, master=frm_info)
ent_in2.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

lbl_directory = tk.Label(text="File Path:", master=frm_info)
lbl_directory.grid(row=2, column=0, padx=2, pady=2, sticky="e")
ent_directory = tk.Entry(width=50, master=frm_info)
ent_directory.grid(row=2, column=1, padx=2, pady=2, sticky="nsew")
btn_dir = tk.Button(master=frm_info, text=u'\udcc1', command=open_file)
btn_dir.grid(row=2, column=2, padx=2, pady=2, sticky="w")

frm_num = tk.Frame(master=ROOT, relief=tk.FLAT)
btn_decrease = tk.Button(master=frm_num, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
lbl_value = tk.Label(master=frm_num, text="0")
lbl_value.grid(row=0, column=1, padx=2, pady=2)
btn_increase = tk.Button(master=frm_num, text="+", command=increase)
btn_increase.grid(row=0, column=2, padx=2, pady=2, sticky="nsew")

frm_conv = tk.Frame(master=ROOT, relief=tk.FLAT)
ent_costInEuro = tk.Entry(master=frm_conv, width=10)
lbl_euro = tk.Label(master=frm_conv, text=u'\u20ac')
ent_costInEuro.grid(row=0, column=0, sticky="e")
lbl_euro.grid(row=0, column=1, sticky="w")
btn_convert = tk.Button(master=frm_conv,text="\N{RIGHTWARDS BLACK ARROW}", command=dollar2euro)
lbl_result = tk.Label(master=frm_conv, text=u'\u0024')
btn_convert.grid(row=0, column=2, pady=10)
lbl_result.grid(row=0, column=3, padx=10)

frm_buttons = tk.Frame(master=ROOT, relief=tk.FLAT)
btn_clear = tk.Button(text="Clear", master=frm_buttons, command=clear)
btn_clear.pack(side=tk.RIGHT, padx=5, pady=5)
btn_submit = tk.Button(text="Submit", master=frm_buttons, command=submit)
btn_submit.pack(side=tk.RIGHT, padx=5, pady=5)


frm_info.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
frm_num.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
frm_conv.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
frm_buttons.grid(row=3, column=0, padx=5, pady=5, sticky="se")

ROOT.mainloop()