import random
import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear()
    print("<=== permainan batu, gunting, kertas ===>")
    pilihan = ("b", "k", "g")
    emoji = {
    "b" : "🪨",
    "k" : "🗒️",
    "g" : "✂️"
    }
    input_user = input("batu, kertas, gunting, (b/k/g): ").lower().strip()
    if input_user not in pilihan:
        print("pilihan tidak ada")
        input("tekan enter untuk lanjut: ")
        continue

    input_komputer = random.choice(pilihan)

    print(f"pilihan mu {emoji[input_user]}")
    print(f"pilihan komputer {emoji[input_komputer]}")

    if input_user == "b" and input_komputer == "g":
        print("kamu menang")
    elif input_user == "k" and input_komputer == "b":
        print("kamu menang")
    elif input_user == "g" and input_komputer == "k":
        print("kamu menang")
    elif input_user == input_komputer:
        print("kita seri")
    else:
        print("kamu kalah")
        break

    print("1. lanjut")
    print("2. keluar")
    out = input(">>> ").lower().strip()
    if out in ["berhenti", "keluar", "2", "2. keluar", "out", "end"]:
        break
    else:
        pass