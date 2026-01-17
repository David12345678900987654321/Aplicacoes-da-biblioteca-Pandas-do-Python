def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num*fatorial(num-1))
num1 = int(input("digite o número para saber o fatorial:\n"))
print(f"O fatorial é {fatorial(num1)}")