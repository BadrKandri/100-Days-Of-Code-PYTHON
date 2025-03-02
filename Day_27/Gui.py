import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import threading
from PIL import Image, ImageTk  # For displaying the Spotify logo

def create_gui(submit_callback):
    root = tk.Tk()
    root.title("Spotify Playlist Creator")
    root.geometry("500x500")
    root.configure(bg="#1A7F42")  # Darker Spotify Green Background
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", foreground="white", background="#1A7F42", font=("Arial", 12))
    style.configure("TButton", foreground="green", background="#121212", font=("Arial", 12, "bold"), padding=10)
    style.configure("TEntry", font=("Arial", 12), fieldbackground="#ffffff", foreground="#000000", borderwidth=2, relief="flat")
    
    # Load and display Spotify logo
    logo_image = Image.open("spotify_logo.png")  # Make sure you have this file in the same directory
    logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo, bg="#1A7F42")
    logo_label.pack(pady=10)
    
    title_label = ttk.Label(root, text="🎵 Create Your Spotify Playlist 🎵", font=("Arial", 18, "bold"))
    title_label.pack(pady=10)
    
    frame = ttk.Frame(root, padding=20, style="TFrame")
    frame.pack(fill="both", expand=True)
    
    date_label = ttk.Label(frame, text="📅 Enter Date (YYYY-MM-DD):", font=("Arial", 12))
    date_label.pack(anchor="w", pady=(5, 0))
    
    date_entry = ttk.Entry(frame, width=30, font=("Arial", 12))
    date_entry.pack(pady=(0, 10))
    
    playlist_label = ttk.Label(frame, text="🎧 Enter Playlist Name:", font=("Arial", 12))
    playlist_label.pack(anchor="w", pady=(5, 0))
    
    playlist_entry = ttk.Entry(frame, width=30, font=("Arial", 12))
    playlist_entry.pack(pady=(0, 20))
    
    feedback_label = ttk.Label(root, text="", foreground="white", font=("Arial", 12))
    feedback_label.pack(pady=(10, 5))
    
    loading_label = ttk.Label(root, text="", font=("Arial", 12))
    loading_label.pack(pady=5)
    
    def on_submit():
        date, playlist_name = date_entry.get(), playlist_entry.get()
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please use the format YYYY-MM-DD.")
            return
        
        if not playlist_name.strip():
            messagebox.showerror("Invalid Playlist Name", "Please enter a valid playlist name.")
            return
        
        loading_label.config(text="⏳ Creating playlist...", foreground="white")
        feedback_label.config(text="")
        root.update()
        
        def execute_callback():
            try:
                submit_callback(date, playlist_name)
                root.after(0, root.destroy)
            except Exception as e:
                root.after(0, feedback_label.config, {"text": f"❌ Error: {str(e)}", "foreground": "red"})
                root.after(0, loading_label.config, {"text": ""})
        
        threading.Thread(target=execute_callback, daemon=True).start()
    
    submit_button = ttk.Button(root, text="🚀 Create Playlist", command=on_submit)
    submit_button.pack(pady=20)
    
    root.mainloop()

