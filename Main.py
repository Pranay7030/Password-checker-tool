import re

print("===================================")
print("   Password Strength Checker v1.0  ")
print("   Made for Cyber Safety Education ")
print("===================================\n")

password = input("Apna password yahan likho: ")

score = 0
feedback = []

# 1. Length check
if len(password) >= 8:
    score += 1
else:
    feedback.append("Kam se kam 8 characters rakho")

# 2. Number check
if re.search(r"[0-9]", password):
    score += 1
else:
    feedback.append("1 number add karo: 0-9")

# 3. Capital letter check
if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("1 Capital letter add karo: A-Z")

# 4. Special character check
if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
    score += 1
else:
    feedback.append("1 special character add karo: !@#$")

# Result dikhao
print("\n--- Result ---")
if score <= 1:
    print("Status: Weak 🔴")
    print("Ye password bahut easy hai, hack ho sakta hai")
elif score == 2:
    print("Status: Medium 🟡")
    print("Thik hai, par aur strong banao")
elif score == 3:
    print("Status: Strong 🟢")
    print("Badhiaya password hai!")
else:
    print("Status: Very Strong 🔵")
    print("Perfect! Aisa hi password rakhna chahiye")

if feedback:
    print("\n--- Improvement Tips ---")
    for tip in feedback:
        print("-", tip)

print("\nNote: Ye tool sirf apna password check karne ke liye hai")
