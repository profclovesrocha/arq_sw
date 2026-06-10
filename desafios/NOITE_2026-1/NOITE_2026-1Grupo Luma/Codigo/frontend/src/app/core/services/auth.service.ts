import { Injectable, signal, computed, inject } from '@angular/core';
import { Router } from '@angular/router';

export interface SessaoUsuario {
  tipo: 'estudante' | 'professor';
  id: string;
  nome?: string;
  matricula?: string;
  token?: string;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  private router = inject(Router);

  private _sessao = signal<SessaoUsuario | null>(this.carregarSessao());

  readonly sessao = this._sessao.asReadonly();
  readonly tipoUsuario = computed(() => this._sessao()?.tipo ?? 'estudante');
  readonly idUsuario = computed(() => this._sessao()?.id ?? '');
  readonly nomeUsuario = computed(() => this._sessao()?.nome ?? '');
  readonly matriculaUsuario = computed(() => this._sessao()?.matricula ?? '');
  readonly estaAutenticado = computed(() => this._sessao() !== null);

  login(sessao: SessaoUsuario): void {
    sessionStorage.setItem('alfabe_sessao', JSON.stringify(sessao));
    this._sessao.set(sessao);
  }

  logout(): void {
    sessionStorage.removeItem('alfabe_sessao');
    this._sessao.set(null);
    this.router.navigate(['/login']);
  }

  private carregarSessao(): SessaoUsuario | null {
    const raw = sessionStorage.getItem('alfabe_sessao');
    if (!raw) return null;
    try {
      return JSON.parse(raw) as SessaoUsuario;
    } catch {
      return null;
    }
  }
}
