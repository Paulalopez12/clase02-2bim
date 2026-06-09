# Titulo de la serie con el promedio de edad de los actores de serie
from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todas las series con sus actores
series = session.query(Serie).all()

# Mostrar resultados usando el método obtener_edad_actores()
for serie in series:
    promedio = serie.obtener_edad_actores()
    print(f"Serie: {serie.titulo} - Promedio de edad: {promedio}")

session.close()

# titulo de la serie promedio de edades y ahora cuantos premios tiene esa serie

for serie in series:
    cantidad_premios = serie.obtener_premios_serie()
    print(f"Serie: {serie.titulo} - Cantidad de premios: {cantidad_premios}")