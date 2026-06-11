import { Routes } from '@angular/router';
import { estudanteGuard } from './core/guards/estudante.guard';
import { professorGuard } from './core/guards/professor.guard';

export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  {
    path: 'login',
    loadComponent: () =>
      import('./features/auth/login-page/login-page.component').then(m => m.LoginPageComponent),
  },
  {
    path: 'cadastro',
    loadComponent: () =>
      import('./features/auth/cadastro-page/cadastro-page.component').then(m => m.CadastroPageComponent),
  },
  {
    path: 'aprendizado',
    canActivate: [estudanteGuard],
    loadComponent: () =>
      import('./features/estudante/dashboard-page/dashboard-page.component').then(m => m.DashboardPageComponent),
  },
  {
    path: 'licao/:categoriaId/:nivelId',
    canActivate: [estudanteGuard],
    loadComponent: () =>
      import('./features/estudante/licao-page/licao-page.component').then(m => m.LicaoPageComponent),
  },
  {
    path: 'perfil',
    canActivate: [estudanteGuard],
    loadComponent: () =>
      import('./features/estudante/perfil-page/perfil-page.component').then(m => m.PerfilPageComponent),
  },
  {
    path: 'professor',
    canActivate: [professorGuard],
    loadComponent: () =>
      import('./features/professor/painel-page/painel-page.component').then(m => m.PainelPageComponent),
  },
  {
    path: 'professor/aluno/:id',
    canActivate: [professorGuard],
    loadComponent: () =>
      import('./features/professor/aluno-detalhe-page/aluno-detalhe-page.component').then(
        m => m.AlunoDetalhePageComponent,
      ),
  },
  { path: '**', redirectTo: 'login' },
];
