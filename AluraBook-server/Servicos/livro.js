const fs = require("fs")

function getTodosLivros() {
    return JSON.parse( fs.readFileSync("./livros.json") )
}
function getLivroid(id) {

    const livros = JSON.parse (fs.readFileSync("./livros.json"))
    const livroFiltrado =livros.filter(livro => livro.id === id)[0]
    return livroFiltrado
}
function getLivroNome(nome) {

    const livros = JSON.parse (fs.readFileSync("./livros.json"))
    const livroFiltrado =livros.filter(livro => livro.nome.toLowerCase().includes(nome.toLowerCase()))
    return livroFiltrado
}

function insereLivro(livroNovo) {
    const livros = JSON.parse (fs.readFileSync("./livros.json"))
    const novaLista = [...livros, livroNovo]
    fs.writeFileSync("./livros.json", JSON.stringify(novaLista))
}

function modificaLivro (modificacoes,id){
    let livrosAtuais = JSON.parse (fs.readFileSync("./livros.json"))
    const indiceMode = livrosAtuais.findIndex(livro => livro.id === id)
    const conteudoMudado ={...livrosAtuais[indiceMode], ...modificacoes}
    livrosAtuais[indiceMode]=conteudoMudado

    fs.writeFileSync("./livros.json", JSON.stringify(livrosAtuais))
}
function deletaLivro(id){
    let livrosAtuais = JSON.parse (fs.readFileSync("./livros.json"))
    const excetoID = livrosAtuais.filter(livro => livro.id !== id)

    fs.writeFileSync("./livros.json", JSON.stringify(excetoID))




}

module.exports= {
    getTodosLivros, getLivroid,getLivroNome, insereLivro, modificaLivro,deletaLivro
}
