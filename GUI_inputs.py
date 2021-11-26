import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.rowconfigure([0, 1], weight=1, minsize=100)
ROOT.columnconfigure(0, weight=1, minsize=100)

 # other relief options: tk.FLAT, tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE
frm_a = tk.Frame(master=ROOT, relief=tk.RAISED, width=50, borderwidth=2)
frm_b = tk.Frame(master=ROOT, relief=tk.RAISED, width=50, borderwidth=2)

#ROOT.withdraw()

lbl_a = tk.Label(
    text="Enter input",
    fg="black",  # Set the text color to white
    bg="white",  # Set the background color to black
    width=15, #measured in text units
    height=3,
    master=frm_a
)
lbl_a.pack(fill=tk.X, expand=True, padx=5, pady=5)

ent_a = tk.Entry(fg="black", bg="white", width=50, master=frm_a)
ent_a.pack(fill=tk.X, expand=True, padx=5, pady=5)
#entry.get()
#entry.delete(0, tk.END)
#entry.insert(0, "text")

lbl_b = tk.Label(
    text="More input",
    fg="black",  # Set the text color to white
    bg="white",  # Set the background color to black
    width=15, #measured in text units
    height=3,
    master=frm_b
)
lbl_b.pack(side= tk.LEFT, expand=True, padx=5, pady=5)

txt_b = tk.Text(master=frm_b)
txt_b.pack(side= tk.LEFT, expand=True, padx=5, pady=5)
#entry.get("1.0", tk.END) # get the character at line 1 and position 0 until the end of the text box
#entry.delete("1.0", tk.END)
#entry.insert("1.0", "text")

btn_done = tk.Button(
    text="Done",
    width=7,
    height=3,
    bg="white",
    fg="black",
)

frm_a.grid(row=0, column=0, padx=5, pady=5, sticky="nsew") # sticky "nsew" fill all available space, other option are: "n", "s", "e", "w" and all other combinations
frm_b.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
btn_done.place(x=0,y=350)

ROOT.mainloop()




# the input dialog
#USER_INP = simpledialog.askstring(title="Test",
#                                  prompt="What's your Name?:")

# check it out
#print("Hello", USER_INP)