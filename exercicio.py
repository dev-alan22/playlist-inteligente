def saudacaoPersonalizada(nome, periodo):
    if periodo == "manhã":
        return f"Bom dia, {nome}!"
    elif periodo == "tarde":
        return f"Boa tarde, {nome}!"
    elif periodo == "noite":
        return f"Boa noite, {nome}!"
    else:
        return f"Olá, {nome}!"

# Exemplos de uso:
print(saudacaoPersonalizada("João", "manhã"))   # Bom dia, João!
print(saudacaoPersonalizada("Maria", "noite"))  # Boa noite, Maria!
print(saudacaoPersonalizada("Ana", "tarde"))    # Boa tarde, Ana!
print(saudacaoPersonalizada("Carlos", "xyz"))   # Olá, Carlos!
