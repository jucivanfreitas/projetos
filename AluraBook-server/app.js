const express = require("express")
const app = express()
app.use(express.json())
const port =8000
const rotaLivro = require("./Rotas/Livro")

app.use('/livros', rotaLivro)





app.listen(port, () => {
  console.log('escutando a porta: '+ port)
})
