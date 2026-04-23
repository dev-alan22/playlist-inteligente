# 🎵 Sistema de Playlist com Persistência

## 📌 O que o sistema faz
Este projeto implementa um sistema simples de gerenciamento de playlist.  
Ele permite:
- Adicionar músicas à playlist  
- Remover músicas da playlist  
- Registrar e processar ações em fila  
- Manter um histórico das ações realizadas  
- Salvar e carregar os dados da playlist automaticamente entre execuções  

---

## 📈 Como o sistema evoluiu
O desenvolvimento foi feito em etapas semanais:
1. **Semana 1** – Estrutura inicial com listas (`playlist`, `fila_acoes`, `historico`).  
2. **Semana 2** – Implementação do controle de ações e histórico.  
3. **Semana 3** – Adição da persistência com JSON para manter os dados entre execuções.  
4. **Semana 4 em diante** – Integração de todas as partes em um fluxo único: carregar dados → executar ações → salvar dados.  

---

## 💾 Como funciona o JSON
- O sistema utiliza a biblioteca `json` do Python.  
- A playlist é salva em um arquivo chamado **`playlist.json`**.  
- Funções principais:
  - `salvar_dados()`: grava a playlist atual no arquivo.  
  - `carregar_dados()`: lê o arquivo e restaura a playlist.  
- Caso o arquivo não exista, o sistema cria uma playlist vazia.  

Isso garante que as músicas adicionadas/removidas sejam mantidas mesmo após encerrar o programa.

---

## 🛠️ Estruturas usadas
- **`playlist`** → lista principal de músicas.  
- **`fila_acoes`** → fila de ações pendentes (ex.: adicionar/remover).  
- **`historico`** → registro de todas as ações realizadas.  
- **JSON** → formato de persistência para salvar e carregar os dados da playlist.  

👉 Com isso, o sistema está completo: simples, funcional e persistente.  
