import { Component, inject, signal } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { EstudanteService } from '../../../core/services/estudante.service';

@Component({
  selector: 'app-cadastro-page',
  standalone: true,
  imports: [RouterLink, FormsModule],
  templateUrl: './cadastro-page.component.html',
})
export class CadastroPageComponent {
  private estudanteService = inject(EstudanteService);
  private router = inject(Router);

  nomeInput = signal('');
  cpfInput = signal('');
  idadeInput = signal('');
  erro = signal('');
  matriculaGerada = signal<string | null>(null);
  cadastroConcluido = signal(false);
  carregando = signal(false);

  onNomeInput(event: Event): void {
    this.nomeInput.set((event.target as HTMLInputElement).value);
    this.erro.set('');
  }

  onCpfInput(event: Event): void {
    let value = (event.target as HTMLInputElement).value.replace(/\D/g, '');
    value = value.slice(0, 11);
    // Auto-format CPF: 000.000.000-00
    if (value.length > 9) {
      value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(6, 9)}-${value.slice(9)}`;
    } else if (value.length > 6) {
      value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(6)}`;
    } else if (value.length > 3) {
      value = `${value.slice(0, 3)}.${value.slice(3)}`;
    }
    this.cpfInput.set(value);
    this.erro.set('');
  }

  onIdadeInput(event: Event): void {
    const value = (event.target as HTMLInputElement).value.replace(/\D/g, '');
    this.idadeInput.set(value);
    this.erro.set('');
  }

  onSubmit(): void {
    if (this.carregando()) return;

    const nome = this.nomeInput().trim();
    const cpf = this.cpfInput().trim();
    const idadeStr = this.idadeInput().trim();

    if (!nome) {
      this.erro.set('O nome é obrigatório.');
      return;
    }

    // CPF formatado deve ter 14 chars: 000.000.000-00
    if (cpf.length !== 14) {
      this.erro.set('O CPF deve ter exatamente 11 dígitos.');
      return;
    }

    const idade = parseInt(idadeStr, 10);
    if (isNaN(idade) || idade < 3 || idade > 12) {
      this.erro.set('A idade deve ser entre 3 e 12 anos.');
      return;
    }

    this.carregando.set(true);
    this.estudanteService.cadastrar({ nome, cpf, idade }).subscribe({
      next: (estudante) => {
        this.matriculaGerada.set(estudante.matricula);
        this.cadastroConcluido.set(true);
        this.carregando.set(false);
      },
      error: (err) => {
        const msg = err.error?.message ?? 'Erro ao cadastrar. Tente novamente.';
        this.erro.set(msg);
        this.carregando.set(false);
      },
    });
  }

  voltarLogin(): void {
    this.router.navigate(['/login']);
  }
}
