#! /bin/env python3
import re

def update_payment(local):
    phrase = "Indo até "
    for loc in local[0]:
        if loc:
            phrase += f"{loc} "
    
    return phrase

def track_order(local):
    phrase = "Indo até "
    for loc in local[0]:
        if loc:
            phrase += f"{loc} "
    
    return phrase

intent_dict = {
    r"": "update_payment",
    r"\b(?:status|rastre(?:io|ar)|onde|consultar)\s?(?:(?:do|est[áa])?\s?(?:meu|minha)?|d[aeo])\s?(entrega|pedido)": "track_order",
}

action_dict = {
    "update_payment": update_payment,
    "track_order": track_order,
}

def main():
    print('Fala alguma coisa pro Bot\n(aperte "sair" para sair)\n')
    while True:
        command = input("Você: ").lower()

        if command == "sair": break

        for key, value in intent_dict.items():
            pattern = re.compile(key)
            groups = pattern.findall(command)
            if groups:
                print(f"Bot: {action_dict[value](groups)}")
        print()

if __name__ == "__main__":
    main()