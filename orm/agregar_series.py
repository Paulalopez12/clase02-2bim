import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Serie, Plataforma, Pais

Session = sessionmaker(bind=engine)
session = Session()

def cargar_series():
    try:
        with open('../data/series.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Relaciones de Llaves Foráneas
                plataforma = session.query(Plataforma).filter_by(nombre=row['plataforma']).first()
                pais = session.query(Pais).filter_by(nombre=row['pais']).first()

                # Evitar duplicar la misma serie en la misma plataforma
                existe = session.query(Serie).filter_by(titulo=row['titulo'], plataforma_id=plataforma.id if plataforma else None).first()
                
                if not existe:
                    nueva_serie = Serie(
                        titulo=row['titulo'],
                        genero=row['genero'],
                        anio_estreno=int(row['anio_estreno']) if row['anio_estreno'] else None,
                        temporadas=int(row['temporadas']) if row['temporadas'] else None,
                        plataforma_id=plataforma.id if plataforma else None,
                        pais_id=pais.id if pais else None
                    )
                    session.add(nueva_serie)
            
            session.commit()
            print("Series cargadas exitosamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al cargar series: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    cargar_series()