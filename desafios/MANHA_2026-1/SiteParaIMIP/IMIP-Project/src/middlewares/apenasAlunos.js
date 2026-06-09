function apenasAluno(req, res, next) {
    if (req.session.tipo !== 'aluno') return res.redirect('/home_professor');
    next();
}

module.exports = apenasAluno;