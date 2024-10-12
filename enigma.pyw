import tkinter as tk
import string
import subprocess

class EnigmaMachine:
    def __init__(self, rotor_settings):
        self.rotors = [self.create_rotor(setting) for setting in rotor_settings]

    def create_rotor(self, setting):
        alphabet = string.ascii_uppercase
        rotor = {}
        for i in range(len(alphabet)):
            rotor[alphabet[i]] = alphabet[(i + setting) % len(alphabet)]
        return rotor

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char in string.ascii_uppercase:
                for rotor in self.rotors:
                    char = rotor[char]
                encrypted_message += char
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ""
        for char in message:
            if char in string.ascii_uppercase:
                for rotor in reversed(self.rotors):  # Usar los rotores en orden inverso
                    char = self.reverse_rotor(rotor)[char]
                decrypted_message += char
            else:
                decrypted_message += char
        return decrypted_message

    def reverse_rotor(self, rotor):
        return {v: k for k, v in rotor.items()}  # Invertir el rotor

class EnigmaApp:
    def __init__(self, master):
        self.master = master
        master.title("Máquina Enigma")

        self.label_message = tk.Label(master, text="Mensaje (en mayúsculas):")
        self.label_message.pack()

        self.entry_message = tk.Entry(master)
        self.entry_message.pack()

        self.label_rotor = tk.Label(master, text="Configuración de rotores (ej: 1,2,3):")
        self.label_rotor.pack()

        self.entry_rotor = tk.Entry(master)
        self.entry_rotor.pack()

        self.encrypt_button = tk.Button(master, text="Cifrar", command=self.encrypt_message)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Descifrar", command=self.decrypt_message)
        self.decrypt_button.pack()

        self.copy_button = tk.Button(master, text="Copiar Mensaje", command=self.copy_to_clipboard)
        self.copy_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def encrypt_message(self):
        message = self.entry_message.get().upper()
        rotor_settings = list(map(int, self.entry_rotor.get().split(',')))
        enigma = EnigmaMachine(rotor_settings)
        self.encrypted_message = enigma.encrypt(message)
        self.result_label.config(text=f"Mensaje cifrado: {self.encrypted_message}")

    def decrypt_message(self):
        if hasattr(self, 'encrypted_message'):
            rotor_settings = list(map(int, self.entry_rotor.get().split(',')))
            enigma = EnigmaMachine(rotor_settings)
            decrypted_message = enigma.decrypt(self.encrypted_message)
            self.result_label.config(text=f"Mensaje descifrado: {decrypted_message}")
        else:
            tk.messagebox.showwarning("Advertencia", "No hay mensaje cifrado para descifrar.")

    def copy_to_clipboard(self):
        if hasattr(self, 'encrypted_message'):
            self.master.clipboard_clear()
            self.master.clipboard_append(self.encrypted_message)
            tk.messagebox.showinfo("Copiado", "Mensaje copiado al portapapeles.")
        else:
            tk.messagebox.showwarning("Advertencia", "No hay mensaje para copiar.")

# Ejecutar la interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaApp(root)
    root.mainloop()