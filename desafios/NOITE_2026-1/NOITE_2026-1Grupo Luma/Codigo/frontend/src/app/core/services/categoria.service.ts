import { Injectable, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Categoria } from '../models';
import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })
export class CategoriaService {
  private http = inject(HttpClient);
  private baseUrl = `${environment.apiUrl}/categorias`;

  private _categorias = signal<Categoria[]>([]);
  readonly categorias = this._categorias.asReadonly();

  carregarCategorias(): void {
    this.http.get<Categoria[]>(`${this.baseUrl}/`).subscribe({
      next: (cats) => this._categorias.set(cats),
    });
  }

  listarTodas(): Categoria[] {
    return this._categorias();
  }

  buscarPorId(id: string): Categoria | undefined {
    return this._categorias().find(c => c.id === id);
  }
}
