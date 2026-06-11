import { Component, input } from '@angular/core';

@Component({
  selector: 'app-estrela',
  standalone: true,
  templateUrl: './estrela.component.html',
})
export class EstrelaComponent {
  preenchida = input<boolean>(false);
  tamanho = input<number>(32);
}
