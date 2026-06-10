import { Component, input, output } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterLink, RouterLinkActive],
  templateUrl: './header.component.html',
})
export class HeaderComponent {
  tipoUsuario = input.required<'estudante' | 'professor'>();
  idUsuario = input.required<string>();
  sair = output<void>();

  get saudacao(): string {
    return this.tipoUsuario() === 'estudante' ? '👋 Olá, Estudante!' : 'Olá, Professor!';
  }
}
