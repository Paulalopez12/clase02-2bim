import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Plataforma, Pais

Session = sessionmaker(bind=engine)
session = Session()

def cargar_plataformas():
    try:
        with open('../data/plataformas.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existe = session.query(Plataforma).filter_by(nombre=row['nombre']).first()
                if not existe:
                    # Buscar el país por nombre
                    pais = session.query(Pais).filter_by(nombre=row['pais']).first()
                    
                    if pais:
                        nueva_plataforma = Plataforma(
                            nombre=row['nombre'],
                            pais_id=pais.id,
                            suscriptores_millones=float(row['suscriptores_millones'])
                        )
                        session.add(nueva_plataforma)
                    else:
                        print(f"País '{row['pais']}' no encontrado")
            
            session.commit()
            print("Plataformas cargadas exitosamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al cargar plataformas: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    cargar_plataformas()