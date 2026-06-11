import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Licao } from '../models';
import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })
export class LicaoService {
  private http = inject(HttpClient);
  private baseUrl = `${environment.apiUrl}/licoes`;

  getLicao(categoriaId: string, nivelId: string): Observable<Licao> {
    return this.http.get<Licao>(`${this.baseUrl}/${categoriaId}/${nivelId}`);
  }
}
