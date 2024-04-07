from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
# Definimos las funciones de Suma, Resta , Multiplicacion y Dividir
def sumar(entero1, entero2):
    return entero1 + entero2

def restar(entero1, entero2):
    return entero1 - entero2

def multiplicar(entero1, entero2):
    return entero1 * entero2

def dividir(entero1, entero2):
    if entero2 == 0:
        return "Error: División por cero"
    else:
        return entero1 / entero2

# Creamos la ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

# Registramos las funciones de las operaciones
dispatcher.register_function(
    "Sumar",
    sumar,
    returns={"resultado": int},
    args={"entero1": int, "entero2": int},
)

dispatcher.register_function(
    "Restar",
    restar,
    returns={"resultado": int},
    args={"entero1": int, "entero2": int},
)

dispatcher.register_function(
    "Multiplicar",
    multiplicar,
    returns={"resultado": int},
    args={"entero1": int, "entero2": int},
)

dispatcher.register_function(
    "Dividir",
    dividir,
    returns={"resultado": float},
    args={"entero1": int, "entero2": int},
)

# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()