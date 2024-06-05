// controladores > livro.js

const { is } = require("express/lib/request")
const { getTodosLivros,getLivroid,getLivroNome, insereLivro,modificaLivro, deletaLivro } = require("../Servicos/livro")

function getLivros(req, res) {
    try {
        const livros = getTodosLivros()
        res.send(livros)
    } catch (error) {
        res.status(500)
        res.send(error.message)
    }
}
function getLivro(req, res) {
    try {
        const id = req.query.id;

        // Verifica se o id é válido (exemplo de verificação simples)
        if (!Number(id))  {
            res.status(422).json({code: 422, error: 'ID digitado é inválido. dígite um número inteiro. ' + id + '. Tente outro id.', resolution: '400 Bad req'})
            return;

        }

        const livro = getLivroid(id);

        if (!livro) {
            res.status(404).json({ code: 404 , error: 'Livro não encontrado para o id: '+ id +'. Tente Outro id.', resolution: '404 Not Found - O recurso solicitado não foi encontrado, mas poderá estar disponível novamente no futuro. Solicitações subsequentes do cliente são permitidas.' });
            return;
        }

        res.json(livro);
    } catch (error) {
        res.status(500).send(error.message);
    }}

    function getLivroNM(req, res) {
        try {
            const nome = req.query.nome;

            // Verifica se o nome é válido (exemplo de verificação simples)
            if (!nome) {
                res.status(400).json({code: 400, error: 'nome inválido para o livro. ' + nome + '. Tente outro nome.', resolution: '400 Bad req'})
                return;
            }

            const livro = getLivroNome(nome);

            if (!livro) {
                res.status(404).json({ code: 404 , error: 'Livro não encontrado para o nome: '+ nome +'. Tente Outro nome.', resolution: '404 Not Found - O recurso solicitado não foi encontrado, mas poderá estar disponível novamente no futuro. Solicitações subsequentes do cliente são permitidas.' });
                return;
            }

            res.json(livro);
        } catch (error) {
            res.status(500).send(error.message);
        }



}

function postLivro(req, res) {

    try {
        const livroNovo = req.body
        insereLivro(livroNovo)
        res.send('Livro inserido com sucesso!'+ livroNovo + req.body)
        res.status(201)

    }catch (error) {
        res.status(500)
        res.send(error.message)
    }
}

function patchLivro(req,res){
    try {
        const id =req.query.id
        const body =req.body

        modificaLivro(body,id)
        res.send("Itesn Modificado com sucesso")


    } catch (error) {
        res.status(500)
        res.send(error.message)

    }

}

function delLivros(req,res) {
    try {
        const id =req.query.id
        deletaLivro(id)
        res.send("Item Deletado ")

    } catch (error) {
        res.status(500)
        res.send(error.message)

    }

}




module.exports = {
    getLivros, getLivro, getLivroNM, postLivro, patchLivro, delLivros}
