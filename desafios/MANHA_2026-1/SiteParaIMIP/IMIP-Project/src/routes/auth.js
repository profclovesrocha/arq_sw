const bcrypt = require('bcrypt');
const express = require('express');
const router = express.Router();
const prisma = require('../db');

router.get('/', (req, res) => {
    res.render('cadastro', { erro: null });
});

router.post('/', async (req, res) => {
    const { nome, email, senha, tipo } = req.body;
    try {
        const hash = await bcrypt.hash(senha, 10);
        await prisma.usuario.create({
            data: { nome, email, senha: hash, tipo }
        });
        res.redirect('/login');
    } catch (err) {
        res.render('cadastro', { erro: 'Email ja cadastrado!' });
    }
});

router.get('/login', (req, res) => {
    res.render('login', { erro: null });
});

router.post('/login', async (req, res) => {
    const { email, senha, tipo } = req.body;
    const usuario = await prisma.usuario.findFirst({
        where: { email, tipo }
    });

    if (usuario && await bcrypt.compare(senha, usuario.senha)) {
        req.session.usuario_id = usuario.id;
        req.session.tipo = usuario.tipo;
        res.redirect(usuario.tipo === 'aluno' ? '/home_aluno' : '/home_professor');
    } else {
        res.render('login', { erro: 'Login inválido' });
    }
});

router.get('/logout', (req, res) => {
    req.session.destroy(() => {
        res.redirect('/login');
    });
});

module.exports = router;