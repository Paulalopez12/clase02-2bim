# Titulo de la serie con el promedio de edad de los actores de serie
from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie

Session = sessionmaker(bind=engine)
session = Session()


series = session.query(Serie).all()

for s in series:
    
    promedio = s.obtener_edad_actores()
    print(f"Serie: {s.titulo} - Promedio de edad: {promedio}")
session.close()