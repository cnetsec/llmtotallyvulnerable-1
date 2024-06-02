from app.model import GPT2Generator
import sqlite3

# Inicializar o modelo GPT-2
generator = GPT2Generator()

# Banco de dados SQLite
conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

# Criar tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS qa
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              question TEXT NOT NULL,
              answer TEXT NOT NULL)''')
conn.commit()

# Função para inserir nova pergunta e resposta no banco de dados
def inserir_qa(question, answer):
    c.execute("INSERT INTO qa (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()

# Função para responder perguntas usando o modelo GPT-2 e dados no banco de dados
def responder_pergunta(pergunta):
    c.execute("SELECT answer FROM qa WHERE question=?", (pergunta,))
    resposta = c.fetchone()
    if resposta:
        return resposta[0]
    else:
        return generator.generate_response(pergunta)

# Função para treinar o modelo com novos exemplos
def treinar_modelo(novos_exemplos):
    for exemplo in novos_exemplos:
        inserir_qa(exemplo["pergunta"], exemplo["resposta"])
    print("Modelo treinado com sucesso!")

# Função principal
def main():
    while True:
        print("\nOpções:")
        print("1 - Fazer uma pergunta")
        print("2 - Treinar o modelo")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pergunta = input("Digite sua pergunta: ")
            resposta = responder_pergunta(pergunta)
            print(f"Resposta: {resposta}")

        elif opcao == "2":
            novos_exemplos = []
            while True:
                nova_pergunta = input("Digite uma nova pergunta (ou deixe em branco para parar): ")
                if not nova_pergunta:
                    break
                nova_resposta = input("Digite a resposta correspondente: ")
                novos_exemplos.append({"pergunta": nova_pergunta, "resposta": nova_resposta})
            
            if novos_exemplos:
                treinar_modelo(novos_exemplos)
            else:
                print("Nenhum novo exemplo foi adicionado.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == '__main__':
    main()

