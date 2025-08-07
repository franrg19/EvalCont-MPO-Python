import time

def cargar_preguntas (tema):
    if tema == "1": #Ciudad de Málaga
        return [
            {"enunciado": "¿Qué famoso pintor, considerado uno de los artistas más influyentes del siglo XX, nació en Málaga?",
             "opciones": {"A": "Joan Miro","B": "Pablo Picasso","C": "Salvador Dali", "D": "Francisco de Goya"},
             "correcta": "B"},
            
            {"enunciado": "¿Cuál es el nombre de la fortaleza palaciega de la época musulmana que se encuentra en el centro de Málaga, cerca del Teatro Romano?",
             "opciones": {"A": "La Alhambra","B": "La Giralda","C": "El Real Alcazar", "D": "La alcazaba"},
             "correcta": "D"},
            
            {"enunciado": "¿Cuál es la playa urbana más famosa y céntrica de Málaga, conocida por su paseo marítimo y su cercanía al puerto?",
            "opciones": {"A": "Playa de Pedregalejo","B": "Playa de La Malagueta","C": "Playa de el Palo", "D": "Playa de Burriana"},
            "correcta": "B"},
            
            {"enunciado": "¿Qué plato típico de la gastronomía malagueña consiste en pescados ensartados en cañas y asados al fuego en barcas de arena en la playa?",
            "opciones": {"A": "Fritura malagueña","B": "Pescaito frito","C": "Espeto de sardina", "D": "Adobo de pescado"},
            "correcta": "C"},
            
            {"enunciado": "¿Cuál es el gentilicio de Málaga?",
             "opciones": {"A": "Malaguense", "B": "Malacitano", "C": "Malagueño", "D": "Malagano"},
             "correcta": "C"}            
        ]
        
    elif tema == "2": #cine
        return[
            {"enunciado": "¿Quién dirigió la película 'Titanic'?",
             "opciones": {"A": "Steven Spielberg", "B": "James Cameron", "C": "Christopher Nolan", "D": "Martin Scorsese"},
             "correcta": "B"},
            
            {"enunciado": "¿Qué actor interpreta a Iron Man?",
             "opciones": {"A": "Robert Downey Jr.", "B": "Chris Evans", "C": "Mark Ruffalo", "D": "Chris Hemsworth"},
             "correcta": "A"},
            
            {"enunciado": "¿Quién protagonizó la película 'Forrest Gump' y ganó el Óscar al Mejor Actor por su interpretación?",
             "opciones": {"A": "Tom Cruise", "B": "Leonardo DiCaprio", "C": "Tom Hanks", "D": "Brad Pitt"},
             "correcta": "C"},
            
            {"enunciado": "¿Cuál de estas películas de Disney fue la primera en ser completamente animada por ordenador?",
             "opciones": {"A": "Buscando a Nemo", "B": "El Rey León", "C": "Toy Story", "D": "La sirenita"},
             "correcta": "C"},
            
            {"enunciado": "¿Cuál es el nombre del colegio de magia y hechicería de la saga de películas y libros de 'Harry Potter'?",
             "opciones": {"A": "Beaxbatons", "B": "Durmstrang", "C": "Howarts", "D": "El Colegio de los magos"},
             "correcta": "C"},  
        ]
    
    elif tema == "3": #hechos historicos
        return[
            {"enunciado": "¿En qué año llegó Cristóbal Colón a América?",
             "opciones": {"A": "1492", "B": "1500", "C": "1485", "D": "1498"},
             "correcta": "A"},
            
            {"enunciado": "¿Quién fue el primer presidente de Estados Unidos?",
             "opciones": {"A": "Abraham Lincoln", "B": "Thomas Jefferson", "C": "George Washington", "D": "Benjamin Franklin"},
             "correcta": "C"},
            
            {"enunciado": "¿Quién fue el primer emperador del Imperio Romano?",
             "opciones": {"A": "Julio Cesar", "B": "Augusto", "C": "Neron", "D": "Marco Aurelio"},
             "correcta": "B"},
            
            {"enunciado": "¿Quién fue el líder militar y político de la antigua Francia que se autoproclamó Emperador de los franceses en 1804?",
             "opciones": {"A": "Carlos V", "B": "Luis XVI", "C": "Maximilien Robespierre", "D": "Napoleon Bonaparte"},
             "correcta": "D"},
            
            {"enunciado": "¿Cuál de las siguientes civilizaciones antiguas es conocida por haber construido las pirámides de Giza?",
             "opciones":{"A": "El Antiguo Egipto", "B": "Imperio Romano", "C": "La Antigua Grecia", "D": "La civilizacion Maya"},
             "correcta": "A"}    
        ]
    else:
        return []
    
    
