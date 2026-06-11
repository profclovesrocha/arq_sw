import { Component, inject } from '@angular/core';
import { AuthService } from '../../../core/services/auth.service';
import { HeaderComponent } from '../header/header.component';

@Component({
  selector: 'app-shell',
  standalone: true,
  imports: [HeaderComponent],
  templateUrl: './shell.component.html',
})
export class ShellComponent {
  private authService = inject(AuthService);

  tipoUsuario = this.authService.tipoUsuario;
  idUsuario = this.authService.idUsuario;

  onSair(): void {
    this.authService.logout();
  }
}
