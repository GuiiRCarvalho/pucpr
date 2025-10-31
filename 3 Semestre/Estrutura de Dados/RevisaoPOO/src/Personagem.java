import java.util.List;

public class Personagem {
    private String nome;
    private String sexo;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSexo() {
        return sexo;
    }

    @Override
    public String toString() {
        return "Personagem{" +
                "nome='" + nome + '\'' +
                ", sexo='" + sexo + '\'' +
                ", altura=" + altura + '\'' +
                ", habilidades=" + habilidades + '\'' +
                '}';
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    private List<String> habilidades;

    private double altura;

    public Personagem(String nome, String sexo, double altura, List<String> habilidades) {
        this.nome = nome;
        this.sexo = sexo;
        this.altura = altura;
        this.habilidades = habilidades;
    }


    public List<String> getHabilidades() {
        return habilidades;
    }

    public void setHabilidades(List<String> habilidades) {
        this.habilidades = habilidades;
    }
}

