class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_aprobacion(self):
        return self.calificacion >= 60

nombre_estudiante = input("Ingresa el Nombre del estudiante: ")
edad_estudiante = int(input("Ingresa la edad del estudiante: "))
calificacion_estudiante = float(input("Ingresa la nota del estudiante: "))


estudiante1 = Estudiante(nombre_estudiante, edad_estudiante, calificacion_estudiante)

print(f"Estudiante: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad} años")
print(f"Calificación: {estudiante1.calificacion}")

if estudiante1.verificar_aprobacion():
    print("El estudiante ha aprobado.")
else:
    print("El estudiante no ha aprobado.")