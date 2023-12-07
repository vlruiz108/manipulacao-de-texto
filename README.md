# manipulacao-de-texto

## Vamos escrever um programa para manipular um texto e conjunto de comandos.

Comandos
h move o cursor para a esquerda
l move o cursor para a direita
r<char> atualiza o carácter na posição atual pelo <char> 

Repetição dos comandos

Nh move o cursor N caracteres para a esquerda
Nl move o cursor N caracteres para a direita
Nr<char> atualiza N caracteres, começando pela posição do cursor, pelo <char> e move o cursor de posição
Exemplos
Vamos utilizar a seguinte string como entrada: “Hello Linguagem Python”
Entrada: Hello Linguagem Python
Comandos: hhllllhlhhl
Saída: Hello Linguagem Python - cursor: 3



Entrada: Hello Linguagem Python
Comandos: rhllllllrgllllllrb
Saída: hello linguagem python - cursor: 12



Entrada: Hello Linguagem Python
Comandos: rh6lrg6lrb2h
Saída: hello linguagem python - cursor: 10


Entrada: Hello Linguagem Python
Comandos: 9999lrO
Saída: Hello Linguagem PythonO - cursor: 20


Entrada: Hello Linguagem Python
Comandos: 21rA
Saída: AAAAAAAAAAAAAAAAAAAAA - cursor: 20