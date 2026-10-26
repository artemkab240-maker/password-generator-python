import random
import string
from tkinter import Tk, Label, Button, Entry, messagebox


def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4 or length > 50:
            messagebox.showwarning("Внимание", "Длина пароля должна быть от 4 до 50 символов!")
            return

        characters = string.ascii_letters + string.digits
        password = "".join(random.choice(characters) for _ in range(length))

        entry_result.delete(0, "end")
        entry_result.insert(0, password)
    except ValueError:
        messagebox.onerror("Ошибка", "Введите корректное число!")


root = Tk()
root.title("Генератор паролей")
root.geometry("400x200")
root.resizable(False, False)

Label(root, text="Укажите длину пароля:", font=("Arial", 11)).pack(pady=10)
entry_length = Entry(root, font=("Arial", 11), width=10, justify="center")
entry_length.pack()
entry_length.insert(0, "12")

Button(root, text="Сгенерировать", font=("Arial", 10), command=generate_password, bg="#2ecc71", fg="white").pack(
    pady=15)

entry_result = Entry(root, font=("Arial", 12), width=25, justify="center")
entry_result.pack(pady=5)

print("Программа 'Генератор паролей' успешно запущена на локальной машине...")
root.mainloop()
