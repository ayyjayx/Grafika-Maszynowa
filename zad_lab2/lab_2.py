import numpy as np
from PIL import Image

inicjaly = Image.open("inicjaly.bmp")
t_inicjaly = np.asarray(inicjaly)

def wstaw_obraz(o_wstawiany, w_m, h_m, wsp):
    tab_obrazu = np.asarray(o_wstawiany)
    h0, w0 = tab_obrazu.shape
    rozmiar_tab = (wsp * h0, wsp * w0)
    tab = np.zeros(rozmiar_tab, dtype=np.uint8)

    for i in range(h_m, h_m + h0 - 1):
        for j in range (w_m, w_m + w0 - 1):
            if i + h0 > wsp * h0 or j + w0 > wsp * w0:
                break
            tab[i][j] = tab_obrazu[i - h_m][j - w_m]
    tab = tab.astype(bool)
    img = Image.fromarray(tab)
    return img


# wstaw_obraz(inicjaly, 0, 0, 2).show()
# wstaw_obraz(inicjaly, 20, 20, 3).show()
# wstaw_obraz(inicjaly, 90, 90, 4).show()
