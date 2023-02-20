import pdfrw
import tkinter as tk
from tkinter import filedialog
import os.path

root = tk.Tk()
root.withdraw()

#Se busca el archivo PDF
dir_arch = filedialog.askopenfilename(title = "Select PDF File", filetypes = (("PDF files","*.pdf"),("all files","*.*")))

archivo = os.path.basename(dir_arch)


# Abrir el archivo PDF
pdf_file = open(archivo, 'rb')
pdf_reader = pdfrw.PdfReader(pdf_file)


# Crear una carpeta para los archivos PDF
import os
import errno

try:
    os.mkdir('Carpeta_Destino')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


# Extraer las páginas deseadas
pag_num = 0
while pag_num < pdf_reader.numPages:
    # Determina la carpeta destino donde buscara para enumerar las paginas
    page_file_name = f'Carpeta_Destino/{archivo}_pagina_{pag_num}.pdf'
    page_obj = pdf_reader.pages[pag_num]
    page_writer = pdfrw.PdfWriter()
    page_writer.addPage(page_obj)

    with open(page_file_name, 'wb') as page_file:
        page_writer.write(page_file)

    pag_num += 1

# Cerrar el archivo PDF
pdf_file.close()