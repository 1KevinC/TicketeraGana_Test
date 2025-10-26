        Archivos creados:
        - requirements.txt
        - build.sh
        - Procfile  (usa módulo: asgiref)

        Parches generados para settings.py (no sobrescriben nada automáticamente):
        [
  {
    "original": "/mnt/data/work_ticketera/TicketeraGana-proyecto-/config/settings.py",
    "patched": "/mnt/data/work_ticketera/TicketeraGana-proyecto-/config/settings.render.patch.py"
  }
]

        Instrucciones rápidas:
        1) Copia requirements.txt, build.sh y Procfile a la raíz del repo.
        2) Abre el archivo *.render.patch.py correspondiente y aplica los cambios en tu settings.py,
           o renómbralo a settings.py si quieres reemplazar por completo.
        3) En Render:
           - Build Command: bash ./build.sh
           - Start Command: gunicorn asgiref.wsgi:application --bind 0.0.0.0:$PORT
           - Env: DATABASE_URL, SECRET_KEY, DEBUG=False, ALLOWED_HOSTS=<tu_servicio.onrender.com>
