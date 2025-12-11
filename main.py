from fastapi import FastAPI
import scraper
from fastapi.middleware.cors import CORSMiddleware
from database import criar_tabela, salvar_valor

criar_tabela()

app = FastAPI(title="Meu Monitor Fiscal")

origins = [
    "http://localhost:5173", # O endereço do seu React
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite qualquer origem (facilitador para dev)
    allow_credentials=True,
    allow_methods=["*"], # Permite GET, POST, etc.
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "API está rodando!"}

@app.get('/dolar')
def pegar_cotacao_dolar():
    try:
        valor = scraper.buscar_dolar()
        salvar_valor(valor)
        return {"moeda": "dolar", "valor": valor}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get('/euro')
def pegar_cotacao_euro():
    try:
        valor = scraper.buscar_euro()
        salvar_valor(valor)
        return {"moeda": "euro", "valor": valor}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))