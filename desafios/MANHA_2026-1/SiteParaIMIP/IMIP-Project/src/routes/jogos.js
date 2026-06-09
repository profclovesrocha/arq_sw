const express = require('express');
const router = express.Router();
const Groq = require('groq-sdk');

const client = new Groq({ apiKey: process.env.GROQ_API_KEY });

const historico = {
    frase: [],
    letra: [],
    imagem: []
};

const palavrasLetra = [
    { emoji: '🐶', palavra: 'Cachorro' },
    { emoji: '🐱', palavra: 'Gato' },
    { emoji: '🐰', palavra: 'Coelho' },
    { emoji: '🦊', palavra: 'Raposa' },
    { emoji: '🐻', palavra: 'Urso' },
    { emoji: '🐯', palavra: 'Tigre' },
    { emoji: '🦁', palavra: 'Leão' },
    { emoji: '🐮', palavra: 'Vaca' },
    { emoji: '🐷', palavra: 'Porco' },
    { emoji: '🐸', palavra: 'Sapo' },
    { emoji: '🐵', palavra: 'Macaco' },
    { emoji: '🐴', palavra: 'Cavalo' },
    { emoji: '🐢', palavra: 'Tartaruga' },
    { emoji: '🐬', palavra: 'Golfinho' },
    { emoji: '🍎', palavra: 'Maçã' },
    { emoji: '🍊', palavra: 'Laranja' },
    { emoji: '🍌', palavra: 'Banana' },
    { emoji: '🍉', palavra: 'Melancia' },
    { emoji: '🍓', palavra: 'Morango' },
    { emoji: '🍇', palavra: 'Uva' },
    { emoji: '🥕', palavra: 'Cenoura' },
    { emoji: '🌽', palavra: 'Milho' },
    { emoji: '🥔', palavra: 'Batata' },
    { emoji: '🚗', palavra: 'Carro' },
    { emoji: '✈️', palavra: 'Avião' },
    { emoji: '🚲', palavra: 'Bicicleta' },
    { emoji: '🎂', palavra: 'Bolo' },
    { emoji: '🌞', palavra: 'Sol' },
    { emoji: '🌙', palavra: 'Lua' },
    { emoji: '⭐', palavra: 'Estrela' },
];

async function gerarPergunta(prompt, usadas) {
    const semente = Math.floor(Math.random() * 10000);
    const avisoUsadas = usadas.length > 0
        ? `\nNÃO use nenhuma dessas que já foram usadas: ${usadas.join(', ')}`
        : '';

    const response = await client.chat.completions.create({
        model: 'llama-3.3-70b-versatile',
        messages: [{ role: 'user', content: `${prompt}${avisoUsadas}\nSemente: ${semente}` }],
        temperature: 1.0,
    });

    const conteudo = response.choices?.[0]?.message?.content;
    if (!conteudo) throw new Error('Resposta vazia');

    let texto = conteudo.trim();
    texto = texto.replace(/```json/g, '').replace(/```/g, '').trim();

    const match = texto.match(/\{[\s\S]*\}/);
    if (!match) throw new Error('JSON não encontrado');

    return JSON.parse(match[0]);
}

router.get('/pergunta/frase', async (req, res) => {
    try {
        const dados = await gerarPergunta(`
            Você é um educador profissional do IMIP, em Recife, Brasil.
            Crie UMA pergunta de completar frases em português para crianças.
            REGRA IMPORTANTE: a frase deve ter APENAS UMA resposta possível e óbvia. Evite frases subjetivas ou com múltiplas respostas válidas.
            Use frases sobre sons de animais, cores de objetos, ações específicas ou fatos conhecidos.
            Exemplos bons: "O cachorro faz ____" (só au au), "O céu é ____" (só azul), "A banana é ____" (só amarela)
            Exemplos ruins: "Minha mãe gosta de ____" (muitas respostas possíveis)
            Responda APENAS com JSON, sem texto extra, sem markdown.
            Formato: {"frase":"O cachorro faz ____","resposta":"au au","opcoes":["au au","miau","cocoricó"]}
            O campo "opcoes" DEVE ter EXATAMENTE 3 opções embaralhadas, apenas uma correta.
        `, historico.frase);

        historico.frase.push(dados.frase);
        if (historico.frase.length > 20) historico.frase.shift();

        res.json(dados);
    } catch (err) {
        console.error(err);
        res.status(500).json({ erro: 'Erro ao gerar pergunta' });
    }
});

router.get('/pergunta/letra', async (req, res) => {
    try {
        const item = palavrasLetra[Math.floor(Math.random() * palavrasLetra.length)];
        console.log('Item sorteado:', item);
        const letraCorreta = item.palavra[0].toUpperCase();

        const dados = await gerarPergunta(`
            Gere 2 LETRAS ÚNICAS do alfabeto (apenas um caractere cada) DIFERENTES de "${letraCorreta}".
            APENAS LETRAS, sem palavras, sem números.
            RESPONDA APENAS COM O JSON. NENHUM TEXTO ANTES OU DEPOIS.
            Formato exato: {"erradas":["X","Y"]}
        `, []);

        const opcoes = [letraCorreta, ...dados.erradas];
        opcoes.sort(() => Math.random() - 0.5);

        res.json({
            emoji: item.emoji,
            palavra: item.palavra,
            resposta: letraCorreta,
            opcoes
        });
    } catch (err) {
        console.error(err);
        res.status(500).json({ erro: 'Erro ao gerar pergunta' });
    }
});

router.get('/pergunta/imagem', async (req, res) => {
    try {
        const item = palavrasLetra[Math.floor(Math.random() * palavrasLetra.length)];

        const dados = await gerarPergunta(`
            Gere 2 palavras em português DIFERENTES de "${item.palavra}" para usar como opções erradas num jogo infantil.
            REGRAS:
            - Apenas palavras em português, NUNCA em inglês
            - Sem sinônimos ou palavras com significado similar à correta
            - As palavras erradas devem ser de categorias COMPLETAMENTE DIFERENTES da correta
            Exemplo bom para "Bolo": usar "Cachorro" e "Avião" (categorias diferentes)
            Exemplo ruim para "Bolo": usar "Torta" e "Cake" (sinônimos)
            RESPONDA APENAS COM O JSON. NENHUM TEXTO ANTES OU DEPOIS.
            Formato exato: {"erradas":["palavra1","palavra2"]}
        `, []);

        const opcoes = [item.palavra.toLowerCase(), ...dados.erradas.map(op => op.toLowerCase())];
        opcoes.sort(() => Math.random() - 0.5);

        res.json({
            emoji: item.emoji,
            resposta: item.palavra.toLowerCase(),
            opcoes
        });
    } catch (err) {
        console.error(err);
        res.status(500).json({ erro: 'Erro ao gerar pergunta' });
    }
});

module.exports = router;