def mostrar_pregunta (pregunta):
    print("\n" + pregunta["enunciado"])
    for letra,texto in pregunta["opciones"].items ():
        print( f"{letra}) {texto}")


def obtener_respuesta ():
    while True:
        respuesta = input("Tu respuesta (A, B, C o D): ").upper ()
        if respuesta in ["A","B","C","D"]:
            return respuesta
        else:
            print("Respuesta invalida. Intentalo de nuevo")
            
            
def corregir_respuesta (respuesta,correcta):
    return respuesta == correcta


def mostrar_resultados (nombre,aciertos,total):
    porcentaje= (aciertos/total)*100
    
    print("\ ### RESULTADOS ###")
    print(f"👤 Usuario: {nombre}")
    print(f"Total de preguntas: {total}")
    print(f"Aciertos: {aciertos}")
    print(f"Porcentaje de aciertos: {porcentaje:.2f}%")
    
    if porcentaje == 100:
        print("🏆 ¡Excelente! ¡Has acertado todas!")
    elif porcentaje >= 75:
        print("👏 ¡Muy bien!")
    elif porcentaje >= 50:
        print("👍 Nada mal, pero puedes mejorar.")
    else:
        print("📚 Necesitas practicar más.")

    
    
#Funcion para que el jugador elija un tema
def elegir_tema ():
    print ("\n ### TEMAS DISPONIBLES ###")
    print ("1 - ¿Conoces la ciudad de Málaga?")
    print ("2 - ¿Cuanto sabes de cine?")
    print ("3 - ¿Cuanto sabes de historia?")
    
    while True:
        tema=input("Elige un tema (1, 2 o 3): ")
        if tema in ["1","2","3"]:
            return tema
        else:
            print ("Opción no valida")
            

def guardar_resultado_archivo (nombre,aciertos,total):
    porcentaje= (aciertos/total)*100
    with open("ranking.txt","a") as archivo:
        archivo.write (f"{nombre}: {aciertos}/{total} ({porcentaje:.2f}%)\n")
        
        
def mostrar_ranking ():
    print("\n 📊 RANKING DE USUARIOS")
    
    try:
        with open("ranking.txt","r") as archivo:
            contenido =archivo.read ()
            if contenido:
                print (contenido)
            else:
                print("Aun no hay puntuaciones para mostrar")
    except FileNotFoundError:
        print("Aun no hay resultados para mostrar")
    
    
def empezar_quiz ():
    nombre = input("Introduce tu nombre de jugador")
    tema= elegir_tema ()
    preguntas = cargar_preguntas ()
    
    if not preguntas:
        print("No hay preguntas para este tema")
        return
    
    aciertos=0
    
    
    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        respuesta= obtener_respuesta ()
        
        if corregir_respuesta (respuesta,pregunta["correcta"]):
            print("✅ ¡Correcto!")
            aciertos +=1
        else:
            print(f"Incorrecto. La respuesta correcta era {pregunta["correcta"]}")
    
    mostrar_resultados (nombre,aciertos, len(preguntas))
    guardar_resultado_archivo (nombre, aciertos, len(preguntas))
            