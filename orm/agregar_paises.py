import csv
from sqlalchemy.orm import sessionmaker
from modelo import engine, Pais

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

def cargar_paises():
    try:
        with open('../data/paises.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Verificar si ya existe para evitar duplicados
                existe = session.query(Pais).filter_by(nombre=row['nombre']).first()
                if not existe:
                    nuevo_pais = Pais(
                        nombre=row['nombre'],
                        continente=row['continente']
                    )
                    session.add(nuevo_pais)
            
            session.commit()
            print("Países cargados exitosamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al cargar países: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    cargar_paises()