import tkinter as tk
from tkinter import scrolledtext

def caesar_decrypt(ciphertext, shift):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():  # Verificar si es una letra
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Volver al final del alfabeto
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char  # Mantener otros caracteres
    return decrypted_message

def all_decryptions(ciphertext):
    decryptions = {}
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        decryptions[shift] = decrypted
    return decryptions

def keyword_matches(decrypted_message, keywords):
    matches = []
    words = decrypted_message.split()
    for word in words:
        if word in keywords:
            matches.append(word)
    return matches

def calculate_probabilities(decryptions, keywords):
    probabilities = {}
    
    for shift, message in decryptions.items():
        matches = keyword_matches(message, keywords)
        match_count = len(matches)
        total_keywords = len(keywords)
        
        percentage = (match_count / total_keywords) * 100 if total_keywords > 0 else 0
        probabilities[shift] = (percentage, matches, message)  # Guardamos el porcentaje, las palabras coincidentes y el mensaje descifrado
    
    return probabilities

class CaesarCipherApp:
    def __init__(self, master):
        self.master = master
        master.title("Descifrador César")

        self.label_message = tk.Label(master, text="Mensaje cifrado:")
        self.label_message.pack()

        self.entry_message = tk.Entry(master, width=50)
        self.entry_message.pack()

        self.decrypt_button = tk.Button(master, text="Descifrar", command=self.decrypt_message)
        self.decrypt_button.pack()

        self.result_label = tk.Label(master, text="Resultados:")
        self.result_label.pack()

        self.result_text = scrolledtext.ScrolledText(master, width=60, height=20)
        self.result_text.pack()

    def decrypt_message(self):
        ciphertext = self.entry_message.get().upper()  # Convertir a mayúsculas
        decryptions = all_decryptions(ciphertext)
        
        # Lista ampliada de palabras clave
        keywords = {
                        "A", "ABACO", "ABAD", "ABANDONAR", "ABIERTO", "ABISPA", "ABOGADO", "ABRIL", "ABUELA", 
                        "ABUELITO", "ACEITE", "ACELGA", "ACEPTAR", "ACERO", "ACUARIO", "ACUÁTICO", 
                        "ADIOS", "ADIVINANZA", "ADULTO", "AFICIÓN", "AFICIONADO", "AGUA", "AGUJERO", "AGUSTO", 
                        "AHORRAR", "AIRE", "AJEDREZ", "ALACRÁN", "ALAMBRE", "ALBA", "ALBERCA", "ALBUM", 
                        "ALDEANO", "ALERCE", "ALFABETO", "ALIMENTOS", "ALMA", "ALMANAQUE", "ALMENDRA", 
                        "ALMOHADA", "ALMUERZO", "ALQUIMIA", "AMAR", "AMIGO", "AMISTAD", "AMOR", "ANIMAL", 
                        "ANIVERSARIO", "ANCHO", "ANIMAR", "ANULAR", "APLAUSO", "APRENDER", "ARCO", 
                        "ARITMÉTICA", "ARROZ", "ARTES", "ARTISTA", "ASADO", "ASTRONOMÍA", "ATENCIÓN", 
                        "ATRCTIVO", "AUSTRALIA", "BAILE", "BAJO", "BASTÓN", "BEBÉ", "BEBIDA", "BICICLETA", 
                        "BISABUELO", "BISCUIT", "BISMA", "BIZCOCHO", "BOCA", "BOLSA", "BOMBA", 
                        "BONO", "BRAZO", "BROWNIE", "BUENAS", "CADENA", "CAMA", "CAMBIAR", "CAMIÓN", 
                        "CAMPANA", "CAMPANADA", "CAMPOS", "CAMPUS", "CANCIÓN", "CANELA", "CAPA", 
                        "CAPTURAR", "CARNE", "CARPINTERO", "CARRERA", "CARTEL", "CARTÓN", "CASA", 
                        "CASCADA", "CASCOS", "CIELO", "CINEMA", "CIRCO", "CIRCULACIÓN", "CITA", 
                        "CIUDAD", "CLASE", "CLIMA", "CLOVER", "CLOWN", "CONEJO", "CONOCER", "CONSEJO", 
                        "CONSTITUCIÓN", "CONTRA", "CORAZÓN", "CORTAR", "COSTO", "COSTURA", "CREAR", 
                        "CREATIVIDAD", "CRUZ", "CUIDAR", "CURSO", "DANZA", "DICHO", "DIFICIL", 
                        "DIRECCIÓN", "DIVERSIÓN", "DOLAR", "DOLOR", "DUCHA", "EDIFICIO", "EDUCACIÓN", 
                        "EDUCADOR", "ELECTRICIDAD", "ELIXIR", "EMOCIÓN", "EMPAQUE", "EMPEZAR", 
                        "ENCUENTRO", "ENLACE", "ENTREGA", "ESCALERA", "ESCAPAR", "ESCENARIO", 
                        "ESCUELA", "ESFERA", "ESPERAR", "ESPEJO", "ESPÍRITU", "ESTABLECER", "ESTADO", 
                        "ESTRELLA", "ESTUDIO", "EXAMEN", "EXPLORAR", "EXPOSICIÓN", "EXPRESIÓN", 
                        "FELICIDAD", "FELINO", "FELIZ", "FESTIVAL", "FIESTA", "FLEXIBILIDAD", "FLOR", 
                        "FLUJO", "FOCOS", "FORO", "FÚTBOL", "FUTURO", "GALAXIA", "GALLO", "GATO", 
                        "GENIO", "GEOGRAFÍA", "GERMÁN", "GIGANTE", "GIMNASIA", "GLOBAL", "GLOBO", 
                        "GUITARRA", "HABITANTE", "HABILIDADES", "HACER", "HOMBRE", "HORMIGA", 
                        "HORIZONTE", "HUGO", "IDEA", "IDEAS", "ILUMINAR", "IMÁGENES", "IMÁN", 
                        "IMPULSO", "INMERSIÓN", "INICIATIVA", "INSTITUCIÓN", "INTERNET", "INVIERNO", 
                        "INVITAR", "JARDÍN", "JAQUE", "JAZZ", "JUGAR", "JUVENTUD", "JUEGO", 
                        "JUICIO", "JULIO", "LAZAR", "LIBERTAD", "LIBRO", "LIDERAZGO", "LIMÓN", 
                        "LLAMADA", "LLUVIA", "LUNA", "LUZ", "MAESTRO", "MAGIA", "MALBADO", 
                        "MALDITO", "MAMÁ", "MANERA", "MANOS", "MAR", "MARAVILLA", "MARCHA", 
                        "MATERIA", "MATICES", "MATEMÁTICAS", "MAZAPÁN", "MEGAFONÍA", "MEJOR", 
                        "MEMORIA", "MENTE", "MÉTODO", "MOMENTO", "MONEDAS", "MONTAR", "MONTAÑAS", 
                        "MORIR", "MUJER", "MUNDO", "NATURALEZA", "NOMBRE", "NOSTALGIA", "NUBE", 
                        "NUESTRO", "NUNCA", "OCÉANO", "ODIO", "OLVIDO", "OPORTUNIDAD", "ORIGEN", 
                        "OTROS", "PAZ", "PAISAJE", "PAN", "PARA", "PARAÍSO", "PASEO", "PEZ", 
                        "PIANO", "PLANO", "PLAZA", "POBLACIÓN", "POLÍTICA", "POESÍA", "POLARIDAD", 
                        "PROYECTO", "QUE", "RECONOCER", "RECREO", "REFUGIO", "REGLA", "REINAR", 
                        "RELOJ", "RENACER", "REUNIÓN", "RÍO", "RITMO", "RUTA", "SALIDA", "SALUD", 
                        "SALUDABLE", "SALUDO", "SANGRE", "SÁBADO", "SABIDURÍA", "SABOR", "SABORES", 
                        "SACERDOTES", "SACRIFICIO", "SALTO", "SANDWICH", "SECRETO", "SELECCIÓN", 
                        "SENTIDO", "SILENCIO", "SILUETA", "SITIO", "SISTEMA", "SOL", "SOLICITUD", 
                        "SOMBRERO", "SOMOS", "SONRISA", "SONIDO", "SUEÑO", "SUEÑOS", "SUFRIMIENTO", 
                        "TABLA", "TACOS", "TAZA", "TEATRO", "TELEVISIÓN", "TENDENCIAS", "TERCERA", 
                        "TERRENO", "TIEMPO", "TIGRE", "TOMATE", "TRABAJO", "TRADICIÓN", 
                        "TRANQUILO", "TREN", "TRONCO", "TRUENO", "TURISMO", "UNIVERSIDAD", 
                        "UNIÓN", "USO", "VACACIONES", "VALOR", "VALORES", "VIAJAR", "VIDA", 
                        "VIGOR", "VÍNCULO", "VIRTUD", "VIRTUAL", "VOLVER", "YOGA", "ZAPATO", 
                        "ABUNDANCIA", "ABUSO", "ACERCAR", "ACOMPAÑAR", "ADAPTAR", "AGENDA", "ALIMENTO", 
                        "AMENAZA", "ANÁLISIS", "ANIMACIÓN", "APORTAR", "APROVECHAR", "AUMENTAR", 
                        "BASTANTE", "BEBIDA", "BENDICIÓN", "BUENA", "CANTAR", "CAPACIDAD", 
                        "CARNES", "CARTAS", "CIEGA", "COMUNICACIÓN", "CONDICIÓN", "CONEXIÓN", 
                        "CRECIMIENTO", "CRÉDITO", "DECISIÓN", "DEDICACIÓN", "DELICADO", 
                        "DESAFÍO", "DESIERTO", "DESPERTAR", "DESVÍO", "DIVERSIDAD", "EDUCACIONAL", 
                        "EJEMPLO", "ELEMENTO", "EMOCIONANTE", "ENTORNO", "EVALUAR", "EXPERIMENTO", 
                        "FELICITACIONES", "FENÓMENO", "FIDELIDAD", "FISICAMENTE", "FORMULARIO", 
                        "FRACASO", "FRECUENCIA", "GRACIAS", "HABILIDAD", "HEROÍSMO", "IMPACTO", 
                        "INNOVACIÓN", "INTEGRIDAD", "INTELECTUAL", "INVIERTE", "INVITACIÓN", 
                        "JERARQUÍA", "JOYA", "LAUREL", "LIDERAR", "MEJORA", "MEJORAR", 
                        "METÁFORA", "MORALIDAD", "MUERTE", "NAVEGAR", "NAVEGANTE", "NECESIDAD", 
                        "NIVELES", "OBLIGACIONES", "OPINIONES", "ORGANIZACIÓN", "ORIGINALES", 
                        "PAISAJES", "PENSAMIENTO", "PLAZO", "PLURALIDAD", "POTENCIAL", "PREPARAR", 
                        "PROBLEMAS", "PROGRESO", "QUERER", "REFORMA", "REFORZAR", "RENOVACIÓN", 
                        "RESPONSABILIDAD", "RETOS", "RIGOR", "SABIDURÍA", "SECRETO", "SEMINARIO", 
                        "SERVICIO", "SOSTENIBLE", "SUPERACIÓN", "SUSPENSO", "TALENTO", 
                        "TEMÁTICA", "TENIS", "TOPO", "TRADICIONES", "TRANSMISIÓN", 
                        "TRANSPARENCIA", "TROPA", "VALORACIÓN", "VERDAD", "VERANO", 
                        "VIDENTE", "VIOLENCIA", "VOLUNTAD", "VULNERABLE", "ZOOLOGÍA"
             }

        probabilities = calculate_probabilities(decryptions, keywords)

        # Limpiar el texto anterior
        self.result_text.delete(1.0, tk.END)
        
        # Mostrar todos los resultados
        self.result_text.insert(tk.END, "Resultados de descifrado:\n")
        for shift, (percentage, matches, message) in probabilities.items():
            matches_str = ", ".join(matches) if matches else "Ninguna"
            self.result_text.insert(tk.END, 
                f"Desplazamiento {shift}: {message}\n\n"
            )

# Ejecutar la interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()