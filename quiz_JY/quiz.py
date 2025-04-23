def executar_quiz(perguntas):
    pontu = 0

    for i, pergunta in enumerate(perguntas, 1):
        print(f"\nPergunta {i}: {pergunta['pergunta']}")
        for idx, opcao in enumerate(pergunta["opcoes"], 1):
            print(f"{idx}. {opcao}")

        while True:
            try:
                escolha = int(input("Escolha sua resposta (1 a 4): "))
                if 1 <= escolha <= 4:
                    break
                else:
                    print("Por favor, escolha um número entre 1 e 4.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        resposta_usuario = pergunta["opcoes"][escolha - 1]
        if resposta_usuario == pergunta["resposta"]:
            print("Resposta correta!")
            pontu += 1
        else:
            print(f"Errado! A resposta correta era: {pergunta['resposta']}")

    print("\nQuiz finalizado!")
    print(f"Você acertou {pontu} de {len(perguntas)} perguntas.")