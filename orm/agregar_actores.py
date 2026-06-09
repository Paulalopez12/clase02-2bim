import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Actor, Pais, Serie

Session = sessionmaker(bind=engine)
session = Session()

def cargar_actores():
    try:
        with open('../data/actores.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pais = session.query(Pais).filter_by(nombre=row['pais']).first()
                serie = session.query(Serie).filter_by(titulo=row['serie']).first()

                # Evitar duplicar actor en la misma serie
                existe = session.query(Actor).filter_by(nombre=row['nombre'], serie_id=serie.id if serie else None).first()
                
                if not existe:
                    nuevo_actor = Actor(
                        nombre=row['nombre'],
                        edad=int(row['edad']) if row['edad'] else None,
                        rol=row.get('rol', 'No especificado'),
                        pais_id=pais.id if pais else None,
                        serie_id=serie.id if serie else None
                    )
                    session.add(nuevo_actor)
            
            session.commit()
            print("Actores cargados exitosamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al cargar actores: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    cargar_actores()