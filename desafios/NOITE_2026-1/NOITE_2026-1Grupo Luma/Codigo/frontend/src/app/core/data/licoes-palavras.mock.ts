import { Licao } from '../models';

export const LICOES_PALAVRAS: Licao[] = [
  {
    id: 'palavras-1',
    categoriaId: 'palavras',
    nivelId: '1',
    titulo: 'Palavras Simples',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'O que é uma palavra?',
        conteudo: 'Uma palavra é um conjunto de letras com significado. "SOL", "LUA", "PÉ" são palavras!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual dessas é uma palavra real?',
        opcoes: ['XYZ', 'PÁ', 'QRF', 'BWD'],
        respostaCorreta: 1,
      },
      {
        tipo: 'card-informativo',
        titulo: 'Palavras curtas',
        conteudo: 'Palavras de 1 sílaba são curtas e rápidas de falar: PÃO, SOL, PÉ, MAR!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra indica o astro do dia?',
        opcoes: ['LUA', 'SOL', 'MAR', 'CÉU'],
        respostaCorreta: 1,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual dessas palavras é mais curta?',
        opcoes: ['BORBOLETA', 'JANELA', 'PÉ', 'MACACO'],
        respostaCorreta: 2,
      },
    ],
  },
  {
    id: 'palavras-2',
    categoriaId: 'palavras',
    nivelId: '2',
    titulo: 'Palavras com 2 Sílabas',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Palavras com 2 sílabas',
        conteudo: 'BOLA = BO-LA, GATO = GA-TO. Essas palavras têm exatamente 2 sílabas!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual dessas palavras tem 2 sílabas?',
        opcoes: ['SOL', 'BORBOLETA', 'CASA', 'TELEVISÃO'],
        respostaCorreta: 2,
      },
      {
        tipo: 'card-informativo',
        titulo: 'Mais exemplos!',
        conteudo: 'PATO, MALA, FOCA, PELE. Todas têm 2 sílabas. Você consegue bater palmas?',
      },
      {
        tipo: 'pergunta',
        enunciado: 'A criança brinca com a ___ (2 sílabas)',
        opcoes: ['BOLA', 'BORBOLETA', 'PÉ', 'SOL'],
        respostaCorreta: 0,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual animal tem 2 sílabas no nome?',
        opcoes: ['BORBOLETA', 'GATO', 'JACARÉ', 'ELEFANTE'],
        respostaCorreta: 1,
      },
    ],
  },
  {
    id: 'palavras-3',
    categoriaId: 'palavras',
    nivelId: '3',
    titulo: 'Palavras Longas',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Palavras compridas',
        conteudo: 'Palavras longas têm 3 ou mais sílabas. MA-CA-CO, ELE-FAN-TE, BOR-BO-LE-TA!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual animal tem 3 sílabas no nome?',
        opcoes: ['PÃO', 'GATO', 'MACACO', 'SOL'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra tem 4 sílabas?',
        opcoes: ['GATO', 'BORBOLETA', 'CASA', 'SOL'],
        respostaCorreta: 1,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Complete a palavra: ELE-FAN-___',
        opcoes: ['TE', 'SA', 'LA', 'DO'],
        respostaCorreta: 0,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual a palavra mais longa?',
        opcoes: ['PAI', 'BOLA', 'JANELA', 'BORBOLETA'],
        respostaCorreta: 3,
      },
    ],
  },
];
