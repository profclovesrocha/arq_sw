from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime

load_dotenv()

#CONFIGURAÇÕES 
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

# ================== BANCO DE DADOS (Camada de Dados) ==================
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    username = Column(String(100))
    message = Column(Text)
    ai_response = Column(Text)
    status = Column(String(20), default='aberto')
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# ================== CLIENTE DA IA (Camada de Serviços Externos) ==================
groq_client = Groq(api_key=GROQ_API_KEY)

# ================== FUNÇÕES DO BOT ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Olá! Eu sou o chatbot de suporte técnico.\n"
        "Manda sua dúvida que eu te ajudo!\n"
        "Todos os chamados são salvos automaticamente no MySQL."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user = update.message.from_user
    user_id = str(user.id)
    username = user.username or user.first_name or "Desconhecido"

    print(f"📩 Novo chamado de {username} ({user_id}): {user_message}")

    # Camada de Aplicação: chama a IA
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{
                "role": "user",
                "content": f"Você é um atendente de suporte técnico amigável. Responda em português brasileiro de forma clara e útil: {user_message}"
            }],
            temperature=0.7,
            max_tokens=600
        )
        ai_reply = response.choices[0].message.content
    except Exception as e:
        ai_reply = "Desculpe, estou com um probleminha agora. Tenta de novo em alguns segundos! 😅"

    # Camada de Dados: salva no MySQL
    session = Session()
    try:
        ticket = Ticket(
            user_id=user_id,
            username=username,
            message=user_message,
            ai_response=ai_reply
        )
        session.add(ticket)
        session.commit()
        print(f"✅ Chamado salvo no banco com ID {ticket.id}")
    except Exception as e:
        print(f"⚠️ Erro ao salvar no banco: {e}")
    finally:
        session.close()

    # Responde o usuário
    await update.message.reply_text(ai_reply)

# ================== INICIALIZAÇÃO ==================
def main():
    print("🚀 Bot de suporte iniciado com sucesso!")
    print("Telegram + Groq + MySQL tudo integrado!")
    print("Aguardando mensagens... (pressione Ctrl+C para parar)")

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()