import { Licao } from '../models';

export const LICOES_CONSOANTES: Licao[] = [
  {
    id: 'consoantes-1',
    categoriaId: 'consoantes',
    nivelId: '1',
    titulo: 'Conhecendo as Consoantes',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'O que são consoantes?',
        conteudo: 'Consoantes são todas as letras que não são vogais. São 21 consoantes no alfabeto!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual dessas letras é uma consoante?',
        opcoes: ['A', 'B', 'E', 'I'],
        respostaCorreta: 1,
      },
      {
        tipo: 'card-informativo',
        titulo: 'A letra B',
        conteudo: 'O "B" faz o som de "bê". Bola, boneca, bicicleta começam com B!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual dessas letras NÃO é uma consoante?',
        opcoes: ['C', 'D', 'O', 'F'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas consoantes tem o alfabeto?',
        opcoes: ['21', '5', '10', '26'],
        respostaCorreta: 0,
      },
    ],
  },
  {
    id: 'consoantes-2',
    categoriaId: 'consoantes',
    nivelId: '2',
    titulo: 'Consoantes nas Palavras',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Consoantes e vogais juntas',
        conteudo: 'As consoantes precisam das vogais para formar sons. Juntas elas criam palavras!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual a consoante da palavra "PÁ"?',
        opcoes: ['A', 'P', 'E', 'O'],
        respostaCorreta: 1,
      },
      {
        tipo: 'card-informativo',
        titulo: 'Encontrando consoantes',
        conteudo: 'Na palavra "MALA" temos as consoantes M e L, e as vogais A e A.',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas consoantes tem a palavra "BOI"?',
        opcoes: ['0', '3', '1', '2'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual dessas palavras tem MAIS consoantes?',
        opcoes: ['Uva', 'Oi', 'Prato', 'Eu'],
        respostaCorreta: 2,
      },
    ],
  },
  {
    id: 'consoantes-3',
    categoriaId: 'consoantes',
    nivelId: '3',
    titulo: 'Sons das Consoantes',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Consoantes têm sons diferentes',
        conteudo: 'O "R" faz sons diferentes: "rato" (forte) e "caro" (suave). Que legal!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual letra faz o som de "ssss"?',
        opcoes: ['R', 'T', 'S', 'D'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'A palavra "CAJU" começa com qual consoante?',
        opcoes: ['J', 'A', 'C', 'U'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual consoante aparece duas vezes em "PIPA"?',
        opcoes: ['I', 'P', 'A', 'R'],
        respostaCorreta: 1,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra começa com a consoante "M"?',
        opcoes: ['Abelha', 'Elefante', 'Macaco', 'Uva'],
        respostaCorreta: 2,
      },
    ],
  },
];
