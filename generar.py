import csv
import random
from datetime import datetime, timedelta

def generar_id(prefijo, longitud_numeros=4):
    """Genera un ID con números aleatorios seguidos de tres letras constantes"""
    numeros = ''.join([str(random.randint(0, 9)) for _ in range(longitud_numeros)])
    return f"{numeros}{prefijo}"

def fecha_aleatoria(inicio, fin):
    """Genera una fecha aleatoria entre dos fechas"""
    delta = fin - inicio
    dias_aleatorios = random.randrange(delta.days)
    return (inicio + timedelta(days=dias_aleatorios)).strftime('%Y-%m-%d')

def generar_telefono():
    """Genera un número de teléfono español"""
    return f"+34 {random.randint(600, 799)} {random.randint(100, 999)} {random.randint(100, 999)}"

def generar_email(nombre):
    """Genera un email aleatorio"""
    dominios = ['gmail.com', 'hotmail.com', 'live.es', 'outlook.com']
    return f"{nombre.lower().replace(' ', '')}{random.randint(1, 999)}@{random.choice(dominios)}"

def generar_dni():
    """Genera un DNI español"""
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    numero = random.randint(10000000, 99999999)
    return f"{numero}{letras[numero % 23]}"

def generar_cif():
    """Genera un CIF español"""
    letras_inicio = 'ABCDEFGHJNPQRSUVW'
    letra = random.choice(letras_inicio)
    numeros = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    digito_control = random.randint(0, 9)
    return f"{letra}{numeros}{digito_control}"

# CSV 1: VEHÍCULOS (14 campos)
def generar_csv_vehiculos(nombre_archivo='vehiculos.csv', num_registros=50):
    marcas = ['Toyota', 'Ford', 'Volkswagen', 'Seat', 'Renault', 'Peugeot', 'BMW', 'Mercedes', 'Audi', 'Nissan']
    etiquetas = ['CSVModificacion']
    colores = ['Blanco', 'Negro', 'Gris', 'Azul', 'Rojo', 'Verde', 'Plata']
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8', delimiter=';') as file:
        writer = csv.writer(file)
        # Encabezados (14 campos)
        writer.writerow([
            'Matricula', 'Marca', 'Modelo', 'Color', 'Notas', 'Etiqueta', 
            'TarjetaIdentificacion', 'Telefono', 'Email', 'CodigoAcreditacion',
            'FechaInicioAcreditacion', 'FechaFinAcreditacion', 'DNI_Titular', 'Estado'
        ])
        
        fecha_inicio = datetime(2024, 1, 1)
        fecha_fin = datetime(2025, 12, 31)
        
        for _ in range(num_registros):
            matricula = generar_id('CAR', 4)
            marca = random.choice(marcas)
            modelo = f"{marca} {random.choice(['Sedan', 'SUV', 'Compact', 'Sport', 'Coupe'])}"
            color = random.choice(colores)
            notas = random.choice(['En buen estado', 'Requiere revisión', 'Nuevo', 'Mantenimiento programado', ''])
            etiqueta = random.choice(etiquetas)
            tarjeta = generar_id('TRJ', 6)
            telefono = generar_telefono()
            email = generar_email(f"vehiculo{random.randint(1, 1000)}")
            codigo_acred = generar_id('ACR', 5)
            fecha_inicio_acred = fecha_aleatoria(fecha_inicio, datetime(2025, 6, 1))
            fecha_fin_acred = fecha_aleatoria(datetime(2025, 6, 1), fecha_fin)
            dni = generar_dni()
            estado = random.choice(['Activo', 'Inactivo', 'En revisión', 'Pendiente'])
            
            writer.writerow([
                matricula, marca, modelo, color, notas, etiqueta, tarjeta,
                telefono, email, codigo_acred, fecha_inicio_acred, 
                fecha_fin_acred, dni, estado
            ])
    
    print(f"✓ CSV de vehículos generado: {nombre_archivo} ({num_registros} registros, 14 campos)")

