import java.util.ArrayList;
import java.util.List;

public class Estoque {
    private List <Produto> produtos;

    public Estoque() {
        this.produtos = new ArrayList<>();
    }

    public void adicionarProduto(Produto p) {
        produtos.add(p);
    }

    public boolean alterarPrecoPorNome(String nome, double novoPreco) {
        for (Produto p : produtos) {
            if (p.getNome().equalsIgnoreCase(nome)) {
                p.setPreco(novoPreco);
                return true;
            }
        }
        return false;
    }

    public void listarProdutosEmEstoque() {
        if (produtos.isEmpty()) {
            System.out.println("Estoque vazio.");
            return;
        }
        System.out.println("Produtos em estoque:");
        for (Produto p : produtos) {
            System.out.println(p);
        }
    }
}

