# Importa cliente da OpenAI
from openai import OpenAI

# Cria cliente usando a chave do ambiente
client = OpenAI()


def generate_feedback(score, total_questions):

  
   
    if total_questions == 0:
        return "Não há dados suficientes para gerar feedback."

   
    # CALCULA PORCENTAGEM
   
    percentage = (score / total_questions) * 100

    
    # TENTA USAR IA
    
    try:

        # Prompt para IA (contexto pedagógico)
        prompt = f"""
        Você é um especialista em alfabetização infantil.

        Uma criança respondeu um quiz de palavras.

        Resultado:
        - Acertos: {score}
        - Total: {total_questions}
        - Percentual: {percentage:.2f}%

        Gere um feedback pedagógico curto para o professor contendo:
        - Pontos positivos
        - Dificuldades
        - Sugestões de melhoria

        Use linguagem simples e acolhedora.
        Responda em português.
        """

        # Chamada para OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um pedagogo especialista em alfabetização infantil."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Extrai resposta da IA
        feedback = response.choices[0].message.content

        return feedback

    except Exception as e:
        print("Erro ao usar IA:", e)


        if percentage >= 80:
            return (
                "A criança apresentou ótimo desempenho "
                "e boa compreensão das palavras."
            )

        elif percentage >= 50:
            return (
                "A criança demonstrou progresso, "
                "mas ainda possui dificuldades."
            )

        else:
            return (
                "A criança precisa de maior reforço "
                "nas atividades de alfabetização."
            )