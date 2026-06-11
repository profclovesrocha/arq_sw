import { Component, OnInit, effect, input, output, signal } from '@angular/core';
import { StepPergunta } from '../../../core/models';

type EstadoOpcao = 'neutro' | 'correto' | 'incorreto' | 'desabilitado';

@Component({
  selector: 'app-opcao-multipla-escolha',
  standalone: true,
  templateUrl: './opcao-multipla-escolha.component.html',
})
export class OpcaoMultiplaEscolhaComponent {
  pergunta = input.required<StepPergunta>();
  acertou = output<void>();

  estadosOpcoes = signal<EstadoOpcao[]>([]);

  private readonly reducedMotion =
    typeof window !== 'undefined' &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  constructor() {
    effect(() => {
      const p = this.pergunta();
      this.estadosOpcoes.set(p.opcoes.map((): EstadoOpcao => 'neutro'));
    });
  }

  isDesabilitada(indice: number): boolean {
    const estado = this.estadosOpcoes()[indice];
    return estado === 'desabilitado' || estado === 'correto';
  }

  onSelecionarOpcao(indice: number): void {
    if (this.isDesabilitada(indice)) return;

    const correta = this.pergunta().respostaCorreta === indice;

    if (correta) {
      this.estadosOpcoes.update(estados => {
        const novo = [...estados];
        novo[indice] = 'correto';
        return novo;
      });
      setTimeout(() => this.acertou.emit(), 1500);
    } else {
      this.estadosOpcoes.update(estados => {
        const novo = [...estados];
        novo[indice] = 'incorreto';
        return novo;
      });
      setTimeout(() => {
        this.estadosOpcoes.update(estados => {
          const novo = [...estados];
          novo[indice] = 'desabilitado';
          return novo;
        });
      }, 800);
    }
  }

  classeOpcao(indice: number): string {
    const estado = this.estadosOpcoes()[indice];
    const base =
      'w-full min-h-[48px] px-4 py-3 rounded-[var(--rounded-lg)] border-2 text-left font-semibold text-base transition-all focus:outline-none focus:ring-2 focus:ring-[var(--color-imip-green)]';
    switch (estado) {
      case 'correto':
        return `${base} bg-[#DCFCE7] border-[var(--color-success)] text-[var(--color-success)]${this.reducedMotion ? '' : ' animate-confetti'}`;
      case 'incorreto':
        return `${base} bg-[#FEE2E2] border-[var(--color-error)] text-[var(--color-error)]${this.reducedMotion ? '' : ' animate-shake'}`;
      case 'desabilitado':
        return `${base} bg-[#F3F4F6] border-[var(--color-disabled)] text-[var(--color-text-muted)] opacity-50 cursor-not-allowed`;
      default:
        return `${base} bg-white border-[var(--color-border)] text-[var(--color-text-primary)] hover:border-[var(--color-imip-green)] hover:bg-[#F0FDF4] active:scale-[0.98]`;
    }
  }
}
