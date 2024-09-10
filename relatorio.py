import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def exportar_para_pdf():
    pdf_file = "conteudo_exportado.pdf"

    with PdfPages(pdf_file) as pdf:
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Gráfico de Exemplo')
        pdf.savefig(fig)

        plt.close(fig)
    print("PDF exportado com sucesso.")


root = tk.Tk()
root.title("Exportar para PDF")
botao_exportar = tk.Button(root, text="Exportar Gráfico para PDF", command=exportar_para_pdf)
botao_exportar.pack()
root.mainloop()
