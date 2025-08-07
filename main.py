import tkinter as tk
import random
from datetime import datetime

# Preguntas
preguntas = [
    {"pregunta": "¿Qué país ganó el Mundial 2018?", "opciones": ["Alemania", "Brasil", "Francia", "Argentina"], "respuesta_correcta": 2},
    {"pregunta": "¿Qué selección es 'La Canarinha'?", "opciones": ["Argentina", "Brasil", "España", "Italia"], "respuesta_correcta": 1},
    {"pregunta": "¿Quién es 'La Pulga'?", "opciones": ["Cristiano", "Messi", "Maradona", "Neymar"], "respuesta_correcta": 1}
]

random.shuffle(preguntas)

# Estado
indice_actual = 0
puntuacion = 0
vidas = 3
tiempo_restante = 15
temporizador_id = None
nombre_jugador = ""

# Ventana principal
ventana = tk.Tk()
ventana.title("Quiz de Fútbol")
ventana.geometry("600x500")
ventana.configure(bg="#1e1e2f")

# 🎬 Intro animada
def mostrar_intro(texto, i=0):
    if i < len(texto):
        lbl_intro.config(text=lbl_intro.cget("text") + texto[i])
        ventana.after(80, lambda: mostrar_intro(texto, i + 1))
    else:
        ventana.after(1000, mostrar_pantalla_nombre)

def mostrar_pantalla_nombre():
    frame_intro.pack_forget()
    frame_inicio.pack()

# 🎮 Iniciar juego
def iniciar_juego():
    global nombre_jugador
    nombre_jugador = entrada_nombre.get().strip()
    if nombre_jugador == "":
        lbl_error.config(text="❗ Ingresa tu nombre", fg="red")
        return
    frame_inicio.pack_forget()
    frame_quiz.pack()
    mostrar_pregunta()

# Mostrar pregunta
def mostrar_pregunta():
    global tiempo_restante, temporizador_id
    if indice_actual < len(preguntas) and vidas > 0:
        pregunta = preguntas[indice_actual]
        lbl_pregunta.config(text=pregunta["pregunta"])
        for i in range(4):
            botones[i].config(text=pregunta["opciones"][i], state="normal")
        lbl_resultado.config(text="")
        lbl_vidas.config(text=f"❤️ Vidas: {vidas}")
        tiempo_restante = 15
        actualizar_temporizador()
    else:
        terminar_juego()

# Verificar respuesta
def responder(indice):
    global indice_actual, puntuacion, vidas
    ventana.after_cancel(temporizador_id)
    pregunta = preguntas[indice_actual]
    if indice == pregunta["respuesta_correcta"]:
        lbl_resultado.config(text="✅ ¡Correcto!", fg="lightgreen")
        puntuacion += 1
    else:
        correcta = pregunta["opciones"][pregunta["respuesta_correcta"]]
        lbl_resultado.config(text=f"❌ Incorrecto. Era: {correcta}", fg="salmon")
        vidas -= 1
    for btn in botones:
        btn.config(state="disabled")
    ventana.after(1500, siguiente_pregunta)

# Avanzar
def siguiente_pregunta():
    global indice_actual
    indice_actual += 1
    mostrar_pregunta()

# Temporizador
def actualizar_temporizador():
    global tiempo_restante, temporizador_id, vidas
    lbl_tiempo.config(text=f"⏱️ Tiempo: {tiempo_restante}s")
    if tiempo_restante > 0:
        tiempo_restante -= 1
        temporizador_id = ventana.after(1000, actualizar_temporizador)
    else:
        lbl_resultado.config(text="⏰ Tiempo agotado", fg="orange")
        vidas -= 1
        for btn in botones:
            btn.config(state="disabled")
        ventana.after(1500, siguiente_pregunta)

# Guardar puntuación
def guardar_puntuacion():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("puntuacion.txt", "a") as archivo:
        archivo.write(f"{fecha} - {nombre_jugador}: {puntuacion} puntos\n")

# Mostrar ranking
def mostrar_ranking():
    try:
        with open("puntuacion.txt", "r") as archivo:
            lineas = archivo.readlines()
            ultimas = lineas[-5:]
            ranking = "🏆 Top 5:\n" + "".join(ultimas)
            lbl_resultado.config(text=ranking, fg="cyan")
    except FileNotFoundError:
        lbl_resultado.config(text="No hay puntuaciones guardadas", fg="gray")

# Final del juego
def terminar_juego():
    lbl_pregunta.config(text=f"🏁 ¡Juego terminado, {nombre_jugador}!")
    for btn in botones:
        btn.config(state="disabled")
    lbl_tiempo.config(text="")
    lbl_vidas.config(text="")
    guardar_puntuacion()
    mostrar_ranking()

# Frame de intro
frame_intro = tk.Frame(ventana, bg="#1e1e2f")
frame_intro.pack(pady=150)
lbl_intro = tk.Label(frame_intro, text="", font=("Arial", 20), fg="cyan", bg="#1e1e2f")
lbl_intro.pack()
mostrar_intro("⚽ Bienvenido al Quiz de Fútbol ⚽")

# Frame de inicio
frame_inicio = tk.Frame(ventana, bg="#1e1e2f")
tk.Label(frame_inicio, text="🎮 Ingresa tu nombre:", font=("Arial", 16), fg="white", bg="#1e1e2f").pack(pady=10)
entrada_nombre = tk.Entry(frame_inicio, font=("Arial", 14), width=30)
entrada_nombre.pack()
btn_comenzar = tk.Button(frame_inicio, text="Comenzar", font=("Arial", 14), command=iniciar_juego)
btn_comenzar.pack(pady=10)
lbl_error = tk.Label(frame_inicio, text="", font=("Arial", 12), bg="#1e1e2f")
lbl_error.pack()

# Frame del quiz
frame_quiz = tk.Frame(ventana, bg="#1e1e2f")

lbl_pregunta = tk.Label(frame_quiz, text="", font=("Arial", 16), wraplength=550, fg="white", bg="#1e1e2f")
lbl_pregunta.pack(pady=20)

botones = []
colores_botones = ["#ff6f61", "#6fcf97", "#56ccf2", "#f2c94c"]
for i in range(4):
    btn = tk.Button(frame_quiz, text="", font=("Arial", 12), width=40,
                    bg=colores_botones[i], fg="black",
                    command=lambda i=i: responder(i))
    btn.pack(pady=5)
    botones.append(btn)

lbl_resultado = tk.Label(frame_quiz, text="", font=("Arial", 14), bg="#1e1e2f", fg="white")
lbl_resultado.pack(pady=20)

lbl_tiempo = tk.Label(frame_quiz, text="", font=("Arial", 14), bg="#1e1e2f", fg="orange")
lbl_tiempo.pack()

lbl_vidas = tk.Label(frame_quiz, text="", font=("Arial", 14), bg="#1e1e2f", fg="red")
lbl_vidas.pack(pady=10)

ventana.mainloop()