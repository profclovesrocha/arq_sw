function apenasProfesor(req, res, next) {
    if (req.session.tipo !== 'professor') return res.redirect('/home_aluno');
    next();
}

module.exports = apenasProfesor;