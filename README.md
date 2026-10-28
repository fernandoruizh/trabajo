# ASE262 Dashboard - T01

Dashboard web desarrollado con **Python** y **Flask** para visualizar y analizar datos conectados a **Google Sheets**.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Framework Web:** Flask
- **Integración:** Google Sheets API (`gspread` / `google-api-python-client`)
- **Control de Versiones:** Git y GitHub

---

## 📁 Estructura del Proyecto

```text
ASE262_Dashboard_T01/
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── templates/           # Plantillas HTML para Flask
├── .gitignore           # Archivos omitidos por Git (entornos, caché, llaves)
├── analisis.py          # Lógica y procesamiento de datos
├── app.py               # Servidor principal de Flask
├── conexion_sheets.py   # Configuración de conexión a Google Sheets
├── graficos.py          # Generación de gráficos visuales
├── README.md            # Documentación del proyecto
└── requirements.txt     # Lista de dependencias del proyecto