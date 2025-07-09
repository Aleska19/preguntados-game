#Preguntados
import random
#Diccionario de preguntas por categoria 

pregunta_por_categoria = {
    "Historia": [
        {
            "pregunta": "¿Quién fue el primer presidente de Estados Unidos?",
            "opciones": ["a) John Adams", "b) George Washington", "c) Thomas Jefferson"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Cuál fue la causa principal de la Primera Guerra Mundial?",
            "opciones": ["a) El asesinato del archiduque Francisco Fernando", "b) La invasión de Polonia", "c) La Guerra Fría"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Quién escribió Don Quijote de la Mancha?",
            "opciones": ["a) Gabriel García Márquez", "b) Miguel de Cervantes", "c) Lope de Vega"],
            "respuesta": "b"
        },
        
        {
            "pregunta": "¿En qué año llegó Cristóbal Colón a América?",
            "opciones": ["a) 1492", "b) 1500", "c) 1519"],
            "respuesta": "a"
        }
        
    ],

    "Deporte": [
        {
            "pregunta": "¿Cuál es el deporte más popular del mundo?",
            "opciones": ["a) Béisbol", "b) Fútbol", "c) Baloncesto"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿De qué color es la tarjeta que enseña un árbitro de fútbol para echar a un jugador?",
            "opciones": ["a) Amarilla", "b) Azul", "c) Roja"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué selección de fútbol ha ganado más Mundiales?",
            "opciones": ["a) Brasil", "b) Alemania", "c) Argentina"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿En qué país se originaron los Juegos Olímpicos?",
            "opciones": ["a) Grecia", "b) Italia", "c) Egipto"],
            "respuesta": "a"
        }
    ],

    "Entretenimiento": [
        {
            "pregunta": "¿Quién interpretó a Jack Dawson en Titanic?",
            "opciones": ["a)  Leonardo DiCaprio ", "b) Leonardo Da Vince", "c) Johnny Depp"],
            "respuesta": "a"
        },

        {
            "pregunta": "¿Qué personaje de dibujos animados vive en una piña bajo el mar?",
            "opciones": ["a) Patrick Estrella  ", "b) Bob Esponja", "c) Calamardo Tentaculo "],
            "respuesta": "b"
        },

        {
            "pregunta":"¿Cuál es la primera película de Disney?",
            "opciones": ["a) La Cenicienta ", "b) Mickey", "c) Blancanieves y los siete enanitos"],
            "respuesta": "c"
        },
        
        {
            "pregunta": "¿Qué banda británica escribió la canción 'Hey Jude'?",
            "opciones": ["a) The Beatles", "b) Queen", "c) Rolling Stones"],
            "respuesta": "a"
        },
    ],
    
    "Cultura General": [
        {
            "pregunta": "¿Cuál es la capital de Francia?",
            "opciones": ["a)  Madrid", "b) Paris", "c) Lima"],
            "respuesta": "b"
        },

        {
            "pregunta": "¿Cuál es el río más largo del mundo?",
            "opciones": ["a) Rio Misisipi ", "b) Nilo", "c) Amazonas "],
            "respuesta": "c"
        },

        {
            "pregunta":"¿Cuál es la montaña más alta del planeta?",
            "opciones": ["a)  El Everest  ", "b) Himalayas", "c) Chimborazo"],
            "respuesta": "a"
        },
        
        {
            "pregunta": "¿Cuál es el elemento químico cuyo símbolo es O?",
            "opciones": ["a) Oro", "b) Oxígeno", "c) Osmio"],
            "respuesta": "b"
        },
    ],

}

victorias = 0
derrotas = 0


def jugar(victorias, derrotas):
    print("Bienvenidos al Juego 🎮 de preguntados")
    categoria = list(pregunta_por_categoria.keys())
    print(' Categorias Disponibles')

    for i, cat in enumerate(categoria, 1):
        print(f'{i}, {cat}')

    #Eleccion del usuario 

    opcion = input("Elige una de las opciones anteriores en numero: ")
    if opcion == "1":
        categoria = 'Historia'
    elif opcion == "2":
        categoria = 'Deporte'
    elif opcion == "3":
        categoria = 'Entretenimiento'
    elif opcion == "4":
        categoria = 'Cultura General'
    else:
        print("❌ Opción inválida.")
        return
    
    victorias = 0
    derrotas = 0
    
    preguntas_al_usuario(categoria, victorias, derrotas)
    
    eleccion = input("¿Desea continuar?: ").capitalize()
    if eleccion == "Si": 
        jugar(victorias, derrotas)
    else:
        print("Gracias por jugar")



def preguntas_al_usuario(categoria, victorias, derrotas):
    pregunta = random.choice(pregunta_por_categoria[categoria])
    print(f"\n🧠 Pregunta de {categoria.capitalize()}: ")
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]: 
        print(opcion)
        
    return respuesta_del_usuario(categoria, pregunta, victorias, derrotas)
    

    # respuesta_usuario = input("Tu respuesta a), b) o c): ").lower()


def respuesta_del_usuario(categoria, pregunta, victorias, derrotas):
    respuesta_usuario = input("Tu respuesta a), b) o c): ").lower()
    if chequeo_respuesta(respuesta_usuario, pregunta) == False:
        derrotas += 1
        if derrotas == 3:
            print("☹️Perdiste la Categoria! ")
            return False
    elif chequeo_respuesta(respuesta_usuario, pregunta) == True:
        victorias += 1
        if victorias == 3:
            print("🎉Felicidades! Ganaste la categoria")
            return True
        
    preguntas_al_usuario(categoria, victorias, derrotas)
        
    
    
    

def chequeo_respuesta(respuesta_del_usuario, preguntas_al_usuario):
    if respuesta_del_usuario == preguntas_al_usuario['respuesta']:
        print("✅ ¡Correcto!")
        return True
    else: 
        print(f"❌ Incorrecto. La respuesta correcta era: {preguntas_al_usuario['respuesta']}")
        return False
    

    



jugar(victorias, derrotas)