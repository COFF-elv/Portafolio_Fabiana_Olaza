#.venv \ Scripts\ activate
#uv run uvicorn api:app --host 0.0.0.0 --port 8080 --reload
''' Invoke-WebRequest -Uri http://localhost:8080/sensor/data `       
>>   -Method POST `
>>   -Headers @{ "Content-Type" = "application/json" } `
>>    -Body '{"sensor":"microfon","valor":5555}'
'''

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
 
# Crea les taules a l'arrencada si no existeixen
Base.metadata.create_all(bind=engine)

 
# Endpoint POST que recibira la lectura del sensor MAX9814  
@app.post("/sensor/data")
async def inserir_lectura(
    body: dict,
    db:   Session = Depends(get_db)
):
    # Validació manual: comprovem que hi siguin tots els camps
    camps = ["sensor", "valor", "unitat", "dispositiu"]
    for camp in camps:
        if camp not in body:
            raise HTTPException(
                status_code=400,
                detail="Falta el camp: " + camp
            )
 
    # Crear la instancia ORM amb les dades rebudes
    nova = Lectura(
        sensor     = body["sensor"],
        valor      = body["valor"],
        unitat     = body["unitat"],
        dispositiu = body["dispositiu"],
        timestamp  = datetime.now().isoformat()
  
    )
 
    db.add(nova)       # afegeix a la sessió (INSERT pendent)
    db.commit()        # executa el INSERT i confirma
    db.refresh(nova)   # llegeix l'id que SQLite ha assignat
 
    # Retornem un dict — FastAPI el serialitza a JSON automàticament
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
    # Construir la query: ORDER BY id DESC per obtenir la mes recent
    query = select(Lectura).order_by(desc(Lectura.id)).limit(1)
 
    # execute() envia la query a SQLite
    # scalars() desempaqueta els resultats com a objectes Lectura
    # first() retorna el primer o None si no hi ha resultats
    resultat = db.execute(query).scalars().first()


    global energia_global
    global prev_like


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
    # Retornem un dict — FastAPI el serialitza a JSON automàticament
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

# Endpoint POST que recibira la lectura de datos ingresados en el streamlit la parte de afooro y limite de likes
@app.post("/limites")
async def consultar_data(
    body: dict,
    db:   Session = Depends(get_db)
):
    # Validació manual: comprovem que hi siguin tots els camps
    camps = ["likes_limit", "aforo"]
    for camp in camps:
        if camp not in body:
            raise HTTPException(
                status_code=400,
                detail="Falta el camp: " + camp
            )
 
    # Crear la instancia ORM amb les dades rebudes
    nova = Parameters(
        likes_limit            = body["likes_limit"],
        aforo                  = body["aforo"],
        timestamp              = datetime.now().isoformat()
  
    )
 
    db.add(nova)       # afegeix a la sessió (INSERT pendent)
    db.commit()        # executa el INSERT i confirma
    db.refresh(nova)   # llegeix l'id que SQLite ha assignat
 
    # Retornem un dict — FastAPI el serialitza a JSON automàticament
    return {
        "id":              nova.id,
        "likes_limit":     nova.likes_limit,
        "aforo":           nova.aforo,
        "timestamp":       nova.timestamp
    }


@app.get("/sensor/historial")
async def historial(
    sensor: Optional[str] = None,
    limit:  int           = 20,
    db:     Session       = Depends(get_db)
):
    query = select(Lectura).order_by(desc(Lectura.id)).limit(limit)
 
    if sensor is not None:
        query = query.where(Lectura.sensor == sensor)
 
    # all() retorna una llista de tots els objectes Lectura
    resultats = db.execute(query).scalars().all()
 
    # llista local per construir la resposta JSON
    # (no és emulació de BD — les dades venen de SQLite via resultats)
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
