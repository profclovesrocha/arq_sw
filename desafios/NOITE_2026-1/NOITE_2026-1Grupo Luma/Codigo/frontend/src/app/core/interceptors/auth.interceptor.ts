import { HttpInterceptorFn } from '@angular/common/http';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const raw = sessionStorage.getItem('alfabe_sessao');
  if (!raw) return next(req);

  try {
    const sessao = JSON.parse(raw);
    const token = sessao.token;
    if (token) {
      const cloned = req.clone({
        setHeaders: { Authorization: `Bearer ${token}` },
      });
      return next(cloned);
    }
  } catch {
    // token inválido, segue sem auth
  }

  return next(req);
};
