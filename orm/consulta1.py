# Titulo de la serie con el promedio de edad de los actores de serie
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie, Actor

Session = sessionmaker(bind=engine)
session = Session()

# Consulta: Título de serie con promedio de edad de actores
resultado = session.query(
    Serie.titulo,
    func.avg(Actor.edad).label('promedio_edad')
).join(
    Actor, Serie.id == Actor.serie_id
).group_by(
    Serie.titulo
).all()

# Mostrar resultados
for serie, promedio in resultado:
    print(f"Serie: {serie} - Promedio de edad: {promedio:.2f}")

session.close()