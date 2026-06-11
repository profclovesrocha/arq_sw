import { Categoria } from '../models';

export const CATEGORIAS_MOCK: Categoria[] = [
  {
    id: 'vogais',
    nome: 'Vogais',
    descricao: 'Aprenda as vogais A, E, I, O, U',
    icone: '🅐',
    corPastel: '#FDE8E8',
    corAccent: '#E53E3E',
  },
  {
    id: 'consoantes',
    nome: 'Consoantes',
    descricao: 'Conheça as consoantes do alfabeto',
    icone: '🅑',
    corPastel: '#DBEAFE',
    corAccent: '#3B82F6',
  },
  {
    id: 'silabas',
    nome: 'Sílabas',
    descricao: 'Aprenda a juntar sons e formar sílabas',
    icone: 'sí',
    corPastel: '#FEF3C7',
    corAccent: '#D97706',
  },
  {
    id: 'palavras',
    nome: 'Palavras',
    descricao: 'Forme palavras completas e divirta-se!',
    icone: 'abc',
    corPastel: '#D1FAE5',
    corAccent: '#059669',
  },
];
