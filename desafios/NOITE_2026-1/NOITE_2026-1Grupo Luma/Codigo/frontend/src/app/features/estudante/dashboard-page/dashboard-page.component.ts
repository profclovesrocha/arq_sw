import { Component, OnInit, computed, inject } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../../core/services/auth.service';
import { CategoriaService } from '../../../core/services/categoria.service';
import { ProgressoService } from '../../../core/services/progresso.service';
import { ShellComponent } from '../../../shared/layout/shell/shell.component';
import { BannerMotivacionalComponent } from '../../../shared/ui/banner-motivacional/banner-motivacional.component';
import { CardCategoriaComponent } from '../../../shared/ui/card-categoria/card-categoria.component';
import { IndicadorProgressoComponent } from '../../../shared/ui/indicador-progresso/indicador-progresso.component';

@Component({
  selector: 'app-dashboard-page',
  standalone: true,
  imports: [
    ShellComponent,
    BannerMotivacionalComponent,
    IndicadorProgressoComponent,
    CardCategoriaComponent,
  ],
  templateUrl: './dashboard-page.component.html',
})
export class DashboardPageComponent implements OnInit {
  private auth = inject(AuthService);
  private router = inject(Router);
  readonly progressoService = inject(ProgressoService);
  readonly categoriaService = inject(CategoriaService);

  readonly categorias = computed(() => this.categoriaService.listarTodas());

  readonly proximoNivel = computed(() => {
    const ordem = ['vogais', 'consoantes', 'silabas', 'palavras'];
    const nivelIds = ['1', '2', '3'];
    for (const catId of ordem) {
      for (const nvId of nivelIds) {
        if (this.progressoService.estadoNivel(catId, nvId) === 'disponivel') {
          return { categoriaId: catId, nivelId: nvId };
        }
      }
    }
    return null;
  });

  ngOnInit(): void {
    this.categoriaService.carregarCategorias();
    const id = this.auth.idUsuario();
    if (id) {
      this.progressoService.carregarProgresso(id);
    }
  }

  niveisDeCategoria(categoriaId: string) {
    return this.progressoService.niveis().filter(n => n.categoriaId === categoriaId);
  }

  proximoNivelIdParaCategoria(categoriaId: string): string | null {
    const proximo = this.proximoNivel();
    return proximo?.categoriaId === categoriaId ? proximo.nivelId : null;
  }

  onJogar(event: { categoriaId: string; nivelId: string }): void {
    this.router.navigate(['/licao', event.categoriaId, event.nivelId]);
  }
}
