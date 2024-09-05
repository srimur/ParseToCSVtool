import customtkinter as ctk
from tkinter import filedialog, messagebox
from utils import convert_to_csv, convert_to_json
import os

class ChatGPTCSVParserApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Parse to CSV")
        self.root.geometry("900x600")


        icon_path = os.path.abspath(os.path.join("assets", "logo.ico"))
        self.set_icon(icon_path)

        title_label = ctk.CTkLabel(self.root, text="Parse to CSV", font=ctk.CTkFont(size=28, weight="bold"))
        title_label.pack(pady=(20, 10))

        self.text_area = ctk.CTkTextbox(self.root, height=350, width=800, corner_radius=10)
        self.placeholder = "If you want to generate test data in CSV format, this tool works on ChatGPT responses too..."
        self.placeholder_color = "gray"  
        self.default_text_color = "gray" 

        self.text_area.insert("1.0", self.placeholder)
        self.text_area.bind("<FocusIn>", self.clear_placeholder)
        self.text_area.bind("<FocusOut>", self.add_placeholder)
        self.text_area.pack(pady=(10, 20))

        save_csv_button = ctk.CTkButton(self.root, text="Save as CSV", command=self.save_as_csv, corner_radius=10, width=200)
        save_csv_button.pack(pady=10)

        save_json_button = ctk.CTkButton(self.root, text="Save as JSON", command=self.save_as_json, corner_radius=10, width=200)
        save_json_button.pack(pady=10)

    def set_icon(self, icon_path):
        try:
            # Set the window icon (title bar and taskbar)
            self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error setting icon: {e}")

    def clear_placeholder(self, event):
        if self.text_area.get("1.0", "end-1c") == self.placeholder:
            self.text_area.delete("1.0", "end")

    def add_placeholder(self, event):
        if not self.text_area.get("1.0", "end-1c").strip():
            self.text_area.insert("1.0", self.placeholder)

    def save_as_csv(self):
        response_text = self.text_area.get("1.0", "end-1c")
        if response_text == self.placeholder or not response_text.strip():
            messagebox.showerror("Error", "The text area is empty!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            convert_to_csv(response_text, file_path)
            messagebox.showinfo("Success", f"CSV file saved to {file_path}")

    def save_as_json(self):
        response_text = self.text_area.get("1.0", "end-1c")
        if response_text == self.placeholder or not response_text.strip():
            messagebox.showerror("Error", "The text area is empty!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            convert_to_json(response_text, file_path)
            messagebox.showinfo("Success", f"JSON file saved to {file_path}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ChatGPTCSVParserApp()
    app.run()
