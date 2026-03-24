from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Session, create_engine, select, Field
from typing import Optional
from datetime import datetime

# Configuração do Banco de Dados (SQLite para teste, use Postgres para produção)
sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url)

class Vaga(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    horario: datetime
    paciente_cpf: Optional[str] = None
    disponivel: bool = Field(default=True)

# Cria as tabelas ao iniciar
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/agendar/{vaga_id}")
def agendar(vaga_id: int, cpf: str):
    with Session(engine) as session:
        # Busca a vaga específica
        statement = select(Vaga).where(Vaga.id == vaga_id)
        vaga = session.exec(statement).first()

        if not vaga or not vaga.disponivel:
            raise HTTPException(status_code=400, detail="Vaga indisponível ou inexistente")

        # Realiza o agendamento
        vaga.paciente_cpf = cpf
        vaga.disponivel = False
        
        session.add(vaga)
        session.commit() # Salva no banco de forma segura
        session.refresh(vaga)
        return {"status": "Agendado", "vaga": vaga}