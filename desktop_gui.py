import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import string
import random
import datetime
import json
import os

AUTHOR = "Ethan Bragdon"
VERSION = "Alpha 1.0.3"
SERVICE_FILE = "services.json"
ADMIN_PASSWORD = os.environ.get("NITRO_ADMIN_PW", "starfire")

# Load or initialize services
if os.path.exists(SERVICE_FILE):
    with open(SERVICE_FILE, "r") as f:
        SERVICES = json.load(f)
else:
    SERVICES = {
        "Discord Nitro": 16,
        "Steam Gift": 15,
        "Amazon Gift": 14,
        "Spotify Premium": 18
    }

def save_services():
    with open(SERVICE_FILE, "w") as f:
        json.dump(SERVICES, f, indent=2)

def generate_code(length: int) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class AdminPanel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("CodeGen Administration Panel")
        self.geometry("1920x1080")

        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda *args: self.refresh_list())
        self.search_entry = tk.Entry(self, textvariable=self.search_var)
        self.search_entry.pack(fill=tk.X, padx=10, pady=5)

        self.service_list = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.service_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        for name, length in SERVICES.items():
            self.service_list.insert(tk.END, f"{name} ({length})")

        controls = tk.Frame(self)
        controls.pack(fill=tk.X, padx=10, pady=5)

        self.new_name = tk.Entry(controls)
        self.new_name.insert(0, "New or Existing Service")
        self.new_name.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.new_length = tk.Entry(controls, width=5)
        self.new_length.insert(0, "16")
        self.new_length.pack(side=tk.LEFT, padx=2)

        tk.Button(controls, text="Add/Update", command=self.add_or_update_service).pack(side=tk.LEFT, padx=2)
        tk.Button(controls, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=2)
        tk.Button(controls, text="Delete All", command=self.delete_all).pack(side=tk.LEFT, padx=2)

    def add_or_update_service(self):
        name = self.new_name.get().strip()
        try:
            length = int(self.new_length.get())
        except ValueError:
            messagebox.showerror("Invalid", "Length must be a number.")
            return
        SERVICES[name] = length
        self.refresh_list()
        save_services()
        messagebox.showinfo("Saved", f"'{name}' set to length {length}.")

    def refresh_list(self):
        filter_text = self.search_var.get().lower()
        self.service_list.delete(0, tk.END)
        for name, length in SERVICES.items():
            if filter_text in name.lower():
                self.service_list.insert(tk.END, f"{name} ({length})")

    def remove_selected(self):
        selections = self.service_list.curselection()
        if not selections:
            return
        for index in reversed(selections):
            selected = self.service_list.get(index)
            name = selected.rsplit(" (", 1)[0]
            if name in SERVICES:
                del SERVICES[name]
        self.refresh_list()
        save_services()
        messagebox.showinfo("Removed", "Selected services removed.")

    def delete_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete ALL services?"):
            SERVICES.clear()
            self.refresh_list()
            save_services()
            messagebox.showinfo("Cleared", "All services have been deleted.")

class CodeGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"CodeGen {VERSION} By Ethan Bragdon (For Educational Purposes Only)")
        self.geometry("1920x1080")
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

        menubar = tk.Menu(self)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Packaging Info", command=self.show_packaging_info)
        admin_menu = tk.Menu(menubar, tearoff=0)
        admin_menu.add_command(label="Login", command=self.admin_login)
        menubar.add_cascade(label="Help", menu=help_menu)
        menubar.add_cascade(label="Admin", menu=admin_menu)
        self.config(menu=menubar)

    def show_about(self):
        about_text = (
            f"Gift Code Generator v{VERSION}\n"
            f"Author: {AUTHOR}\n"
            f"Date: 05/13/2025\n\n"
            "This is a simulation tool. Generated codes are not valid!"
        )
        messagebox.showinfo(title="About", message=about_text)

    def show_packaging_info(self):
        info = (
            "Packaging Instructions with PyInstaller:\n\n"
            "1. pip install pyinstaller\n"
            "2. pyinstaller --noconfirm --onefile --windowed --icon=nitro_icon.ico desktop_gui.py\n"
        )
        messagebox.showinfo(title="Packaging", message=info)

    def admin_login(self):
        pw = simpledialog.askstring("Admin Login", "Enter admin password:", show="*")
        if pw == ADMIN_PASSWORD:
            AdminPanel(self)
        else:
            messagebox.showerror("Access Denied", "Incorrect password.")

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
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'w') as f:
                    f.write("\n".join(codes))
                messagebox.showinfo(title="Saved", message=f"Codes saved to {file_path}")

if __name__ == "__main__":
    app = CodeGeneratorApp()
    app.mainloop()
