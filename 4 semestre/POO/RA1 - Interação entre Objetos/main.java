public class main {
    public static void main(String[] args) {
        Professor professor = new Professor("Carlos Mendes", "P-042");
        Aluno aluno = new Aluno("Ana Souza", "2024001");
        Disciplina disciplina = new Disciplina("Estruturas de Dados", professor, aluno);

        disciplina.exibirInformacoes();
    }
}

class Professor {
    private String nome;
    private String identificador;

    public Professor(String nome, String identificador) {
        this.nome = nome;
        this.identificador = identificador;
    }

    public String getNome() {
        return nome;
    }

    public String getIdentificador() {
        return identificador;
    }
}

class Disciplina {
    private String nome;
    private Professor professor;
    private Aluno aluno;

    public Disciplina(String nome, Professor professor, Aluno aluno) {
        this.nome = nome;
        this.professor = professor;
        this.aluno = aluno;
    }

    public void exibirInformacoes() {
        System.out.println("=== Informações da Disciplina ===");
        System.out.println("Disciplina : " + nome);
        System.out.println("Professor  : " + professor.getNome() +
                           " (ID: " + professor.getIdentificador() + ")");
        System.out.println("Aluno      : " + aluno.getNome() +
                           " (Matrícula: " + aluno.getMatricula() + ")");
    }
}

class Aluno {
    private String nome;
    private String matricula;

    public Aluno(String nome, String matricula) {
        this.nome = nome;
        this.matricula = matricula;
    }

    public String getNome() {
        return nome;
    }

    public String getMatricula() {
        return matricula;
    }
}