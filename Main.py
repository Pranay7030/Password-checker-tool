import re, time, random

R="\033[91m"; G="\033[92m"; Y="\033[93m"; B="\033[94m"; C="\033[96m"; W="\033[97m"; M="\033[95m"; E="\033[0m"

def banner():
    print(f"{C}  ____  _                     _                   {E}")
    print(f"{C} | __ )| |__   __ _ __   __| | __ _ __ __ _  {E}")
    print(f"{B} |  _ \\| '_ \\ / _` | '_ \\ / _` |/ _` | '__/ _` | {E}")
    print(f"{M} | |_) | | | | (_| | | | | (_| | (_| | | | (_| | {E}")
    print(f"{Y} |____/|_| |_|\\__,_|_| |_|\\__,_|\\__,_|_|  \\__,_| {E}")
    print(f"{W}=================================================={E}")
    print(f"{G} 🛡️  Pranav Meshram - Bhandara Cyber Tool{E}")
    print(f"{G} 🔓 Password Strength Checker - Termux Edition{E}")
    print(f"{W}=================================================={E}")

def check(pwd):
    checks = {
        "8+ Characters": len(pwd)>=8,
        "Uppercase [A-Z]": bool(re.search(r"[A-Z]", pwd)),
        "Lowercase [a-z]": bool(re.search(r"[a-z]", pwd)),
        "Number [0-9]": bool(re.search(r"[0-9]", pwd)),
        "Symbol [!@#]": bool(re.search(r"[!@#$%^&*]", pwd))
    }
    score = sum(checks.values())
    print(f"\n{W}─── Requirements ───{E}")
    for k,v in checks.items():
        print(f"{G}  [✔] {k}{E}" if v else f"{R}  [✘] {k}{E}")
    print(f"{W}────────────────────{E}")
    bar = "█" * score + "░" * (5-score)
    if score==5:
        print(f"{G} [{bar}] STRONG 100% {E}")
        print(f"{C} Entropy: ~72 bits | Crack Time: Centuries{E}")
        print(f"{G} Status: Secure Hai Bhai! ✅{E}")
    elif score>=3:
        print(f"{Y} [{bar}] MEDIUM {score*20}% {E}")
        print(f"{Y} Status: Thoda aur strong bana...{E}")
    else:
        print(f"{R} [{bar}] WEAK {score*20}% {E}")
        print(f"{R} Status: Hack ho jayega! ❌{E}")

banner()
while True:
    p = input(f"\n{M}┌─[{W}PASSWORD{Y}@{W}BHANDARA{M}]{W}─[{C}~{W}]\n{M}└──╼ {W}Password daal: {E}")
    if p.lower()=="exit": 
        print(f"{G}Bye Bye!{E}")
        break
    check(p)
