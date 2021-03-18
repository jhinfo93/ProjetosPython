from random import randint


print("------------------------------")
print("----- JOGO DA ADVINHAÇÂO -----")
print("------------------------------")
min = 0
max = 100

n = randint(min, max)
print(n)
t = 0
while (t < 10):
    print("------------------------------")
    print("----- TENTATIVAS ", t, " -----")
    print("------------------------------")
    num = int(input("Digite o número: "))

    if(num > n):
        print("--Você está acima do numero--")
        t = t+1
    if(num < n):
        print("--Vestá abaixo do numero--")
        t = t+1
    if(num == n):
        print("Parabéns, você acertou!!")
        t = 10
