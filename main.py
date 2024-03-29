import tkinter as tk
import random
import string


def sifre_uret(uzunluk=12):
    # Şifre karakterlerinin havuzu oluşturuluyor
    karakter_havuzu = string.ascii_letters + string.digits + string.punctuation

    # Rastgele karakterlerden oluşan bir şifre oluşturuluyor
    sifre = ''.join(random.choice(karakter_havuzu) for _ in range(uzunluk))

    return sifre


def sifre_uret_gui():
    def generate_password():
        uzunluk = int(entry.get())
        yeni_sifre = sifre_uret(uzunluk)
        output_label.config(text="Önerilen Şifre: " + yeni_sifre)

    root = tk.Tk()
    root.title("Şifre Önerme Programı")

    label = tk.Label(root, text="Şifre Uzunluğu:")
    label.grid(row=0, column=0, padx=10, pady=10)

    entry = tk.Entry(root)
    entry.grid(row=0, column=1, padx=10, pady=10)

    generate_button = tk.Button(root, text="Şifre Oluştur", command=generate_password)
    generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    output_label = tk.Label(root, text="")
    output_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    sifre_uret_gui()
