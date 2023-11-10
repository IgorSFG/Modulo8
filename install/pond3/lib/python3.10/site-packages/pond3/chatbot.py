#! /bin/env python3
import re

def greet_back(time_of_day):
    if time_of_day == "dia":
        return f"Bom {time_of_day}!"
    else:
        return f"Boa {time_of_day}!"

def genki_back(_):
    return "Comigo está tudo bem, e com você?"

intent_dict = {
    r"\b(?:v[aá]i?|dirija(?:-se)?|leve|ir)\s?(?:para|at[ée]|ao|[aà])?\s?(?:a|o|ao)?\s(ponto|prateleira|estante|local|peça)\s?(\d*)",
}

action_dict = {
        "greetings": greet_back,
        "genki": genki_back
}

def main():

    command = input("Digite o seu comando: ")

    for key, value in intent_dict.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
            print(f"{action_dict[value](groups[0])}", end=" ")
    print()

if __name__ == "__main__":
    main()