export interface NivelProgresso {
  categoriaId: string;
  nivelId: string;
  concluido: boolean;
  estrelas: number; // 0, 1, 2 ou 3
}

export interface Conquista {
  id: string;
  nome: string;
  categoriaId: string;
  nivelId: string;
  desbloqueada: boolean;
}

export interface Progresso {
  estudanteId: string;
  niveis: NivelProgresso[];
  conquistas: Conquista[];
  estrelas: number;
}
