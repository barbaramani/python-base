#Este programa imprime Hello World
"""Hello Worlds Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha variável LANG devidamente configurada ex:

    export (set) LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Barbara Mani"
__licence__ = "Unlicense"

import os
currente_language = os.getenv("LANG", "pt_BR")[:5]
msg = "Hello, World!"

if currente_language == "pt_BR":
    msg = "Olá, Mundo!"
elif currente_language =="it_IT":
    msg = "Ciao, Mondo!"

print(msg)
