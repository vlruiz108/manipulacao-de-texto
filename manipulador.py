def manipulador_de_texto(texto, comandos):
    cursor = 0
    texto_processado = list(texto)  # Converter a string em uma lista para facilitar a manipulação

    for comando in comandos:
        if comando == 'h':
            cursor = max(0, cursor - 1)  # Move o cursor para a esquerda, mas não abaixo de 0
        elif comando == 'l':
            cursor = min(len(texto_processado) - 1, cursor + 1)  # Move o cursor para a direita, mas não além do final do texto
        elif comando[0] == 'r':
            if len(comando) > 1 and comando[1].isdigit():
                num_chars = int(comando[1:])
                for i in range(num_chars):
                    if cursor + i < len(texto_processado):
                        texto_processado[cursor + i] = comando[-1]
                cursor += num_chars

    texto_final = ''.join(texto_processado)  # Converter a lista de caracteres de volta para uma string
    return texto_final, f"Cursor: {cursor}"


# Exemplos de uso da função com os dados fornecidos
entrada1 = "Hello Linguagem Python"
comandos1 = " 9999lrO"
saida1, cursor1 = manipulador_de_texto(entrada1, comandos1)
print(f"Saida: {saida1} - {cursor1}")
