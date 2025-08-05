
def chatbot_resposta(mensagem):
    if mensagem.lower() in ["oi", "olá", "olá, como vai?", "ola", "ola, como vai?"]:
        return "Olá! Como posso ajudar você hoje?"
    elif mensagem.lower() in ["qual é o seu nome?", "qual e o seu nome?", "qual é o seu nome", "qual e o seu nome"]:
        return "Eu sou o Jarvis. Como posso ajudar você hoje?"
    elif mensagem.lower() in ["como você está?", "como você está?", "como você está?", "como você está?"]:
        return "Estou bem, obrigado por perguntar!"
    elif mensagem.lower() in ["qual é a sua função?", "qual e a sua função?", "qual é a sua função", "qual e a sua função"]:
        return "Eu sou um assistente virtual criado para ajudar você com suas necessidades."
    elif mensagem.lower() in ["conhece a Carol?", "conhece a carol?", "conhece a Carol", "conhece a carol"]:
        return "Carol é uma amiga muito especial. Ela é uma pessoa incrivelmente inteligente e linda. Ela é a esposa de meu criador."
    else:
        return "Desculpe, não entendi a pergunta. Pode repetir?"
    

print("Chatbot iniciado! Digite 'sair' para encerrar.")
while True:
    mensagem = input("Digite uma mensagem: ")
    
    if mensagem.lower() in ["sair", "exit", "quit", "tchau"]:
        print("Até logo! Foi um prazer conversar com você!")
        break
    
    resposta = chatbot_resposta(mensagem)
    print(resposta)