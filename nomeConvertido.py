vowels_dict = {
    'A': '@',
    'E': '&',
    'I': '!',
    'O': '#',
    'U': '*'
}

name = input("Digite seu nome e após aperte o name: ").lower().upper()
result = ""

for char in name:
    if char.isalpha():
        result += vowels_dict.get(char, char)
    else:
        result += char

print(result)