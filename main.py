from funciones import *
import time
from colorama import init,Fore,Style
init(autoreset=True)

# Función principal que muestra el menú del quiz
def mostrar_menu ():
    while True:  # Bucle infinito hasta que el usuario decida salir
        print(Fore.GREEN +"\n 🎮 MENU PRINCIPAL 🎮") 
        time.sleep(1)
        
        # Muestra las opciones del menú con pequeñas pausas entre ellas
        print("1 ▶️  Empezar Quiz")
        time.sleep(0.5)
        print("2.🏆-Ver Ranking")
        time.sleep(0.5)
        print("3.❌-Salir")
        time.sleep (0.5)
        
        # Solicita al usuario que seleccione una opción
        opcion = input("👉 Selecciona una opción: \n")
        
         # Evalúa la opción ingresada
        if opcion == "1":
            empezar_quiz ()
        elif opcion== "2":
            mostrar_ranking ()
        elif opcion== "3":
            print("👋 Hasta la proxima")
            break
        else:
            print("🚫 Opcion no valida")

            


 # Llama a la función para que se muestre el menú al iniciar el programa           
mostrar_menu ()
