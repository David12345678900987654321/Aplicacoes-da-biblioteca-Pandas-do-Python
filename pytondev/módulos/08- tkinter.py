import tkinter as tk

#módulo para aplicações deskto

#1 criando uma janela

windows = tk.Tk()
windows.geometry("300x150")
windows.title("01")

#2 cirando um frame
frame = tk.Frame(windows)
frame.pack(padx=10,pady=10,fill="x",expand=True)

#3 adicionando o label
label = tk.Label(frame, text="Olá mundo")
label.pack(fill="x",expand=True)

#4 input text

frase_lab= tk.Label(frame, text="Frase")
frase_lab.pack(fill="x",expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill="x", expand=True)

def click():
    label.config(text=frase_inp.get())

#6 adicionando o botão

button = tk.Button(frame,text="Enviar", command=click)
button.pack()

windows.mainloop()