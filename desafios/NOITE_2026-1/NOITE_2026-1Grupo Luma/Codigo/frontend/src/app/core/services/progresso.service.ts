import { Injectable, computed, signal, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Progresso } from '../models';
import { environment } from '../../../environments/environment';

export type EstadoNivel = 'bloqueado' | 'disponivel' | 'concluido';

interface ConcluirResponse {
  estrelas_ganhas: number;
  conquista: string | null;
  ja_concluida: boolean;
}

@Injectable({ providedIn: 'root' })
export class ProgressoService {
  private http = inject(HttpClient);
  private baseUrl = `${environment.apiUrl}/alunos`;

  private _progresso = signal<Progresso | null>(null);

  readonly totalEstrelas = computed(() => this._progresso()?.estrelas ?? 0);
  readonly totalConquistas = computed(
    () => this._progresso()?.conquistas.filter(c => c.desbloqueada).length ?? 0
  );
  readonly niveisCompletos = computed(
    () => this._progresso()?.niveis.filter(n => n.concluido).length ?? 0
  );
  readonly niveis = computed(() => this._progresso()?.niveis ?? []);
  readonly conquistas = computed(() => this._progresso()?.conquistas ?? []);

  carregarProgresso(estudanteId: string): void {
    this.http.get<Progresso>(`${this.baseUrl}/${estudanteId}/progresso`).subscribe({
      next: (progresso) => this._progresso.set(progresso),
      error: () => this._progresso.set({ estudanteId, niveis: [], conquistas: [], estrelas: 0 }),
    });
  }

  estadoNivel(categoriaId: string, nivelId: string): EstadoNivel {
    const progresso = this._progresso();
    if (!progresso) return 'bloqueado';

    const nivel = progresso.niveis.find(
      n => n.categoriaId === categoriaId && n.nivelId === nivelId
    );

    if (nivelId === '1') {
      return nivel?.concluido ? 'concluido' : 'disponivel';
    }

    const nivelAnteriorId = String(Number(nivelId) - 1);
    const nivelAnterior = progresso.niveis.find(
      n => n.categoriaId === categoriaId && n.nivelId === nivelAnteriorId
    );
    if (!nivelAnterior?.concluido) return 'bloqueado';

    return nivel?.concluido ? 'concluido' : 'disponivel';
  }

  concluirLicao(estudanteId: string, categoriaId: string, nivelId: string): void {
    this.http.post<ConcluirResponse>(
      `${this.baseUrl}/${estudanteId}/progresso/concluir`,
      { categoriaId, nivelId }
    ).subscribe({
      next: () => {
        // Recarrega progresso completo após conclusão
        this.carregarProgresso(estudanteId);
      },
    });
  }
}