# CSV 2: EMPRESA (6 campos)
def generar_csv_empresa(nombre_archivo='empresa.csv', num_registros=50):
    sectores = ['Tecnología', 'Construcción', 'Servicios', 'Comercio', 'Industria', 'Consultoría']
    nombres_empresa = ['CedroSL', 'CerezoSL', 'CirueloSL', 'AguacateSL']
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8', delimiter=';') as file:
        writer = csv.writer(file)
        # Encabezados (6 campos)
        writer.writerow([
            'ID_Empresa', 'NombreEmpresa', 'CIF', 'Sector', 'Telefono', 'Email'
        ])
        
        for _ in range(num_registros):
            id_empresa = generar_id('EMP', 4)
            nombre = f"{random.choice(nombres_empresa)} {random.choice(['S.L.', 'S.A.', 'S.L.U.'])}"
            cif = generar_cif()
            sector = random.choice(sectores)
            telefono = generar_telefono()
            email = generar_email(f"contacto{random.randint(1, 999)}")
            
            writer.writerow([
                id_empresa, nombre, cif, sector, telefono, email
            ])
    
    print(f"✓ CSV de empresa generado: {nombre_archivo} ({num_registros} registros, 6 campos)")

# CSV 3: PERSONA (12 campos - ajustar a 14 si confirmas los campos)
def generar_csv_persona(nombre_archivo='persona.csv', num_registros=50):
    nombres = ['Juan', 'María', 'Carlos', 'Ana', 'Pedro', 'Laura', 'Luis', 'Carmen', 'José', 'Isabel']
    apellidos = ['García', 'Rodríguez', 'López', 'Martínez', 'González', 'Pérez', 'Sánchez', 'Fernández']
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8', delimiter=';') as file:
        writer = csv.writer(file)
        # Encabezados (12 campos - puedo ampliarlo a 14 si me confirmas qué campos faltan)
        writer.writerow([
            'ID_Persona', 'Nombre', 'Apellidos', 'DNI', 'FechaNacimiento',
            'Telefono', 'Email', 'Direccion', 'CodigoPostal', 'Ciudad', 
            'Provincia', 'Estado'
        ])
        
        fecha_inicio = datetime(1950, 1, 1)
        fecha_fin = datetime(2005, 12, 31)
        
        ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Málaga', 'Santander']
        provincias = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Vizcaya', 'Málaga', 'Cantabria']
        
        for i in range(num_registros):
            id_persona = generar_id('PER', 5)
            nombre = random.choice(nombres)
            apellido = f"{random.choice(apellidos)} {random.choice(apellidos)}"
            dni = generar_dni()
            fecha_nacimiento = fecha_aleatoria(fecha_inicio, fecha_fin)
            telefono = generar_telefono()
            email = generar_email(nombre)
            direccion = f"Calle {random.choice(['Mayor', 'Real', 'Sol', 'Luna'])} {random.randint(1, 100)}"
            codigo_postal = f"{random.randint(10000, 52999):05d}"
            ciudad_idx = random.randint(0, len(ciudades)-1)
            ciudad = ciudades[ciudad_idx]
            provincia = provincias[ciudad_idx]
            estado = random.choice(['Activo', 'Inactivo', 'Pendiente verificación'])
            
            writer.writerow([
                id_persona, nombre, apellido, dni, fecha_nacimiento,
                telefono, email, direccion, codigo_postal, ciudad,
                provincia, estado
            ])
    
    print(f"✓ CSV de persona generado: {nombre_archivo} ({num_registros} registros, 12 campos)")

# Ejecutar la generación de los tres CSV
if __name__ == "__main__":
    print("Generando archivos CSV...\n")
    
    generar_csv_vehiculos('vehiculos.csv', 50)
    generar_csv_empresa('empresa.csv', 50)
    generar_csv_persona('persona.csv', 50)
    
    print("\n¡Todos los archivos CSV han sido generados exitosamente!")