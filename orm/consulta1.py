# Titulo de la serie con el promedio de edad de los actores de serie
from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie

Session = sessionmaker(bind=engine)
session = Session()

# Traemos todas las series
series = session.query(Serie).all()

for s in series:
    # Llamamos únicamente al método de los actores
    promedio = s.obtener_edad_actores()
    print(f"Serie: {s.titulo} - Promedio de edad: {promedio}")
session.close()