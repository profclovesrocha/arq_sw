import { Component, OnInit, computed, inject } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../../core/services/auth.service';
import { CategoriaService } from '../../../core/services/categoria.service';
import { ProgressoService } from '../../../core/services/progresso.service';
import { ShellComponent } from '../../../shared/layout/shell/shell.component';
import { BadgeConquistaComponent } from '../../../shared/ui/badge-conquista/badge-conquista.component';

const CONQUISTAS_ORDEM = [
  { categoriaId: 'vogais',     nivelId: '1' },
  { categoriaId: 'vogais',     nivelId: '2' },
  { categoriaId: 'vogais',     nivelId: '3' },
  { categoriaId: 'consoantes', nivelId: '1' },
  { categoriaId: 'consoantes', nivelId: '2' },
  { categoriaId: 'consoantes', nivelId: '3' },
  { categoriaId: 'silabas',    nivelId: '1' },
  { categoriaId: 'silabas',    nivelId: '2' },
  { categoriaId: 'silabas',    nivelId: '3' },
  { categoriaId: 'palavras',   nivelId: '1' },
  { categoriaId: 'palavras',   nivelId: '2' },
  { categoriaId: 'palavras',   nivelId: '3' },
];

@Component({
  selector: 'app-perfil-page',
  standalone: true,
  imports: [ShellComponent, BadgeConquistaComponent],
  templateUrl: './perfil-page.component.html',
})
export class PerfilPageComponent implements OnInit {
  private auth = inject(AuthService);
  private router = inject(Router);
  private progressoService = inject(ProgressoService);
  private categoriaService = inject(CategoriaService);

  readonly categorias = computed(() => this.categoriaService.listarTodas());

  readonly conquistas = computed(() => {
    const obtidas = this.progressoService.conquistas();
    const cats = this.categorias();
    return CONQUISTAS_ORDEM.map(pos => {
      const cat = cats.find(c => c.id === pos.categoriaId);
      const obtida = obtidas.find(
        c => c.categoriaId === pos.categoriaId && c.nivelId === pos.nivelId
      );
      return {
        ...pos,
        nome: obtida?.nome ?? `${cat?.nome ?? pos.categoriaId} — Nível ${pos.nivelId}`,
        desbloqueada: obtida?.desbloqueada ?? false,
        corAccent: cat?.corAccent ?? '#ccc',
      };
    });
  });

  readonly progressoPorCategoria = computed(() => {
    const niveis = this.progressoService.niveis();
    return this.categorias().map(cat => {
      const concluidos = niveis.filter(n => n.categoriaId === cat.id && n.concluido).length;
      return { cat, concluidos };
    });
  });

  ngOnInit(): void {
    this.categoriaService.carregarCategorias();
    const id = this.auth.idUsuario();
    if (id) {
      this.progressoService.carregarProgresso(id);
    }
  }

  voltarParaDashboard(): void {
    this.router.navigate(['/aprendizado']);
  }
}
