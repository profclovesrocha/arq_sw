import { Component, OnInit, inject } from '@angular/core';
import { Router } from '@angular/router';
import { ProfessorService, AlunoMetricas } from '../../../core/services/professor.service';
import { ShellComponent } from '../../../shared/layout/shell/shell.component';

@Component({
  selector: 'app-painel-page',
  standalone: true,
  imports: [ShellComponent],
  templateUrl: './painel-page.component.html',
})
export class PainelPageComponent implements OnInit {
  private professorService = inject(ProfessorService);
  private router = inject(Router);

  alunos: AlunoMetricas[] = [];

  ngOnInit(): void {
    this.professorService.listarAlunos().subscribe({
      next: (alunos) => {
        this.alunos = alunos;
      },
    });
  }

  onVerDetalhe(id: number): void {
    this.router.navigate(['/professor/aluno', id]);
  }
}
