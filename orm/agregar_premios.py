import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Premio, Serie

Session = sessionmaker(bind=engine)
session = Session()

def cargar_premios():
    try:
        with open('../data/premios.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                serie = session.query(Serie).filter_by(titulo=row['serie']).first()

                # Evitar duplicar el premio exacto para la misma serie en el mismo año
                existe = session.query(Premio).filter_by(
                    nombre_premio=row['nombre_premio'], 
                    anio=int(row['anio']), 
                    serie_id=serie.id if serie else None
                ).first()
                
                if not existe:
                    nuevo_premio = Premio(
                        nombre_premio=row['nombre_premio'],
                        categoria=row['categoria'],
                        anio=int(row['anio']) if row['anio'] else None,
                        serie_id=serie.id if serie else None
                    )
                    session.add(nuevo_premio)
            
            session.commit()
            print("Premios cargados exitosamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al cargar premios: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    cargar_premios()