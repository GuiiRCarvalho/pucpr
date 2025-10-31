import java.util.List;

public class SuperHeroi extends Personagem {

    public SuperHeroi(String nome, String sexo, double altura, List<String> habilidades) {
        super(nome, sexo, altura, habilidades);
    }

    public void usarHabilidades() {
        System.out.println(getNome() + " esta usando as habilidades: "
        + getHabilidades());
    }
}
