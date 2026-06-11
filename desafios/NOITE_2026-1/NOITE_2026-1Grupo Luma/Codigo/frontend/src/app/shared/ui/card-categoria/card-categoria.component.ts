import { Component, inject, input, output } from '@angular/core';
import { Categoria, NivelProgresso } from '../../../core/models';
import { EstadoNivel, ProgressoService } from '../../../core/services/progresso.service';
import { CardNivelComponent } from '../card-nivel/card-nivel.component';

@Component({
  selector: 'app-card-categoria',
  standalone: true,
  imports: [CardNivelComponent],
  templateUrl: './card-categoria.component.html',
})
export class CardCategoriaComponent {
  private progressoService = inject(ProgressoService);

  categoria = input.required<Categoria>();
  niveisProgresso = input<NivelProgresso[]>([]);
  proximoNivelId = input<string | null>(null);

  jogar = output<{ categoriaId: string; nivelId: string }>();

  readonly nivelIds = ['1', '2', '3'];

  estadoDeNivel(nivelId: string): EstadoNivel {
    return this.progressoService.estadoNivel(this.categoria().id, nivelId);
  }

  estrelasDeNivel(nivelId: string): number {
    return (
      this.niveisProgresso().find(
        n => n.nivelId === nivelId && n.categoriaId === this.categoria().id
      )?.estrelas ?? 0
    );
  }

  isPulsando(nivelId: string): boolean {
    return this.proximoNivelId() === nivelId;
  }

  onJogar(event: { categoriaId: string; nivelId: string }): void {
    this.jogar.emit(event);
  }
}
