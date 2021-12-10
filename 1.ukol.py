from task_template import TEXTS
import os

"""
1. Vyžádá si od uživatele přihlašovací jméno a heslo.
2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
3. Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program.

"""

#definovat uživatele a jejich hesla do slovníku
uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

oddelovac = "-" * 35
mezera = " " * 6

# Zadání uživatelksého jména
username = input('Uživatelské jméno: ')

# Ověření a zadání hesla
if username in uzivatele.keys():
    password = input('Heslo: ')
else:
    print("Neregistrovaný uživatel")
    quit()

print(oddelovac)

# Ověření hesla a výber txt souboru
if uzivatele.get(username) == password:
    print(f'Vítej v aplikaci, {username}.{os.linesep}K analýze máš na výber ze 3 textů.')
    Text_no = input('Zadej číslo mezi 1-3: ')
else:
    print('Heslo je špatné')
    quit()

print(oddelovac)

# Ověření Zda skutečně zadal číslo a počítáme, že podruhé to zadá správně
if Text_no.isnumeric():
    # Ověření Zda skutečně zadal číslo 1,2,3
    if 1 <= int(Text_no) <= 3:
        print(f'Statistiky')
    else:
        print('Zadané číslo není v rozmezí 1-3.')
        Text_no = input('Zadej číslo mezi 1-3: ')
else:
    print('Zadaná hodnota není číslo.')
    Text_no = input('Zadej číslo mezi 1-3: ')
    
# Změnit index
Txt_index = (int(Text_no)-1)

# Uprava textu
TEXTS[Txt_index] = TEXTS[Txt_index].replace('.', '')
TEXTS[Txt_index] = TEXTS[Txt_index].replace(',', '')
TEXTS[Txt_index] = TEXTS[Txt_index].replace('-', ' ')

# Ananlyza textu
Pocet_slov = len(TEXTS[Txt_index].split())
print(f'Ve vybraném textu je {Pocet_slov} slov.')
lowercase = sum(map(str.islower, TEXTS[Txt_index].split()))
title = sum(map(str.istitle, TEXTS[Txt_index].split()))
digit = sum(map(str.isdigit, TEXTS[Txt_index].split()))

upprecase = 0
upprecasehelp = False

for words in TEXTS[Txt_index].split():
    if words.isupper():
        for character in words:
            if character.isdigit():
                upprecasehelp = False
                break
            else:
                upprecasehelp = True
        if upprecasehelp:
            upprecase += 1
            print(words)

suma = 0
for word in TEXTS[Txt_index].split():
    if word.isdigit():
        suma += int(word)

print(f'Ve vybraném textu je {upprecase} slov složených pouze z velkých písmen.')
print(f'Ve vybraném textu jsou {digit} číslice.')
print(f'Součet číslic je {suma}.')
print(f'Ve vybraném textu je {title} slov s počátečním velkým písmenem.')
print(f'Ve vybraném textu je {lowercase} slov složených pouze z malých písmen.')
print(oddelovac)
print(f'Delka slova {mezera} frekvence slova')
print(oddelovac)

words = TEXTS[Txt_index].split()

# graf
lengths = [len(word) for word in words]
max_length = max(lengths)
tallies = [0 for x in range(max_length + 1)]

for length in lengths:
    tallies[length] += 1

total_words = len(words)
for length in range(len(tallies)):
    if tallies[length] != 0:
        freq = tallies[length]
        hodnoty = "*" * freq
        print(f'{length:3} {hodnoty:17} {freq:10d}')