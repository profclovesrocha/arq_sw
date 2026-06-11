import { Licao } from '../models';

export const LICOES_SILABAS: Licao[] = [
  {
    id: 'silabas-1',
    categoriaId: 'silabas',
    nivelId: '1',
    titulo: 'O que é uma Sílaba?',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Sílabas são pedacinhos',
        conteudo: 'Uma sílaba é cada "pedacinho" de uma palavra. CASA = CA-SA (2 sílabas)!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas sílabas tem a palavra "PÉ"?',
        opcoes: ['1', '2', '3', '4'],
        respostaCorreta: 0,
      },
      {
        tipo: 'card-informativo',
        titulo: 'Toda sílaba tem uma vogal',
        conteudo: 'Cada sílaba tem pelo menos uma vogal. A vogal é o coração da sílaba!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas sílabas tem "GATO"?',
        opcoes: ['3', '1', '4', '2'],
        respostaCorreta: 3,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual das palavras tem APENAS 1 sílaba?',
        opcoes: ['CASA', 'PÃO', 'BOLA', 'GATO'],
        respostaCorreta: 1,
      },
    ],
  },
  {
    id: 'silabas-2',
    categoriaId: 'silabas',
    nivelId: '2',
    titulo: 'Contando Sílabas',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Vamos contar sílabas!',
        conteudo: 'Para contar sílabas, bata palmas enquanto fala a palavra. Cada palma é uma sílaba!',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas sílabas tem "BORBOLETA"?',
        opcoes: ['5', '3', '4', '2'],
        respostaCorreta: 2,
      },
      {
        tipo: 'card-informativo',
        titulo: 'Pratique!',
        conteudo: 'JA-NE-LA tem 3 sílabas. MA-CA-CO também tem 3. Você consegue pensar em outras?',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas sílabas tem "JANELA"?',
        opcoes: ['4', '2', '3', '5'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra tem 2 sílabas?',
        opcoes: ['ABELHA', 'SOL', 'MACACO', 'CASA'],
        respostaCorreta: 3,
      },
    ],
  },
  {
    id: 'silabas-3',
    categoriaId: 'silabas',
    nivelId: '3',
    titulo: 'Palavras Longas',
    steps: [
      {
        tipo: 'card-informativo',
        titulo: 'Palavras longas têm muitas sílabas!',
        conteudo: 'BOR-BO-LE-TA tem 4 sílabas! Palavras longas são como um trem com muitos vagões.',
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual palavra tem MAIS sílabas?',
        opcoes: ['SOL', 'CASA', 'BORBOLETA', 'GATO'],
        respostaCorreta: 2,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Quantas sílabas tem "TE-LE-VI-SÃO"?',
        opcoes: ['5', '4', '6', '3'],
        respostaCorreta: 1,
      },
      {
        tipo: 'pergunta',
        enunciado: 'A palavra "CA-VA-LO" tem quantas sílabas?',
        opcoes: ['2', '4', '1', '3'],
        respostaCorreta: 3,
      },
      {
        tipo: 'pergunta',
        enunciado: 'Qual a sílaba que falta? CA-VA-___',
        opcoes: ['LA', 'RA', 'SO', 'TO'],
        respostaCorreta: 0,
      },
    ],
  },
];
