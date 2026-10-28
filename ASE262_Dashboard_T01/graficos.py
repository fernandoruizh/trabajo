import plotly.graph_objects as go

# 1. IMPORTAMOS LAS 6 FUNCIONES DE TU EQUIPO
from analisis import (
    agrupar_dias_por_departamento,       # Patrick G.
    contar_solicitudes_por_estado,      # Patrick G.
    contar_solicitudes_por_departamento, # Fernando R.
    promedio_dias_por_estado,           # Fernando R.
    agrupar_solicitudes_por_estado,     # Dayana A.
    contar_vacaciones_prolongadas       # Dayana A.
)

from conexion_sheets import obtener_datos


# PALETA DE COLORES
colores = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899", "#6366F1"]


# 1. GRÁFICO DE BARRAS: DÍAS SOLICITADOS POR DEPARTAMENTO (Patrick)
def grafico_dias_departamento(datos):
    resumen = agrupar_dias_por_departamento(datos)
    areas = list(resumen.keys())
    dias = list(resumen.values())

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=areas,
        y=dias,
        marker_color=[colores[i % len(colores)] for i in range(len(areas))],
        text=dias,
        textposition="auto",
        hovertemplate="Área: %{x}<br>Días solicitados: %{y}<extra></extra>"
    ))

    fig.update_layout(
        title="1. Días de vacaciones solicitados por área",
        xaxis_title="Área / Departamento",
        yaxis_title="Total Días",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=50, r=30, t=70, b=50),
        showlegend=False
    )
    return fig


# 2. GRÁFICO DE DONA: SOLICITUDES POR ESTADO (Dayana)
def grafico_solicitudes_estado(datos):
    resumen = agrupar_solicitudes_por_estado(datos)
    estados = list(resumen.keys())
    cantidades = list(resumen.values())

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=estados,
        values=cantidades,
        hole=0.60,
        marker=dict(colors=colores),
        textinfo="label+percent",
        hovertemplate="Estado: %{label}<br>Solicitudes: %{value}<br>Porcentaje: %{percent}<extra></extra>"
    ))

    fig.update_layout(
        title="2. Distribución de solicitudes por estado",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=30, r=30, t=70, b=30),
        showlegend=False
    )
    return fig


# 3. GRÁFICO DE BARRAS HORIZONTALES: SOLICITUDES POR DEPARTAMENTO (Fernando)
def grafico_solicitudes_departamento(datos):
    resumen = contar_solicitudes_por_departamento(datos)
    areas = list(resumen.keys())
    cantidades = list(resumen.values())

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cantidades,
        y=areas,
        orientation="h",
        marker_color="#10B981",
        text=cantidades,
        textposition="auto",
        hovertemplate="Área: %{y}<br>Total Solicitudes: %{x}<extra></extra>"
    ))

    fig.update_layout(
        title="3. Total de solicitudes enviadas por departamento",
        xaxis_title="N° de Solicitudes",
        yaxis_title="Área / Departamento",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=80, r=30, t=70, b=50),
        showlegend=False
    )
    return fig


# 4. GRÁFICO DE BARRAS: PROMEDIO DE DÍAS POR ESTADO (Fernando)
def grafico_promedio_dias_estado(datos):
    estados = ["Aprobado", "Pendiente", "Rechazado"]
    promedios = [promedio_dias_por_estado(datos, est) for est in estados]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=estados,
        y=promedios,
        marker_color="#8B5CF6",
        text=[f"{p:.1f} días" for p in promedios],
        textposition="auto",
        hovertemplate="Estado: %{x}<br>Promedio: %{y:.1f} días<extra></extra>"
    ))

    fig.update_layout(
        title="4. Promedio de días pedidos según el estado",
        xaxis_title="Estado",
        yaxis_title="Promedio de Días",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=50, r=30, t=70, b=50),
        showlegend=False
    )
    return fig


# 5. GRÁFICO INDICADOR: VACACIONES PROLONGADAS >= 10 DÍAS (Dayana)
def grafico_vacaciones_prolongadas(datos):
    cantidad = contar_vacaciones_prolongadas(datos, dias_limite=10)

    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="number",
        value=cantidad,
        title={"text": "Solicitudes Prolongadas (≥ 10 Días)"},
        number={"font": {"size": 70, "color": "#F59E0B"}}
    ))

    fig.update_layout(
        title="5. Alerta de vacaciones prolongadas",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=30, r=30, t=70, b=30)
    )
    return fig


# 6. GRÁFICO COMPARATIVO: CONTEO POR ESTADO ESPECÍFICO (Patrick)
def grafico_comparativo_aprobadas(datos):
    aprobadas = contar_solicitudes_por_estado(datos, "Aprobado")
    rechazadas = contar_solicitudes_por_estado(datos, "Rechazado")
    pendientes = contar_solicitudes_por_estado(datos, "Pendiente")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Aprobadas", "Pendientes", "Rechazadas"],
        y=[aprobadas, pendientes, rechazadas],
        marker_color=["#10B981", "#F59E0B", "#EF4444"],
        text=[aprobadas, pendientes, rechazadas],
        textposition="auto",
        hovertemplate="Estado: %{x}<br>Cantidad: %{y}<extra></extra>"
    ))

    fig.update_layout(
        title="6. Conteo de solicitudes por estado específico",
        xaxis_title="Estado",
        yaxis_title="Cantidad de Solicitudes",
        template="plotly_white",
        autosize=True,
        height=400,
        margin=dict(l=50, r=30, t=70, b=50),
        showlegend=False
    )
    return fig


# BLOQUE DE PRUEBA LOCAL
if __name__ == "__main__":
    datos = obtener_datos()

    grafico_dias_departamento(datos).show()
    grafico_solicitudes_estado(datos).show()
    grafico_solicitudes_departamento(datos).show()
    grafico_promedio_dias_estado(datos).show()
    grafico_vacaciones_prolongadas(datos).show()
    grafico_comparativo_aprobadas(datos).show()