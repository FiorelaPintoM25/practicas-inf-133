from zeep import Client

client = Client('http://localhost:8000')
result1 = client.service.Sumar(entero1=10, entero2=5)
result2 = client.service.Restar(entero1=10, entero2=5)
result3 = client.service.Multiplicar(entero1=10, entero2=5)
result4 = client.service.Dividir(entero1=10, entero2=5)
print("Suma =>",result1)
print("Resta =>",result2)
print("Multiplicacion =>",result3)
print("Division =>",result4)