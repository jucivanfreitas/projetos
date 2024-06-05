const { Router } = require("express")

const { getLivros, getLivro,getLivroNM, postLivro, patchLivro,  delLivros } = require("../Controladores/livro")
const router =Router()


//Rotas
router.get('/', getLivros)
router.get('/id', getLivro) //http://localhost:8000/livros/id?id=1
router.get('/nm', getLivroNM) //http://localhost:8000/livros/nm?nome=demai


router.post('/', postLivro)


router.patch('/id', patchLivro)
router.delete('/id', delLivros)


// Rotas
  module.exports = router
