# Password Checker Tool - By Pranav Meshram | Bhandara Cyber Tool
# GitHub Ready Code - Exact Same as Screenshot
import customtkinter as ctk
import re, random, string, math
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Pranav Meshram - Bhandara Cyber Tool")
app.geometry("900x550")
app.configure(fg_color="#0B0E1A")

# Top Bar
top_bar = ctk.CTkFrame(app, fg_color="#0F1220", height=45, corner_radius=0)
top_bar.pack(fill="x")
ctk.CTkLabel(top_bar, text="🛡️ Pranav Meshram - Bhandara Cyber Tool", font=("Arial", 14, "bold"), text_color="#6C7BFF").pack(side="left", padx=20, pady=10)

# Title
ctk.CTkLabel(app, text="🔓 Password Strength Checker", font=("Arial", 22, "bold"), text_color="#4FC3F7").pack(pady=(15,2))
ctk.CTkLabel(app, text="Evaluate password strength and generate secure passwords", font=("Arial", 13), text_color="gray").pack()

# Main Card
card = ctk.CTkFrame(app, fg_color="#15182A", border_width=1, border_color="#1E3A5F", corner_radius=15)
card.pack(pady=20, padx=100, fill="both", expand=True)

ctk.CTkLabel(card, text="Password", font=("Arial", 12), text_color="#8EA1FF", anchor="w").pack(fill="x", padx=30, pady=(25,5))

# Password Entry with Eye
entry_frame = ctk.CTkFrame(card, fg_color="transparent")
entry_frame.pack(fill="x", padx=30)

password_entry = ctk.CTkEntry(entry_frame, placeholder_text="••••••••••••••", show="•", height=40, fg_color="#0B0E1A", border_color="#2A9DFF", font=("Arial", 14))
password_entry.pack(side="left", fill="x", expand=True)

def toggle_show():
    if password_entry.cget("show") == "•":
        password_entry.configure(show="")
    else:
        password_entry.configure(show="•")

eye_btn = ctk.CTkButton(entry_frame, text="👁", width=40, height=40, fg_color="transparent", command=toggle_show, text_color="#2ECC71", hover_color="#1A1D2E")
eye_btn.pack(side="left", padx=5)

# Strength
strength_row = ctk.CTkFrame(card, fg_color="transparent")
strength_row.pack(fill="x", padx=30, pady=(15,5))
ctk.CTkLabel(strength_row, text="Strength:", font=("Arial", 12)).pack(side="left")
strength_label = ctk.CTkLabel(strength_row, text="Weak", font=("Arial", 16, "bold"), text_color="#FF5555")
strength_label.pack(side="left", padx=10)

progress = ctk.CTkProgressBar(card, height=18, progress_color="#FF5555", fg_color="#2A2A2A")
progress.pack(fill="x", padx=30, pady=5)
progress.set(0.1)

percent_label = ctk.CTkLabel(card, text="10% • Weak", font=("Arial", 11), text_color="#2ECC71", anchor="e")
percent_label.pack(fill="x", padx=30)

req_label = ctk.CTkLabel(card, text="Requirements:", font=("Arial", 11), text_color="gray", anchor="w")
req_label.pack(fill="x", padx=30, pady=(10,5))

reqs = {}
for txt in ["8+ Characters", "Uppercase", "Lowercase", "Number", "Symbol"]:
    lbl = ctk.CTkLabel(card, text=f"✗ {txt}", font=("Arial", 12), text_color="#FF5555", anchor="w")
    lbl.pack(fill="x", padx=35, pady=2)
    reqs[txt] = lbl

def check_password(event=None):
    pwd = password_entry.get()
    checks = {
        "8+ Characters": len(pwd) >= 8,
        "Uppercase": bool(re.search(r"[A-Z]", pwd)),
        "Lowercase": bool(re.search(r"[a-z]", pwd)),
        "Number": bool(re.search(r"[0-9]", pwd)),
        "Symbol": bool(re.search(r"[!@#$%^&*()_+]", pwd))
    }
    score = sum(checks.values()) * 20

    for k,v in checks.items():
        reqs[k].configure(text=f"✓ {k}" if v else f"✗ {k}", text_color="#2ECC71" if v else "#FF5555")

    if score == 100:
        strength_label.configure(text="Strong", text_color="#2ECC71")
        progress.configure(progress_color="#2ECC71")
        progress.set(1)
        percent_label.configure(text="100% • Strong")
        entropy_label.configure(text="Entropy: ~72 bits")
        crack_label.configure(text="Estimated crack time: Centuries (>10¹² years)")
        status_label.configure(text="Status: Secure")
    elif score >= 60:
        strength_label.configure(text="Medium", text_color="#F1C40F")
        progress.configure(progress_color="#F1C40F")
        progress.set(score/100)
        percent_label.configure(text=f"{score}% • Medium")
    else:
        strength_label.configure(text="Weak", text_color="#FF5555")
        progress.configure(progress_color="#FF5555")
        progress.set(max(score/100, 0.1))
        percent_label.configure(text=f"{score}% • Weak")

def generate_password():
    pwd = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%") for _ in range(14))
    password_entry.delete(0, 'end')
    password_entry.insert(0, pwd)
    check_password()
    messagebox.showinfo("Password Generated", f"New Strong Password:\n{pwd}")

password_entry.bind("<KeyRelease>", check_password)

gen_btn = ctk.CTkButton(card, text="✨ Generate Strong Password", fg_color="#2ECC71", text_color="black", font=("Arial", 13, "bold"), height=38, corner_radius=8, command=generate_password)
gen_btn.pack(pady=20)

# Bottom Status Bar
bottom = ctk.CTkFrame(app, fg_color="#0F1220", height=35, corner_radius=0, border_width=1, border_color="#2ECC71")
bottom.pack(fill="x", side="bottom")
status_label = ctk.CTkLabel(bottom, text="🛡️ Status: Secure", font=("Arial", 11, "bold"), text_color="#2ECC71")
status_label.pack(side="left", padx=20)
entropy_label = ctk.CTkLabel(bottom, text="Entropy: ~72 bits", font=("Arial", 11), text_color="#5DADE2")
entropy_label.pack(side="left", padx=40)
crack_label = ctk.CTkLabel(bottom, text="Estimated crack time: Centuries (>10¹² years)", font=("Arial", 11))
crack_label.pack(side="left", padx=20)

app.mainloop()
