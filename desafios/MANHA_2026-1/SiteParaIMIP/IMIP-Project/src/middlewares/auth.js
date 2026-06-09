function autenticado(req, res, next) {
    if (!req.session.usuario_id) return res.redirect('/login');
    next();
}

module.exports = autenticado;