# Italiano — Carpeta de clases

**📥 Descargar la última versión:** https://github.com/matiasacc/Italiano/releases/latest/download/Italiano_carpeta.pdf

Apuntes de las clases de italiano, ordenados clase por clase, con el libro *Dieci A1* (Alma Edizioni).

- **`Italiano_carpeta.pdf`**: la carpeta para imprimir en doble faz. Cada clase arranca en página impar.
  - Cada clase tiene: En clase · Del libro · Lettura · Da ascoltare e da vedere · Mettiti alla prova · Tarea.
  - Anexos: Verbos (tabla de consulta) y Soluciones.
- **`fuente/`**: los scripts en Python (ReportLab) que generan el PDF.
  - `carpeta.py`: contenido de las clases e índice (es el que se ejecuta).
  - `letture.py`: textos de lectura · `extra.py`: canciones/películas, ejercicios y soluciones.
  - `verbos.py`: anexo de verbos · `comun.py`: estilos y armado (página impar para doble faz).

Para regenerar: `cd fuente && pip install reportlab && python3 carpeta.py`
