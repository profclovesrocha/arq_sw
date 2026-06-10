import { Component, OnInit, WritableSignal, input, signal } from '@angular/core';

@Component({
  selector: 'app-indicador-progresso',
  standalone: true,
  templateUrl: './indicador-progresso.component.html',
})
export class IndicadorProgressoComponent implements OnInit {
  totalEstrelas = input<number>(0);
  totalConquistas = input<number>(0);
  niveisCompletos = input<number>(0);
  totalNiveis = input<number>(12);

  _estrelas = signal(0);
  _conquistas = signal(0);
  _niveis = signal(0);

  ngOnInit(): void {
    this.animateCounter(this._estrelas, this.totalEstrelas());
    this.animateCounter(this._conquistas, this.totalConquistas());
    this.animateCounter(this._niveis, this.niveisCompletos());
  }

  private animateCounter(counter: WritableSignal<number>, target: number): void {
    if (target === 0) return;
    let current = 0;
    const step = () => {
      current++;
      counter.set(current);
      if (current < target) {
        setTimeout(step, 200);
      }
    };
    setTimeout(step, 200);
  }
}
