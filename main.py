from fastapi import FastAPI
import scraper
from database import criar_tabela, salvar_valor

criar_tabela()

app = FastAPI(title="Meu Monitor Fiscal")

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
    