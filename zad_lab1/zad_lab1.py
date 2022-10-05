from PIL import Image
import numpy as np

obraz = Image.open("inicjaly.bmp")  # wczytywanie obrazu
obraz.show()
print("tryb:", obraz.mode)
print("format:", obraz.format)
print("rozmiar:", obraz.size)

dane = np.asarray(obraz)
# print(dane)
dane1 = dane * 1
# print(dane1)
np.savetxt('inicjaly.txt', dane1, delimiter=' ', newline='\n')

dane2 = np.loadtxt("inicjaly.txt", dtype=np.int_, converters=float)

print("Typ danych tablicy:", dane2.dtype)
print("Rozmiar tablicy:", dane2.shape)
print("Liczba elementow:", dane2.size)
print("Wymiar tablicy:", dane2.ndim)
print("Rozmiar wyrazu tablicy:", dane2.itemsize)
print("(50,30):", dane2[30][50])
print("(90,40):", dane2[40][90])
print("(90,0):", dane2[0][99])
