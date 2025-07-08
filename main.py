#Preguntados
import random
#Diccionario de preguntas por categoria 

pregunta_por_categoria = {
    "historia": [
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
        }
    ],
    "deporte": [
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
        }
    ]
}


def jugar():
    print("Bienvenidos al Juego 🎮 de preguntados")
    categoria = list(pregunta_por_categoria.keys())
    print(' Categorias Disponibles')

    for i, cat in enumerate(categoria, 1):
        print(f'{i}, {cat}')

    #Eleccion del usuario 

    opcion = input("Elige una de las opciones anteriores en numero: ")
    if opcion == "1":
        categoria = 'historia'
    elif opcion == "2":
        categoria = 'deporte'
    else:
        print("❌ Opción inválida.")
        return
    
    hacer_preguntas_por_categoria(categoria)



def hacer_preguntas_por_categoria(categoria):
    pregunta = random.choice(pregunta_por_categoria[categoria])
    print(f"\n🧠 Pregunta de {categoria.capitalize()}:")
    print(pregunta)
    for opcion in pregunta["opciones"]: 
        print(opcion)

    respuesta_usuario = input("Tu respuesta (a, b o c)").lower()
    if respuesta_usuario == pregunta['respuesta']:
        print("✅ ¡Correcto!")
    else: 
        print(f"❌ Incorrecto. La respuesta correcta era: {pregunta['respuesta']}")
 


jugar()