import { Component, signal } from '@angular/core';

interface MensagemMotivacional {
  emoji: string;
  titulo: string;
  subtexto: string;
}

@Component({
  selector: 'app-banner-motivacional',
  standalone: true,
  templateUrl: './banner-motivacional.component.html',
})
export class BannerMotivacionalComponent {
  private readonly mensagens: MensagemMotivacional[] = [
    {
      emoji: '🌟',
      titulo: 'Continue assim!',
      subtexto: 'Você está indo muito bem!',
    },
    {
      emoji: '🚀',
      titulo: 'Você é incrível!',
      subtexto: 'Cada lição te deixa mais sabido!',
    },
    {
      emoji: '💪',
      titulo: 'Não desista!',
      subtexto: 'Aprender é uma aventura!',
    },
    {
      emoji: '🎉',
      titulo: 'Parabéns!',
      subtexto: 'Você é um campeão do aprendizado!',
    },
    {
      emoji: '⭐',
      titulo: 'Ótimo trabalho!',
      subtexto: 'Continue praticando para ganhar mais estrelas!',
    },
  ];

  readonly mensagem = signal(
    this.mensagens[Math.floor(Math.random() * this.mensagens.length)]
  );
}
