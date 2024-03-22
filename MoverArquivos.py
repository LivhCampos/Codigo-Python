import os

os.chdir("C:\ArquivosPython\\PastaSaida")

os.listdir()

for f in os.listdir():
    os.rename(f, "C:\ArquivosPython\\PastaEntrada\\" + f)
    