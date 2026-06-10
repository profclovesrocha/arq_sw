const express = require('express');
const router = express.Router();
const autenticado = require('../middlewares/auth');
const apenasProfessores = require('../middlewares/apenasProfessores');

router.get('/home_professor', autenticado, apenasProfessores, (req, res) => {
    res.render('home_professor');
});

module.exports = router;