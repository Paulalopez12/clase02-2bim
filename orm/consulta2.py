from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie

Session = sessionmaker(bind=engine)
session = Session()
series = session.query(Serie).all()

# titulo de la serie promedio de edades y ahora cuantos premios tiene esa serie
print("--- CONSULTA 2 ---")
for s in series:
    promedio = s.obtener_edad_actores()
    cantidad_premios = s.obtener_premios_serie()
    print(f"Título: {s.titulo} - Promedio de Edad: {promedio} - Total Premios: {cantidad_premios}")
    
session.close()