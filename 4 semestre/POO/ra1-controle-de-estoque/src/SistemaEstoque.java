public class SistemaEstoque {
    public static void main(String[] args) {
        Estoque estoque = new Estoque();

        // Criar e adicionar pelo menos 10 produtos
        estoque.adicionarProduto(new Produto("Notebook", 4500.00));
        estoque.adicionarProduto(new Produto("Celular", 3000.00));
        estoque.adicionarProduto(new Produto("Teclado", 150.00));
        estoque.adicionarProduto(new Produto("Mouse", 80.00));
        estoque.adicionarProduto(new Produto("Monitor", 1200.00));
        estoque.adicionarProduto(new Produto("Cabo HDMI", 50.00));
        estoque.adicionarProduto(new Produto("Impressora", 900.00));
        estoque.adicionarProduto(new Produto("Roteador", 300.00));
        estoque.adicionarProduto(new Produto("SSD 1TB", 600.00));
        estoque.adicionarProduto(new Produto("Fone de Ouvido", 200.00));

        // Listar todos os produtos
        estoque.listarProdutosEmEstoque();

        // Alterar o preço do produto "Celular" para 5000,00
        boolean alterou = estoque.alterarPrecoPorNome("Celular", 5000.00);
        if (alterou) {
            System.out.println("Preço do produto 'Celular' alterado para R$ 5000,00");
        } else {
            System.out.println("Produto não encontrado");
        }

        // Listar novamente todos os produtos
        estoque.listarProdutosEmEstoque();

        // Tentar alterar o preço de um produto que não está no estoque
        boolean alterouNaoExiste = estoque.alterarPrecoPorNome("Bicicleta", 1200.00);
        if (!alterouNaoExiste) {
            System.out.println("Produto não encontrado");
        }
    }
}
