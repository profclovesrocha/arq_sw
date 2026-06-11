import { Component, computed, input, output, signal } from '@angular/core';

export type EstadoNivel = 'bloqueado' | 'disponivel' | 'concluido';

@Component({
  selector: 'app-card-nivel',
  standalone: true,
  templateUrl: './card-nivel.component.html',
})
export class CardNivelComponent {
  estado = input.required<EstadoNivel>();
  nivelId = input.required<string>();
  categoriaId = input.required<string>();
  corPastel = input.required<string>();
  estrelas = input<number>(0);
  pulsando = input<boolean>(false);

  jogar = output<{ categoriaId: string; nivelId: string }>();

  shaking = signal(false);

  readonly nomeNivel = computed(() => {
    const nomes: Record<string, string> = {
      '1': 'Básico',
      '2': 'Intermediário',
      '3': 'Avançado',
    };
    return nomes[this.nivelId()] ?? `Nível ${this.nivelId()}`;
  });

  readonly estrelasArray = [1, 2, 3];

  onJogar(): void {
    this.jogar.emit({ categoriaId: this.categoriaId(), nivelId: this.nivelId() });
  }

  onClickBloqueado(): void {
    if (this.shaking()) return;
    this.shaking.set(true);
    setTimeout(() => this.shaking.set(false), 300);
  }
}
