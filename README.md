## Discord Bot (Python)

Bot simple para aprender Python y trabajar en equipo

# Requisitos
- Python 3.10+
- Discord bot token

# Instalación
'''bash
git clone git@github.com:Lucas-Acevedo/Discord-bot.git

cd DiscordBot

python -m venv venv

Linux: source venv/bin/activate
Windows: .\venv\Scripts\Activate.ps1

pip install -r requirements.txt

# Ejecutar
'''bash
(para evitar cualquier problema ejecutar después de inicializar el entorno virtual)
python bot.py

# ¿Qué hacer al terminar?
'''bash
git add . ##Esto "prepara" todos los archivos modificados para hacer el commit ("Screenshot" de la carpeta del bot)
git commit -m "COMENTARIO" ##Esto hace el commit
git push ##Esto sube los archivos al repositorio de github
deactivate ##Esto desactiva el entorno virtual


# NOTAS
no guardar el archivo .env en la carpeta donde se hace el commit (si queremos pushear el commit que tiene el archivo .env nos va a tirar error)
Mejor tener el .env guardado en otra carpeta de manera local, copiarla y pegarla en la carpeta del código para ejecutarlo y listo. Luego al finalizar el trabajo borrar el archivo .env de la carpeta del código y luego hacer el commit.
Si instalan nuevas librerías poner este comando en la terminal para agregarlas a "requirements.txt": pip freeze > requirements.txt
