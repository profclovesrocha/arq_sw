import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Professor } from '../models/professor.model';
import { environment } from '../../../environments/environment';

export interface LoginProfessorResponse {
  message: string;
  token: string;
  professor: Professor;
}

export interface AlunoMetricas {
  id: number;
  nome: string;
  matricula: string;
  idade: number;
  estrelas: number;
  conquistas: number;
  niveis_completos: number;
}

@Injectable({ providedIn: 'root' })
export class ProfessorService {
  private http = inject(HttpClient);
  private baseUrl = `${environment.apiUrl}/professores`;

  autenticar(matricula: string, senha: string): Observable<LoginProfessorResponse> {
    return this.http.post<LoginProfessorResponse>(`${this.baseUrl}/login`, { matricula, senha });
  }

  listarAlunos(): Observable<AlunoMetricas[]> {
    return this.http.get<AlunoMetricas[]>(`${this.baseUrl}/alunos`);
  }
}
