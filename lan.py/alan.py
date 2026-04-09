def analisar_vendas(vendas):
    total = sum(vendas)              # soma todos os valores
    media = total / len(vendas)      # divide pelo número de elementos
    maior = max(vendas)              # encontra o maior valor
    menor = min(vendas)              # encontra o menor valor
    
    return total, media, maior, menor

# Exemplo de uso:
valores = [100, 200, 50, 300]
total, media, maior, menor = analisar_vendas(valores)

print("Total:", total)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)
