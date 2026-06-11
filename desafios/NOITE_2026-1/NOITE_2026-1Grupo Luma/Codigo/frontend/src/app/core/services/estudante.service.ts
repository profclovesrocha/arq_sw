import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Estudante } from '../models/estudante.model';
import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })
export class EstudanteService {
  private http = inject(HttpClient);
  private baseUrl = `${environment.apiUrl}/alunos`;

  loginPorMatricula(matricula: string): Observable<Estudante> {
    return this.http.post<Estudante>(`${this.baseUrl}/login`, { matricula });
  }

  cadastrar(dados: { nome: string; cpf: string; idade: number }): Observable<Estudante> {
    return this.http.post<Estudante>(`${this.baseUrl}/cadastro`, dados);
  }
}
