## Discord Bot (Python)

Bot simple para aprender Python y trabajar en equipo

# Requisitos
- Python 3.10+
- Discord bot token

# Instalación
'''bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# Ejecutar
'''bash
(para evitar cualquier problema ejecutar después de inicializar el entorno virtual)
python bot.py

# NOTAS
no guardar el archivo .env en la carpeta donde se hace el commit (si queremos pushear el commit que tiene el archivo .env nos va a tirar error)
Mejor tener el .env guardado en otra carpeta de manera local, copiarla y pegarla en la carpeta del código para ejecutarlo y listo. Luego al finalizar el trabajo borrar el archivo .env de la carpeta del código y luego hacer el commit.
