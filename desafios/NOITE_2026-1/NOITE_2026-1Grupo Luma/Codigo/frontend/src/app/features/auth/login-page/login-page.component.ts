import { Component, inject, signal, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../../core/services/auth.service';
import { EstudanteService } from '../../../core/services/estudante.service';
import { ProfessorService } from '../../../core/services/professor.service';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [RouterLink, FormsModule],
  templateUrl: './login-page.component.html',
})
export class LoginPageComponent implements OnInit {
  private authService = inject(AuthService);
  private estudanteService = inject(EstudanteService);
  private professorService = inject(ProfessorService);
  private router = inject(Router);
  private route = inject(ActivatedRoute);

  matriculaInput = signal('');
  senhaInput = signal('');
  erro = signal('');
  modoProfessor = signal(false);
  carregando = signal(false);

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.modoProfessor.set(params['tipo'] === 'professor');
      this.matriculaInput.set('');
      this.senhaInput.set('');
      this.erro.set('');
    });
  }

  onSubmit(): void {
    if (this.carregando()) return;
    if (this.modoProfessor()) {
      this.loginProfessor();
    } else {
      this.loginEstudante();
    }
  }

  onMatriculaInput(event: Event): void {
    this.matriculaInput.set((event.target as HTMLInputElement).value);
    this.erro.set('');
  }

  onSenhaInput(event: Event): void {
    this.senhaInput.set((event.target as HTMLInputElement).value);
    this.erro.set('');
  }

  private loginEstudante(): void {
    const matricula = this.matriculaInput().trim();
    if (!matricula) return;

    this.carregando.set(true);
    this.estudanteService.loginPorMatricula(matricula).subscribe({
      next: (estudante) => {
        this.authService.login({
          tipo: 'estudante',
          id: String(estudante.id),
          nome: estudante.nome,
          matricula: estudante.matricula,
        });
        this.router.navigate(['/aprendizado']);
      },
      error: () => {
        this.erro.set('Hmm, não encontrei essa matrícula!');
        this.matriculaInput.set('');
        this.carregando.set(false);
      },
    });
  }

  private loginProfessor(): void {
    const matricula = this.matriculaInput().trim();
    const senha = this.senhaInput().trim();
    if (!matricula || !senha) return;

    this.carregando.set(true);
    this.professorService.autenticar(matricula, senha).subscribe({
      next: (response) => {
        this.authService.login({
          tipo: 'professor',
          id: String(response.professor.id),
          nome: response.professor.nome,
          matricula: response.professor.matricula,
          token: response.token,
        });
        this.router.navigate(['/professor']);
      },
      error: () => {
        this.erro.set('Credenciais inválidas');
        this.senhaInput.set('');
        this.carregando.set(false);
      },
    });
  }
}
