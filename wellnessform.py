import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd

class WellnessLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Wellness Entry Logger")
        self.editing_item = None  

        input_frame = tk.Frame(root, padx=10, pady=10)
        input_frame.pack(fill='x')

        tk.Label(input_frame, text="Student Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Mental Wellness Activity:").grid(row=1, column=0, sticky="w")
        self.mental_entry = tk.Entry(input_frame)
        self.mental_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Me-Time Activity:").grid(row=2, column=0, sticky="w")
        self.me_time_entry = tk.Entry(input_frame)
        self.me_time_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Screen-Free Time (min):").grid(row=3, column=0, sticky="w")
        self.screen_time_entry = tk.Entry(input_frame)
        self.screen_time_entry.grid(row=3, column=1, padx=5, pady=5)
        self.screen_time_entry.bind("<FocusOut>", lambda e: self.update_status())

        self.status_label = tk.Label(input_frame, text="Status: ")
        self.status_label.grid(row=4, column=0, padx=5, pady=5)

        button_frame = tk.Frame(root, pady=5)
        button_frame.pack()

        tk.Button(button_frame, text="Add Entry", command=self.add_entry).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Delete Selected Entry", command=self.delete_entry).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Clear All", command=self.clear_all).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Save to Excel", command=self.save_to_excel).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Edit Selected Entry", command=self.edit_entry).grid(row=0, column=4, padx=5)

        self.tree = ttk.Treeview(root, columns=("Name", "Mental", "Me-Time", "Screen-Free", "Status"), show='headings')
        for col in ("Name", "Mental", "Me-Time", "Screen-Free", "Status"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        self.tree.pack(padx=10, pady=10)

    def update_status(self):
        try:
            minutes = int(self.screen_time_entry.get())
            status = "Healthy" if minutes >= 60 else "Needs More Me-Time"
            self.status_label.config(text=f"Status: {status}")
        except:
            self.status_label.config(text="Status: Invalid input")

    def add_entry(self):
        name = self.name_entry.get().strip()
        mental = self.mental_entry.get().strip()
        me_time = self.me_time_entry.get().strip()
        screen_time = self.screen_time_entry.get().strip()

        if not name or not mental or not me_time or not screen_time:
            messagebox.showerror("Input Error", "All fields must be filled.")
            return
        try:
            minutes = int(screen_time)
            if minutes < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Screen-Free Time must be a positive number.")
            return

        status = "Healthy" if minutes >= 60 else "Needs More Me-Time"

        if self.editing_item:
            self.tree.item(self.editing_item, values=(name, mental, me_time, minutes, status))
            messagebox.showinfo("Success", "Entry updated successfully.")
            self.editing_item = None
        else:
            self.tree.insert("", "end", values=(name, mental, me_time, minutes, status))
            messagebox.showinfo("Success", "Entry added successfully.")

        self.name_entry.delete(0, tk.END)
        self.mental_entry.delete(0, tk.END)
        self.me_time_entry.delete(0, tk.END)
        self.screen_time_entry.delete(0, tk.END)
        self.status_label.config(text="Status: ")

    def delete_entry(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an entry to delete.")
            return
        for item in selected:
            self.tree.delete(item)
        messagebox.showinfo("Deleted", "Selected entry deleted.")

    def clear_all(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        messagebox.showinfo("Cleared", "All entries have been cleared.")

    def save_to_excel(self):
        data = [self.tree.item(child)["values"] for child in self.tree.get_children()]
        if not data:
            messagebox.showwarning("No Data", "There is no data to save.")
            return
        df = pd.DataFrame(data, columns=["Name", "Mental", "Me-Time", "Screen-Free", "Status"])
        try:
            df.to_excel("C:/Users/Rebekah David/Desktop/Wellness_Log.xlsx", index=False)
            messagebox.showinfo("Saved", "Data saved to Wellness_Log.xlsx")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = WellnessLogger(root)
    root.mainloop()
