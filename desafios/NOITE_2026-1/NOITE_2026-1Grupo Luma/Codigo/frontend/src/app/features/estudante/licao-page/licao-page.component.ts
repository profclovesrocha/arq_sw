import { Component, OnInit, computed, inject, signal } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Licao, StepInformativo, StepPergunta } from '../../../core/models';
import { AuthService } from '../../../core/services/auth.service';
import { CategoriaService } from '../../../core/services/categoria.service';
import { LicaoService } from '../../../core/services/licao.service';
import { ProgressoService } from '../../../core/services/progresso.service';
import { BadgeConquistaComponent } from '../../../shared/ui/badge-conquista/badge-conquista.component';
import { EstrelaComponent } from '../../../shared/ui/estrela/estrela.component';
import { OpcaoMultiplaEscolhaComponent } from '../../../shared/ui/opcao-multipla-escolha/opcao-multipla-escolha.component';

@Component({
  selector: 'app-licao-page',
  standalone: true,
  imports: [OpcaoMultiplaEscolhaComponent, EstrelaComponent, BadgeConquistaComponent],
  templateUrl: './licao-page.component.html',
})
export class LicaoPageComponent implements OnInit {
  private licaoService = inject(LicaoService);
  private progressoService = inject(ProgressoService);
  private authService = inject(AuthService);
  private categoriaService = inject(CategoriaService);
  private route = inject(ActivatedRoute);
  private router = inject(Router);

  licao = signal<Licao | null>(null);
  stepAtual = signal(0);
  transitando = signal(false);
  concluida = signal(false);
  foiPrimeiraVez = signal(false);
  mostrarConfirmacao = signal(false);

  // Derivados estáticos (definidos em ngOnInit, não mudam depois)
  qtdEstrelas = 1;
  estrelasArray: number[] = [];
  nomeDaConquista = '';
  corAccentDaCategoria = '#8B5CF6';

  private _categoriaId = '';
  private _nivelId = '';

  readonly totalSteps = computed(() => this.licao()?.steps.length ?? 0);
  readonly stepCorrente = computed(() => this.licao()?.steps[this.stepAtual()] ?? null);
  readonly dotsProgresso = computed(() =>
    Array.from({ length: this.totalSteps() }, (_, i) => i <= this.stepAtual())
  );

  comoInformativo(step: unknown): StepInformativo {
    return step as StepInformativo;
  }

  comoPergunta(step: unknown): StepPergunta {
    return step as StepPergunta;
  }

  ngOnInit(): void {
    const categoriaId = this.route.snapshot.paramMap.get('categoriaId') ?? '';
    const nivelId = this.route.snapshot.paramMap.get('nivelId') ?? '';

    this._categoriaId = categoriaId;
    this._nivelId = nivelId;

    this.licaoService.getLicao(categoriaId, nivelId).subscribe({
      next: (licao) => {
        this.licao.set(licao);

        const nomes: Record<string, string> = { '1': 'Básico', '2': 'Reconhecimento', '3': 'Intermediário' };
        const cat = this.categoriaService.buscarPorId(categoriaId);
        this.qtdEstrelas = Number(nivelId) || 1;
        this.estrelasArray = Array.from({ length: this.qtdEstrelas }, (_, i) => i);
        this.nomeDaConquista = `${cat?.nome ?? ''} — ${nomes[nivelId] ?? 'Nível ' + nivelId}`;
        this.corAccentDaCategoria = cat?.corAccent ?? '#8B5CF6';
      },
      error: () => {
        this.router.navigate(['/aprendizado']);
      },
    });
  }

  avancarStep(): void {
    if (this.transitando()) return;
    this.transitando.set(true);
    setTimeout(() => {
      const proximo = this.stepAtual() + 1;
      if (proximo >= this.totalSteps()) {
        const id = this.authService.idUsuario();
        if (id) {
          this.progressoService.concluirLicao(id, this._categoriaId, this._nivelId);
          this.foiPrimeiraVez.set(true);
        }
        this.concluida.set(true);
      } else {
        this.stepAtual.set(proximo);
      }
      this.transitando.set(false);
    }, 200);
  }

  onAcertou(): void {
    this.avancarStep();
  }

  onFechar(): void {
    this.mostrarConfirmacao.set(true);
  }

  confirmarSaida(): void {
    this.router.navigate(['/aprendizado']);
  }

  cancelarSaida(): void {
    this.mostrarConfirmacao.set(false);
  }

  voltarParaAtividades(): void {
    this.router.navigate(['/aprendizado']);
  }
}
