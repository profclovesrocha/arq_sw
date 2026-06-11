import { Licao } from '../models';

export const LICOES_VOGAIS: Licao[] = [
  {
    id: 'vogais-1',
    categoriaId: 'vogais',
    nivelId: '1',
    titulo: 'Conhecendo as Vogais',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'O que são vogais?',
        conteudo: 'As vogais são letras especiais: A, E, I, O, U. Elas fazem sons abertos e bonitos!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual dessas letras é uma vogal?',
        opcoes: ['B', 'A', 'D', 'F'],
        respostaCorreta: 1,
      },
      {
        tipo: 'card-informativo',
        titulo: 'A letra A',
        conteudo: 'O "A" é a primeira vogal. A palavra "abelha" começa com A!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual dessas letras NÃO é uma vogal?',
        opcoes: ['A', 'E', 'B', 'I'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas vogais tem o alfabeto?',
        opcoes: ['3', '4', '5', '6'],
        respostaCorreta: 2,
      },
    ],
  },
  {
    id: 'vogais-2',
    categoriaId: 'vogais',
    nivelId: '2',
    titulo: 'Vogais nas Palavras',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Vogais nas palavras',
        conteudo: 'Toda palavra tem pelo menos uma vogal. Sem vogais, não conseguimos falar!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual vogal está na palavra "BOLA"?',
        opcoes: ['E', 'O', 'U', 'I'],
        respostaCorreta: 1,
      },
      {
        tipo: 'card-informativo',
        titulo: 'Encontrando vogais',
        conteudo: 'Na palavra "GATO" temos duas vogais: o "A" e o "O". Você consegue encontrá-las?',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas vogais tem a palavra "CASA"?',
        opcoes: ['1', '3', '2', '4'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual vogal está no meio da palavra "PÉ"?',
        opcoes: ['A', 'I', 'E', 'U'],
        respostaCorreta: 2,
      },
    ],
  },
  {
    id: 'vogais-3',
    categoriaId: 'vogais',
    nivelId: '3',
    titulo: 'Começando com Vogal',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Palavras que começam com vogal',
        conteudo: 'Muitas palavras legais começam com vogal: Abelha, Elefante, Igreja, Ônibus, Uva!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra começa com a vogal "A"?',
        opcoes: ['Banana', 'Abelha', 'Gato', 'Casa'],
        respostaCorreta: 1,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra começa com a vogal "E"?',
        opcoes: ['Faca', 'Bola', 'Elefante', 'Dente'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra começa com a vogal "I"?',
        opcoes: ['Igreja', 'Pato', 'Rato', 'Sapo'],
        respostaCorreta: 0,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra começa com a vogal "U"?',
        opcoes: ['Sino', 'Leite', 'Mesa', 'Uva'],
        respostaCorreta: 3,
      },
    ],
  },
];
