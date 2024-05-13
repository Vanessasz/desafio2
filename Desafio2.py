
quantVitorias = int (input("Qual é a quantia de Vitórias do jogador? "))
quantDerrotas = int (input("Qual é a quantia de Derrotas do jogador? "))


def CalculaPartidas(quantVitorias, quantDerrotas):
    
    resultado = (quantVitorias - quantDerrotas)

    if resultado <= 10: 
        print("O Herói tem saldo de" ,resultado, "e está no nível de Ferro")
    if resultado >= 11 and resultado <= 20: 
        print("O Herói tem saldo de" ,resultado, "e está no nível de Bronze")
    if resultado >= 21 and resultado <= 50: 
        print("O Herói tem saldo de", resultado, "e está no nível de Prata")
    if resultado >= 51 and resultado <= 80: 
        print("O Herói tem saldo de", resultado, "e está no nível de Ouro") 
    if resultado >= 81 and resultado <= 90: 
        print("O Herói tem saldo de", resultado, "e está no nível de Diamante")
    if resultado >= 91 and resultado <= 100: 
        print("O Herói tem saldo de", resultado, "e está no nível de Lendário")
    if resultado >= 101:
        print("O Herói tem saldo de" , resultado, "e está no nível de Imortal")
   
CalculaPartidas(quantVitorias, quantDerrotas)