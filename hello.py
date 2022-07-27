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
__version__ = "0.1.2"
__author__ = "Barbara Mani"
__licence__ = "Unlicense"

import os
current_language = os.getenv("LANG", "it_IT")[:5]

msg ={
    "en_US":"Hello, World!",
    "pt_BR":"Olá, Mundo!", 
    "it_IT":"Ciao,Mondo!",
    "es_Sp":"Hola, Mundo!",
    "fr_FR":"Bonjour, Monde!"
}
  
#msg = "Olá,Mundo!"
#if currente_language == "pt_BR":
#    msg = "Olá, Mundo!"
#elif currente_language =="it_IT":
#    msg = "Ciao, Mondo!"

print(msg[current_language])


