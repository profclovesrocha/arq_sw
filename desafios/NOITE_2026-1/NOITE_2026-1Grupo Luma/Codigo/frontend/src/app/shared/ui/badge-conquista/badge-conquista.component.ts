import { Component, input } from '@angular/core';

@Component({
  selector: 'app-badge-conquista',
  standalone: true,
  templateUrl: './badge-conquista.component.html',
})
export class BadgeConquistaComponent {
  nome = input.required<string>();
  icone = input<string>('🏆');
  corAccent = input<string>('#8B5CF6');
  desbloqueada = input<boolean>(false);
}
