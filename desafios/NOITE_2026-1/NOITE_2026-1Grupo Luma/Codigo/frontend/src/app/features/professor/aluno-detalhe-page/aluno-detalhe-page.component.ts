import { Component, OnInit, computed, inject, signal } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { Progresso } from '../../../core/models/progresso.model';
import { CategoriaService } from '../../../core/services/categoria.service';
import { ShellComponent } from '../../../shared/layout/shell/shell.component';
import { BadgeConquistaComponent } from '../../../shared/ui/badge-conquista/badge-conquista.component';
import { environment } from '../../../../environments/environment';

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

interface AlunoInfo {
  id: number;
  nome: string;
  matricula: string;
  idade: number;
}

@Component({
  selector: 'app-aluno-detalhe-page',
  standalone: true,
  imports: [ShellComponent, BadgeConquistaComponent],
  templateUrl: './aluno-detalhe-page.component.html',
})
export class AlunoDetalhePageComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private http = inject(HttpClient);
  private categoriaService = inject(CategoriaService);

  estudante = signal<AlunoInfo | null>(null);
  progresso = signal<Progresso | null>(null);

  readonly categorias = computed(() => this.categoriaService.listarTodas());

  readonly conquistas = computed(() => {
    const prog = this.progresso();
    const obtidas = prog?.conquistas ?? [];
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
    const prog = this.progresso();
    const niveis = prog?.niveis ?? [];
    return this.categorias().map(cat => {
      const niveisCateg = niveis.filter(n => n.categoriaId === cat.id && n.concluido);
      return {
        cat,
        concluidos: niveisCateg.length,
        estrelas: niveisCateg.reduce((acc, n) => acc + n.estrelas, 0),
      };
    });
  });

  readonly totalEstrelas = computed(() => this.progresso()?.estrelas ?? 0);
  readonly totalConquistas = computed(
    () => this.progresso()?.conquistas.filter(c => c.desbloqueada).length ?? 0
  );

  ngOnInit(): void {
    this.categoriaService.carregarCategorias();
    const id = this.route.snapshot.paramMap.get('id') ?? '';

    // Fetch progresso (includes student data via endpoint)
    this.http.get<Progresso>(`${environment.apiUrl}/alunos/${id}/progresso`).subscribe({
      next: (prog) => {
        this.progresso.set(prog);
        // Construct student info from what we know
        this.estudante.set({
          id: Number(id),
          nome: `Aluno #${id}`,
          matricula: '',
          idade: 0,
        });
      },
      error: () => {
        this.router.navigate(['/professor']);
      },
    });
  }

  voltar(): void {
    this.router.navigate(['/professor']);
  }
}
