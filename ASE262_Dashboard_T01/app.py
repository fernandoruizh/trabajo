# IMPORTAR FLASK
from flask import Flask, render_template

# IMPORTAR LA CONEXIÓN CON GOOGLE SHEETS
from conexion_sheets import obtener_datos

# IMPORTAR LAS FUNCIONES DE ANÁLISIS DE TU EQUIPO
from analisis import (
    contar_solicitudes_por_estado,        # Patrick G.
    agrupar_dias_por_departamento,         # Patrick G.
    contar_solicitudes_por_departamento,   # Fernando R.
    promedio_dias_por_estado,             # Fernando R.
    contar_vacaciones_prolongadas,         # Dayana A.
    agrupar_solicitudes_por_estado        # Dayana A.
)

# IMPORTAR LOS 6 GRÁFICOS
from graficos import (
    grafico_dias_departamento,
    grafico_solicitudes_estado,
    grafico_solicitudes_departamento,
    grafico_promedio_dias_estado,
    grafico_vacaciones_prolongadas,
    grafico_comparativo_aprobadas
)


# 1. CREAR LA APLICACIÓN FLASK
app = Flask(__name__)


# 2. DEFINIR LA RUTA PRINCIPAL
@app.route("/")
def dashboard():

    # 3. OBTENER LOS DATOS DESDE GOOGLE SHEETS
    datos = obtener_datos()

    # 4. CALCULAR INDICADORES KPI
    total_solicitudes = len(datos)
    total_aprobadas = contar_solicitudes_por_estado(datos, "Aprobado")
    total_prolongadas = contar_vacaciones_prolongadas(datos, dias_limite=10)

    # 5. GENERAR LOS 6 GRÁFICOS INTERACTIVOS
    fig1 = grafico_dias_departamento(datos)
    fig2 = grafico_solicitudes_estado(datos)
    fig3 = grafico_solicitudes_departamento(datos)
    fig4 = grafico_promedio_dias_estado(datos)
    fig5 = grafico_vacaciones_prolongadas(datos)
    fig6 = grafico_comparativo_aprobadas(datos)

    # 6. CONVERTIR LOS GRÁFICOS A HTML
    grafico1 = fig1.to_html(full_html=False, include_plotlyjs=False)
    grafico2 = fig2.to_html(full_html=False, include_plotlyjs=False)
    grafico3 = fig3.to_html(full_html=False, include_plotlyjs=False)
    grafico4 = fig4.to_html(full_html=False, include_plotlyjs=False)
    grafico5 = fig5.to_html(full_html=False, include_plotlyjs=False)
    grafico6 = fig6.to_html(full_html=False, include_plotlyjs=False)

    # 7. ENVIAR LOS RESULTADOS A dashboard.html
    return render_template(
        "dashboard.html",
        total_solicitudes=total_solicitudes,
        total_aprobadas=total_aprobadas,
        total_prolongadas=total_prolongadas,
        grafico1=grafico1,
        grafico2=grafico2,
        grafico3=grafico3,
        grafico4=grafico4,
        grafico5=grafico5,
        grafico6=grafico6
    )


# 8. EJECUTAR LA APLICACIÓN
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
