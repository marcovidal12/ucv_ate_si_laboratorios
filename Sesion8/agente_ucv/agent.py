from google.adk.agents.llm_agent import Agent

def explicar_concepto(concepto: str) -> dict:
    # RETO: Agregamos 5 nuevos conceptos (sistema, red, firewall, git, dns)
    conceptos = {
        "api": "Una API permite comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena información.",
        "sistema": "Un conjunto de elementos interrelacionados que trabajan por un objetivo común.",
        "red": "Conjunto de dispositivos interconectados que comparten recursos e información.",
        "firewall": "Sistema de seguridad que controla el tráfico de red entrante y saliente.",
        "git": "Sistema de control de versiones distribuido para rastrear cambios en el código.",
        "dns": "Sistema que traduce nombres de dominio legibles por humanos a direcciones IP."
    }
    
    concepto = concepto.lower().strip()
    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }
    return {
        "status": "not found",
        "explicacion": "Concepto no registrado."
    }

# RETO: Nueva tool para calcular el promedio de notas de la UCV
def calcular_promedio(nota1: float, nota2: float, nota3: float) -> dict:
    """
    Calcula el promedio final de tres notas del ciclo académico.
    """
    promedio = (nota1 + nota2 + nota3) / 3
    estado = "Aprobado" if promedio >= 10.5 else "Desaprobado"
    
    return {
        "promedio_final": round(promedio, 2),
        "estado": estado
    }

root_agent = Agent(
    model="gemini-flash-latest",
    name="agente_ucv",
    description="Agente académico UCV mejorado",
    instruction="""
    Eres un asistente académico experto en Ingeniería de Sistemas de la UCV.
    Responde siempre en español y usa un lenguaje simple y directo.
    Si te piden calcular un promedio de notas, usa la herramienta correspondiente.
    """,
    # RETO: Registramos ambas herramientas en el agente
    tools=[explicar_concepto, calcular_promedio],
)
