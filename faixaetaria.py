def classificar_etapa_ensino():
    nome = input("Digite o nome da criança: ")
    idade = int(input("Digite a idade da criança: "))

    if idade < 1 or idade > 100:
        print(f"{nome}, por favor, informe uma idade válida entre 1 e 100.")
        return

    if 1 <= idade <= 5:
        print(f"{nome}, a criança está na Educação Infantil.")
    elif 6 <= idade <= 10:
        print(f"{nome}, a criança está no Ensino Fundamental I.")
    elif 11 <= idade <= 14:
        print(f"{nome}, a criança está no Ensino Fundamental II.")
    elif idade >= 15:
        print(f"{nome}, a criança está no Ensino Médio.")
    else:
        print("Ocorreu um erro inesperado.")

    jogar_novamente = input("Deseja classificar outra criança? (sim/não): ")
    if jogar_novamente.lower() == "sim":
        classificar_etapa_ensino()
    else:
        print("Obrigado!")

classificar_etapa_ensino()