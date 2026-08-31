# api.py
from fastapi         import FastAPI, HTTPException, Depends
from sqlalchemy      import select, desc
from sqlalchemy.orm  import Session
from datetime        import datetime
from typing          import Optional
 
from models   import Lectura,Parameters
from database import engine, get_db
from models   import Base
 
 
app = FastAPI(title="Sensors IoT")
 
# Crea las tablas al iniciarse si es que no existen ya
Base.metadata.create_all(bind=engine)

 
# Endpoint POST que recibira la lectura del sensor MAX9814  
@app.post("/sensor/data")
async def inserir_lectura(
    body: dict,
    db:   Session = Depends(get_db)
):
    # Se comprueba que esten todos los campos
    camps = ["sensor", "valor", "unitat", "dispositiu"]
    for camp in camps:
        if camp not in body:
            raise HTTPException(
                status_code=400,
                detail="Falta el camp: " + camp
            )
 
    # Crea la instancia ORM con los datos recibidos
    nova = Lectura(
        sensor     = body["sensor"],
        valor      = body["valor"],
        unitat     = body["unitat"],
        dispositiu = body["dispositiu"],
        timestamp  = datetime.now().isoformat()
  
    )
 
    db.add(nova)       # añade a la sesión(INSERT pendiente)
    db.commit()        # ejecuta el INSERT y confirma
    db.refresh(nova)   # lee el id que SQLite le ha asignado
 
    # Regresa un diccionario — FastAPI lo serializa a JSON automaticamente
    return {
        "id":         nova.id,
        "sensor":     nova.sensor,
        "valor":      nova.valor,
        "unitat":     nova.unitat,
        "dispositiu": nova.dispositiu,
        "timestamp":  nova.timestamp
    }

energia_global = 0
prev_like = 0

# Endpoint GET para obtener el nivel y definir un estado para el ESP32_B
@app.get("/estado")
async def consultar_estado(
    db:     Session = Depends(get_db)
    ):

    # Se consulta datos de la tabla de Lectures
    # Construir la query: ORDER BY id DESC para obtener la mas reciente
    query = select(Lectura).order_by(desc(Lectura.id)).limit(1)
 
    # execute() envia la query a SQLite
    # scalars() desempaqueta los resultados como objetos a Lectura
    # first() muestra el primero o None si no hay resultados
    resultat = db.execute(query).scalars().first()

   
    global energia_global
    global prev_like

    # Se clasifican los valores en estados según la cantidad percibida
    nivel = resultat.valor
    if nivel < 25:
        estado = "chill"
        valor_estado = 0.2
    elif nivel < 50:
        estado = "flow"
        valor_estado = 0.3
    elif nivel < 75:
        estado = "rush"
        valor_estado = 0.4
    else:
        estado = "euphoria"
        valor_estado = 0.5

    
    #Se calcula la energía que en este caso es el valor actual de la barra para llegar al valor límite de la flor servo
    #El cálculo se hace en base a la cantidad de likes recibidos a traves sel streamlit 
    if actual_likes_global == prev_like:
        energia_global += valor_estado
    else:
        diferencia = actual_likes_global - prev_like
        energia_global +=  (diferencia + valor_estado)
        prev_like = actual_likes_global
    
    if energia_global > 100:
        energia_global = 100
    
    return {
        "estado": estado,
        "nivel": resultat.valor,
        "energia": energia_global
    }


actual_likes_global = 0
# Endpoint POST que recibira la lectura de datos ingresados en el streamlit la parte de likes
@app.post("/likes")
async def consultar_data(body: dict):
    global actual_likes_global
    camp = "actual_likes"
    if camp not in body:
        raise HTTPException(
            status_code=400,
            detail="No camp" 
        )
    actual_likes_global = body["actual_likes"]
 
    return {
        "actual_likes": actual_likes_global,
    }

@app.get("/actual")
async def recibir_likes():
    global actual_likes_global
    if actual_likes_global is None:
        actual_likes_global = 0
    return {
        "likes": actual_likes_global
    }

# Endpoint POST que recibira la lectura de datos ingresados en el streamlit la parte de aforo y limite de likes
@app.post("/limites")
async def consultar_data(
    body: dict,
    db:   Session = Depends(get_db)
):
    
    camps = ["likes_limit", "aforo"]
    for camp in camps:
        if camp not in body:
            raise HTTPException(
                status_code=400,
                detail="Falta el camp: " + camp
            )
 
    
    nova = Parameters(
        likes_limit            = body["likes_limit"],
        aforo                  = body["aforo"],
        timestamp              = datetime.now().isoformat()
  
    )
 
    db.add(nova)       
    db.commit()        
    db.refresh(nova)   
 
    
    return {
        "id":              nova.id,
        "likes_limit":     nova.likes_limit,
        "aforo":           nova.aforo,
        "timestamp":       nova.timestamp
    }

# endpoint GET para obtener el historial de los últimos 20 de la base de datos
@app.get("/sensor/historial")
async def historial(
    sensor: Optional[str] = None,
    limit:  int           = 20,
    db:     Session       = Depends(get_db)
):
    query = select(Lectura).order_by(desc(Lectura.id)).limit(limit)
 
    if sensor is not None:
        query = query.where(Lectura.sensor == sensor)
 
    # all() regresa una lista de todos los objetos
    resultats = db.execute(query).scalars().all()
 

    llista = []
    for r in resultats:
        llista.append({
            "id":         r.id,
            "sensor":     r.sensor,
            "valor":      r.valor,
            "unitat":     r.unitat,
            "dispositiu": r.dispositiu,
            "timestamp":  r.timestamp
        })
    return llista
