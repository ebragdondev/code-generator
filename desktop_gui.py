import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import string
import random
import datetime
import os

AUTHOR = "Ethan Bragdon"
VERSION = "5.0.0"

def generate_code(length: int) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

SERVICES = {
    "Discord Nitro": 16,
    "Steam Gift": 15,
    "Amazon Gift": 14,
    "Spotify Premium": 18,
    **{f"Popular Service {i}": random.randint(12, 24) for i in range(1, 997)}
}

class CodeGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"Gift Code Generator v{VERSION}")
        self.geometry("750x600")
        self.configure(bg='#2e2e2e')

        style = ttk.Style(self)
        style.theme_use("clam")

        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Select Code Type:").grid(column=0, row=0, sticky=tk.W)
        self.code_type = tk.StringVar()
        self.type_combo = ttk.Combobox(main_frame, textvariable=self.code_type,
                                       values=sorted(SERVICES.keys()), state="readonly", width=50)
        self.type_combo.grid(column=1, row=0, sticky=tk.W)
        self.type_combo.current(0)

        ttk.Label(main_frame, text="Quantity:").grid(column=0, row=1, sticky=tk.W, pady=(10,0))
        self.quantity = tk.IntVar(value=1)
        self.qty_spin = ttk.Spinbox(main_frame, from_=1, to=1000, textvariable=self.quantity)
        self.qty_spin.grid(column=1, row=1, sticky=tk.W, pady=(10,0))

        self.save_var = tk.BooleanVar(value=False)
        self.save_check = ttk.Checkbutton(main_frame, text="Save codes to file", variable=self.save_var)
        self.save_check.grid(column=0, row=2, columnspan=2, sticky=tk.W, pady=(10,0))

        self.generate_btn = ttk.Button(main_frame, text="Generate", command=self.generate_codes)
        self.generate_btn.grid(column=0, row=3, columnspan=2, pady=20)

        ttk.Label(main_frame, text="Generated Codes:").grid(column=0, row=4, sticky=tk.W)
        self.text_box = tk.Text(main_frame, height=15, width=85, state=tk.DISABLED, bg="#1e1e1e", fg="white")
        self.text_box.grid(column=0, row=5, columnspan=2, pady=(5,0))

    def generate_codes(self):
        service = self.code_type.get()
        count = self.quantity.get()
        length = SERVICES.get(service, 16)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        codes = [f"[{timestamp}] {service}: {generate_code(length)}" for _ in range(count)]

        self.text_box.configure(state=tk.NORMAL)
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, "\n".join(codes))
        self.text_box.configure(state=tk.DISABLED)

        if self.save_var.get():
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'w') as f:
                    f.write("\n".join(codes))
                messagebox.showinfo(title="Saved", message=f"Codes saved to {file_path}")

if __name__ == "__main__":
    app = CodeGeneratorApp()
    app.mainloop()
