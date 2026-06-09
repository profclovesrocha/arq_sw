const express = require('express');
const router = express.Router();
const prisma = require('../db');
const autenticado = require('../middlewares/auth');
const apenasAlunos = require('../middlewares/apenasAlunos');

router.get('/home_aluno', autenticado, apenasAlunos, async (req, res) => {
    const usuario = await prisma.usuario.findUnique({
        where: { id: req.session.usuario_id }
    });
    res.render('home_aluno', { pontos: usuario ? usuario.pontos : 0 });
});

router.post('/add_pontos', autenticado, apenasAlunos, async (req, res) => {
    await prisma.usuario.update({
        where: { id: req.session.usuario_id },
        data: { pontos: { increment: 1 } }
    });
    res.send('ok');
});

router.get('/dados_alunos', autenticado, async (req, res) => {
    const alunos = await prisma.usuario.findMany({
        where: { tipo: 'aluno' },
        select: { nome: true, pontos: true }
    });
    res.json(alunos);
});

router.get('/jogo_frase', autenticado, apenasAlunos, (req, res) => {
    res.render('jogo_frase');
});

router.get('/jogo_imagem', autenticado, apenasAlunos, (req, res) => {
    res.render('jogo_imagem');
});

router.get('/jogo_letras', autenticado, apenasAlunos, (req, res) => {
    res.render('jogo_letras');
});

module.exports = router;