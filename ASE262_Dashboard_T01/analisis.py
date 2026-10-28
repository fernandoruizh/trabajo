from datetime import datetime
from conexion_sheets import obtener_datos


# Y luego ejecutas la función para guardar la información en 'datos':
datos = obtener_datos()


# ==========================================
# FUNCIONES AUXILIARES PARA DATOS DE SHEETS
# ==========================================




def calcular_dias_solicitud(fila):
    """Calcula la cantidad total de días restando Fecha final menos Fecha inicio."""
    f_inicio_str = fila.get("Fecha inicio - 1ra Alternativa")
    f_fin_str = fila.get("Fecha final - 1ra Alternativa")


    if not f_inicio_str or not f_fin_str:
        return 0


    formatos = ["%d/%m/%Y %H:%M:%S", "%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"]
    fecha_inicio, fecha_fin = None, None


    for fmt in formatos:
        try:
            if not fecha_inicio:
                fecha_inicio = datetime.strptime(
                    str(f_inicio_str).strip(), fmt
                )
            if not fecha_fin:
                fecha_fin = datetime.strptime(str(f_fin_str).strip(), fmt)
        except ValueError:
            pass


    if fecha_inicio and fecha_fin:
        # Sumamos 1 día para incluir el día de inicio completo
        dias = (fecha_fin - fecha_inicio).days + 1
        return max(dias, 0)


    return 0




def obtener_estado(fila):
    """Obtiene el estado de la solicitud o asigna 'Aprobado' por defecto."""
    estado = (
        fila.get("Estado")
        or fila.get("Estado de la solicitud")
        or fila.get("Columna 1")
    )
    if not estado or str(estado).strip() == "":
        return "Aprobado"
    return str(estado).strip()




# ==========================================
# PATRICK G.
# ==========================================




def contar_solicitudes_por_estado(datos, estado="Aprobado"):
    """Cuenta cuántas solicitudes de vacaciones se encuentran en un estado específico."""
    return sum(
        1
        for fila in datos
        if obtener_estado(fila).lower() == str(estado).lower()
    )




def agrupar_dias_por_departamento(datos):
    """Suma la cantidad total de días de vacaciones solicitados agrupándolos por departamento/área."""
    resultado = {}
    for fila in datos:
        area = fila.get("Área", "Sin Área")
        dias = calcular_dias_solicitud(fila)
        if area:
            resultado[area] = resultado.get(area, 0) + dias
    return resultado




# ==========================================
# FERNANDO R.
# ==========================================




def contar_solicitudes_por_departamento(datos):
    """Cuenta cuántas solicitudes de vacaciones en total se han enviado agrupadas por área/departamento."""
    resultado = {}
    for fila in datos:
        area = fila.get("Área", "Sin Área")
        if area:
            resultado[area] = resultado.get(area, 0) + 1
    return resultado




def promedio_dias_por_estado(datos, estado="Aprobado"):
    """Calcula el promedio de días pedidos según el estado de la solicitud."""
    dias_filtrados = [
        calcular_dias_solicitud(fila)
        for fila in datos
        if obtener_estado(fila).lower() == str(estado).lower()
    ]
    if not dias_filtrados:
        return 0.0
    return sum(dias_filtrados) / len(dias_filtrados)




# ==========================================
# DAYANA A.
# ==========================================




def contar_vacaciones_prolongadas(datos, dias_limite=10):
    """Filtra y cuenta las solicitudes donde el empleado pide periodos iguales o mayores a 10 días."""
    return sum(
        1 for fila in datos if calcular_dias_solicitud(fila) >= dias_limite
    )




def agrupar_solicitudes_por_estado(datos):
    """Genera un conteo consolidado de cuántas solicitudes hay en cada estado dentro de la base de datos."""
    resultado = {}
    for fila in datos:
        est = obtener_estado(fila)
        resultado[est] = resultado.get(est, 0) + 1
    return resultado




# ==========================================
# EJECUCIÓN E IMPRESIÓN DE RESULTADOS
# ==========================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("      RESULTADOS CON DATOS DE GOOGLE SHEETS      ")
    print("=" * 50)


    print("\n--- PATRICK G. ---")
    print(
        "1. Solicitudes 'Aprobado':",
        contar_solicitudes_por_estado(datos, "Aprobado"),
    )
    print("2. Días agrupados por Área:", agrupar_dias_por_departamento(datos))


    print("\n--- FERNANDO R. ---")
    print(
        "3. Solicitudes por Área/Departamento:",
        contar_solicitudes_por_departamento(datos),
    )
    print(
        "4. Promedio de días (Aprobado):",
        round(promedio_dias_por_estado(datos, "Aprobado"), 2),
    )


    print("\n--- DAYANA A. ---")
    print(
        "5. Vacaciones prolongadas (>=10 días):",
        contar_vacaciones_prolongadas(datos),
    )
    print("6. Conteo por estado:", agrupar_solicitudes_por_estado(datos))


    print("=" * 50 + "\n")

