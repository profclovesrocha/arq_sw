import { Progresso } from '../models';

export const PROGRESSO_MOCK: Progresso[] = [
  {
    estudanteId: '1234',
    niveis: [],
    conquistas: [],
    estrelas: 0,
  },
  {
    estudanteId: '5678',
    niveis: [
      { categoriaId: 'vogais', nivelId: '1', concluido: true, estrelas: 3 },
      { categoriaId: 'vogais', nivelId: '2', concluido: true, estrelas: 2 },
      { categoriaId: 'consoantes', nivelId: '1', concluido: true, estrelas: 1 },
    ],
    conquistas: [
      {
        id: 'vogais-1',
        nome: 'Mestre das Vogais I',
        categoriaId: 'vogais',
        nivelId: '1',
        desbloqueada: true,
      },
      {
        id: 'vogais-2',
        nome: 'Mestre das Vogais II',
        categoriaId: 'vogais',
        nivelId: '2',
        desbloqueada: true,
      },
      {
        id: 'consoantes-1',
        nome: 'Aprendiz das Consoantes',
        categoriaId: 'consoantes',
        nivelId: '1',
        desbloqueada: true,
      },
    ],
    estrelas: 6,
  },
];
