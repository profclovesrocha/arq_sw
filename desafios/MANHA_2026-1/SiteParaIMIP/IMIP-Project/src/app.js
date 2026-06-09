const express = require('express');
const session = require('express-session');
const path = require('path');

const authRoutes = require('./routes/auth');
const alunoRoutes = require('./routes/aluno');
const professorRoutes = require('./routes/professor');
const jogosRoutes = require('./routes/jogos');


const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '../views'));

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));

app.use(session({
    secret: process.env.SECRET,
    resave: false,
    saveUninitialized: false
}));

app.use('/', authRoutes);
app.use('/', alunoRoutes);
app.use('/', professorRoutes);
app.use('/', jogosRoutes);

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Algo deu errado');
});

module.exports = app;