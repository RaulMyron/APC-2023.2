n=int(input())
ordenacao={}
for _ in range(n):
    texto=input().split()
    size = len(texto)
    
    for i in range(size):
        ordenacao[i] = texto[i]
    
    ordem = sorted(ordenacao, key=lambda k: len(ordenacao[k]), reverse=True)
    
    for key in ordem:
        if key == ordem[-1]:
            print(ordenacao[key])
        else:
            print(ordenacao[key], end=" ")
    ordenacao={}
