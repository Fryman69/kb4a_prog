
file_path = '2. prace_se_soubory/data/chatlog.txt'

nigiman = ""
jmeno = ""
zprava = ""
while zprava != "konec" and zprava !="Konec":
    jmeno = input("Zadej uzivatelske jmeno: ")
    zprava = input("Zadej zpravu: ")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f'{jmeno}: {zprava}\n')
