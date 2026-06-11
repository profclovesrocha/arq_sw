export type TipoStep = 'card-informativo' | 'pergunta';

export interface StepInformativo {
  tipo: 'card-informativo';
  titulo: string;
  conteudo: string;
}

export interface StepPergunta {
  tipo: 'pergunta';
  enunciado: string;
  opcoes: string[];
  respostaCorreta: number;
}

export type StepLicao = StepInformativo | StepPergunta;

export interface Licao {
  id: string;
  categoriaId: string;
  nivelId: string;
  titulo: string;
  steps: StepLicao[];
}
