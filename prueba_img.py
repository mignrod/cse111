import tkinter as tk
import pickle

class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.geometry("1366x768+0+0")
        self.config(bg="black")
        self.overrideredirect(True)
        self.Img6=tk.PhotoImage(file="libre.gif")
        tk.Label(self, image=self.Img6).place(x=00,y=00)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1366x768+0+0")
        self.overrideredirect(True)
        self.withdraw()
        self.splash = SplashScreen(self)
        self.after(2000, self.salir_splash)
        self.indice = 0
        self.imagenes = ("me.png", "bg.jpg")


        self.cargar_datos()
        self.Imagenf = tk.PhotoImage(file=self.imagenes[self.indice])
        tk.Label(self, image=self.Imagenf).place(x=00,y=00)
        self.after(20000, self.destroy)


    def salir_splash(self):
        self.splash.destroy()
        self.deiconify()

    def cargar_datos(self):
        try:
            with open("Imagen.dat", "rb") as f:
                self.indice = (pickle.load(f) + 1) % len(self.imagenes) 
        except: pass
        finally:
            with open("Imagen.dat", "wb") as f:
                pickle.dump(self.indice, f)


if __name__ == "__main__":
    app = App()
    app.mainloop()