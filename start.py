#!/usr/bin/env python3

ASCII_ART = r"""
 _____       _        _____       _        
|  ___|__ _| | _____|  ___|__ __ _| |_ ___ 
| |_ / _` | |/ / _ \ |_ / _ \/ _` | __/ _ \
|  _| (_| |   <  __/  _|  __/ (_| | ||  __/
|_|  \__,_|_|\_\___|_|   \___|\__,_|\__\___|
"""

INFO = """
Bienvenido a FakeCyber!

Este repositorio es un proyecto de ejemplo para demostraciones y pruebas 
de conceptos de ciberseguridad. Usa este script para mostrar un mensaje 
de bienvenida en la terminal.
"""

def main():
    # Limpiar la pantalla y mover el cursor al inicio
    print("\033[2J\033[H", end="")
    # Imprimir arte ASCII en color cian
    print("\033[96m" + ASCII_ART + "\033[0m")
    # Imprimir informacion
    print(INFO)
    print("Para volver a ver esta pantalla ejecuta: \033[92mpython3 start.py\033[0m")

if __name__ == "__main__":
    main()
