#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER
from datetime import datetime

# Dados do projeto
ALUNOS = ["Guilherme Reis", "Nicolas Lobo", "Vinicius Trevisan"]
EQUIPE = 6
TITULO_PROJETO = "Sistema de Gestão Hospitalar"
DATA = datetime.now().strftime("%d de %B de %Y")

# Distribuição de classes entre alunos
DISTRIBUICAO = {
    "Vinicius Trevisan": {
        "model": ["Pessoa", "Paciente", "Consulta", "Internacao"],
        "ui": ["JanelaPrincipal", "PacienteUI", "ConsultaUI", "InternacaoUI"],
        "outras": []
    },
    "Guilherme Reis": {
        "model": ["Funcionario", "Medico", "TipoSanguineo"],
        "ui": ["MedicoUI"],
        "outras": []
    },
    "Nicolas Lobo": {
        "model": ["Medicamento", "Pagavel", "Enfermeiro"],
        "ui": ["EnfermeiroUI", "MedicamentoUI"],
        "outras": ["Repositorio", "Main"]
    }
}

# Descrições detalhadas das classes
DESCRICOES_CLASSES = {
    "Pessoa": {
        "tipo": "Classe Abstrata",
        "descricao": "Classe base que representa uma pessoa no sistema. Contém atributos comuns como nome, endereço e data de nascimento. Serve como superclasse para Paciente e Funcionario.",
        "atributos": ["String nome", "String endereco", "LocalDate dataNascimento"],
        "metodos": [
            "Pessoa(String, String, LocalDate) - Construtor",
            "getNome() : String",
            "setNome(String) : void",
            "getEndereco() : String",
            "setEndereco(String) : void",
            "getDataNascimento() : LocalDate",
            "setDataNascimento(LocalDate) : void"
        ]
    },
    "Paciente": {
        "tipo": "Classe Concreta",
        "descricao": "Representa um paciente no hospital. Herda de Pessoa e adiciona informações específicas como ID automático, tipo sanguíneo, convênio e CPF. Implementa Serializable para persistência.",
        "atributos": ["int id", "TipoSanguineo tipoSanguineo", "String convenio", "String cpf"],
        "metodos": [
            "Paciente(String, String, LocalDate, TipoSanguineo, String, String) - Construtor",
            "getId() : int",
            "getTipoSanguineo() : TipoSanguineo",
            "setTipoSanguineo(TipoSanguineo) : void",
            "getConvenio() : String",
            "setConvenio(String) : void",
            "getCpf() : String",
            "setCpf(String) : void",
            "toString() : String"
        ]
    },
    "Funcionario": {
        "tipo": "Classe Abstrata",
        "descricao": "Classe abstrata que representa um funcionário do hospital. Herda de Pessoa e adiciona informações de trabalho como matrícula, salário e carga horária. Base para Medico e Enfermeiro.",
        "atributos": ["String matricula", "double salario", "double cargaHoraria"],
        "metodos": [
            "Funcionario(String, String, LocalDate, String, double, double) - Construtor",
            "calcularSalario() : double",
            "getDados() : String",
            "getMatricula() : String",
            "setMatricula(String) : void",
            "getSalario() : double",
            "setSalario(double) : void",
            "getCargaHoraria() : double",
            "setCargaHoraria(double) : void"
        ]
    },
    "Medico": {
        "tipo": "Classe Concreta",
        "descricao": "Representa um médico no hospital. Herda de Funcionario e adiciona informações médicas como CRM, especialidade e indicação de plantão. Possui ID automático.",
        "atributos": ["int id", "String crm", "String especialidade", "boolean plantao"],
        "metodos": [
            "Medico(String, String, LocalDate, String, double, double, String, String, boolean) - Construtor",
            "getId() : int",
            "getCrm() : String",
            "setCrm(String) : void",
            "getEspecialidade() : String",
            "setEspecialidade(String) : void",
            "isPlantao() : boolean",
            "setPlantao(boolean) : void",
            "toString() : String"
        ]
    },
    "Enfermeiro": {
        "tipo": "Classe Concreta",
        "descricao": "Representa um enfermeiro no hospital. Herda de Funcionario e adiciona COREN, turno e nível. Possui ID automático e método para administrar medicamentos.",
        "atributos": ["int id", "String coren", "String turno", "int nivel"],
        "metodos": [
            "Enfermeiro(String, String, LocalDate, String, double, double, String, String, int) - Construtor",
            "getId() : int",
            "getCoren() : String",
            "setCoren(String) : void",
            "getTurno() : String",
            "setTurno(String) : void",
            "getNivel() : int",
            "setNivel(int) : void",
            "administrarMedicamento(String) : void",
            "toString() : String"
        ]
    },
    "Consulta": {
        "tipo": "Classe Concreta",
        "descricao": "Representa uma consulta médica. Implementa Pagavel para cálculo de valores com desconto. Armazena data, hora, valor, nomes do paciente e médico. Possui ID automático.",
        "atributos": ["int id", "LocalDateTime dataHora", "double valor", "double desconto", "String nomePaciente", "String nomeMedico"],
        "metodos": [
            "Consulta(LocalDateTime, double, String, String) - Construtor",
            "getId() : int",
            "calcularTotal() : double",
            "gerarFatura() : String",
            "aplicarDesconto(double) : void",
            "emitirRecibo() : String",
            "getDataHora() : LocalDateTime",
            "setDataHora(LocalDateTime) : void",
            "getValor() : double",
            "setValor(double) : void"
        ]
    },
    "Internacao": {
        "tipo": "Classe Concreta",
        "descricao": "Representa uma internação hospitalar. Implementa Pagavel com cálculo baseado em diárias. Armazena datas de entrada e saída, diagnóstico e nome do paciente. Possui ID automático.",
        "atributos": ["int id", "LocalDate dataEntrada", "LocalDate dataSaida", "String diagnostico", "String nomePaciente", "double desconto"],
        "metodos": [
            "Internacao(LocalDate, LocalDate, String, String) - Construtor",
            "getId() : int",
            "getDias() : long",
            "calcularTotal() : double",
            "gerarFatura() : String",
            "aplicarDesconto(double) : void",
            "emitirRecibo() : String",
            "getDataEntrada() : LocalDate",
            "setDataEntrada(LocalDate) : void",
            "getDataSaida() : LocalDate",
            "setDataSaida(LocalDate) : void"
        ]
    },
    "Medicamento": {
        "tipo": "Classe Concreta",
        "descricao": "Representa um medicamento no estoque do hospital. Armazena código ANVISA, nome e quantidade em estoque. Possui métodos para verificar e atualizar estoque.",
        "atributos": ["String codigoAnvisa", "String nome", "int estoque"],
        "metodos": [
            "Medicamento(String, String, int) - Construtor",
            "verificarEstoque() : boolean",
            "atualizarEstoque(int) : void",
            "getCodigoAnvisa() : String",
            "setCodigoAnvisa(String) : void",
            "getNome() : String",
            "setNome(String) : void",
            "getEstoque() : int",
            "setEstoque(int) : void",
            "toString() : String"
        ]
    },
    "TipoSanguineo": {
        "tipo": "Enumeração",
        "descricao": "Enumeração que define os tipos sanguíneos possíveis: A+, A-, B+, B-, O+, O-, AB+, AB-. Cada tipo possui uma descrição textual.",
        "atributos": ["A_POS, A_NEG, B_POS, B_NEG, O_POS, O_NEG, AB_POS, AB_NEG"],
        "metodos": [
            "toString() : String - retorna descrição (ex: 'A+')"
        ]
    },
    "Pagavel": {
        "tipo": "Interface",
        "descricao": "Interface que define o contrato para objetos pagáveis no sistema. Implementada por Consulta e Internacao, fornecendo métodos para cálculo de totais, geração de faturas e recibos.",
        "atributos": [],
        "metodos": [
            "calcularTotal() : double",
            "gerarFatura() : String",
            "aplicarDesconto(double) : void",
            "emitirRecibo() : String"
        ]
    },
    "JanelaPrincipal": {
        "tipo": "Classe de Interface (JavaFX Stage)",
        "descricao": "Janela principal do sistema que fornece acesso a todas as funcionalidades através de menus. Menu bar com opções de Arquivo, Pacientes, Funcionários, Atendimentos e Estoque. Abre outras janelas conforme necessário.",
        "atributos": ["MenuBar menuBar", "VBox root"],
        "metodos": [
            "JanelaPrincipal() - Construtor que configura todos os menus"
        ]
    },
    "PacienteUI": {
        "tipo": "Classe de Interface (JavaFX Stage)",
        "descricao": "Interface gráfica para gestão de pacientes. Permite adicionar, editar e excluir pacientes. Contém formulário com campos para nome, CPF, endereço, data de nascimento, tipo sanguíneo e convênio. Tabela exibe lista de pacientes com opções de editar e excluir.",
        "atributos": ["TableView<Paciente> tabela", "Repositorio<Paciente> repositorio", "TextField campoNome, campoCpf, campoEndereco, etc."],
        "metodos": [
            "PacienteUI() - Construtor",
            "criarFormulario() : GridPane",
            "criarTabela() : TableView<Paciente>",
            "salvar() : void",
            "preencherFormulario(Paciente) : void",
            "limparFormulario() : void",
            "confirmarExclusao(String) : boolean",
            "mostrarErro(String) : void"
        ]
    },
    "MedicoUI": {
        "tipo": "Classe de Interface (JavaFX Stage)",
        "descricao": "Interface gráfica para gestão de médicos. Permite gerenciar cadastro de médicos com campos como nome, CRM, especialidade, matrícula, salário, carga horária, endereço, data de nascimento e checkbox de plantão. Inclui tabela com lista de médicos.",
        "atributos": ["TableView<Medico> tabela", "Repositorio<Medico> repositorio", "TextField campoNome, campoCrm, etc.", "CheckBox campoPlantao"],
        "metodos": [
            "MedicoUI() - Construtor",
            "criarFormulario() : GridPane",
            "criarTabela() : TableView<Medico>",
            "salvar() : void",
            "preencherFormulario(Medico) : void",
            "limparFormulario() : void",
            "confirmarExclusao(String) : boolean",
            "mostrarErro(String) : void"
        ]
    },
    "EnfermeiroUI": {
        "tipo": "Classe de Interface (JavaFX Stage)",
        "descricao": "Interface gráfica para gestão de enfermeiros. Permite gerenciar cadastro de enfermeiros com campos como nome, COREN, turno, nível, matrícula, salário, carga horária, endereço e data de nascimento. Inclui tabela com lista de enfermeiros.",
        "atributos": ["TableView<Enfermeiro> tabela", "Repositorio<Enfermeiro> repositorio", "TextField campoNome, campoCoren, etc."],
        "metodos": [
            "EnfermeiroUI() - Construtor",
            "criarFormulario() : GridPane",
            "criarTabela() : TableView<Enfermeiro>",
            "salvar() : void",
            "preencherFormulario(Enfermeiro) : void",
            "limparFormulario() : void",
            "confirmarExclusao(String) : boolean",
            "mostrarErro(String) : void"
        ]
    },
    "ConsultaUI": {
        "tipo": "Classe de Interface (JavaFX Stage)",
        "descricao": "Interface gráfica para gestão de consultas. Permite adicionar, editar e excluir consultas. Campos para data/hora, valor, nomes de paciente e médico, e desconto. Tabela exibe lista de consultas com opções de editar e excluir.",
        "atributos": ["TableView<Consulta> tabela", "Repositorio<Consulta> repositorio", "TextField campoDataHora, campoValor, etc."],
        "metodos": [
            "ConsultaUI() - Construtor",
            "criarFormulario() : GridPane",
            "criarTabela() : TableView<Consulta>",
            "salvar() : void",
            "preencherFormulario(Consulta) : void",
            "limparFormulario() : void",
            "confirmarExclusao(String) : boolean",
            "mostrarErro(String) : void"
        ]
    },
    "InternacaoUI": {
        "tipo": "Classe de Interface (JavaFX Stage)",
        "descricao": "Interface gráfica para gestão de internações. Permite registrar e gerenciar internações com campos para nome do paciente, data de entrada, data de saída, diagnóstico e desconto. Tabela exibe lista com opções de editar e excluir.",
        "atributos": ["TableView<Internacao> tabela", "Repositorio<Internacao> repositorio", "TextField campoNomePaciente, campoDataEntrada, etc."],
        "metodos": [
            "InternacaoUI() - Construtor",
            "criarFormulario() : GridPane",
            "criarTabela() : TableView<Internacao>",
            "salvar() : void",
            "preencherFormulario(Internacao) : void",
            "limparFormulario() : void",
            "confirmarExclusao(String) : boolean",
            "mostrarErro(String) : void"
        ]
    },
    "MedicamentoUI": {
        "tipo": "Classe de Interface (JavaFX Stage)",
        "descricao": "Interface gráfica para gestão de medicamentos no estoque. Permite adicionar, editar e excluir medicamentos com campos para código ANVISA, nome e quantidade em estoque. Tabela exibe lista de medicamentos.",
        "atributos": ["TableView<Medicamento> tabela", "Repositorio<Medicamento> repositorio", "TextField campoCodigoAnvisa, campoNome, campoEstoque"],
        "metodos": [
            "MedicamentoUI() - Construtor",
            "criarFormulario() : GridPane",
            "criarTabela() : TableView<Medicamento>",
            "salvar() : void",
            "preencherFormulario(Medicamento) : void",
            "limparFormulario() : void",
            "confirmarExclusao(String) : boolean",
            "mostrarErro(String) : void"
        ]
    },
    "Repositorio": {
        "tipo": "Classe Genérica",
        "descricao": "Classe genérica responsável por persistência de dados usando serialização Java. Armazena objetos em arquivos .dat no diretório ~/hospital-data. Fornece métodos para carregar e salvar listas de objetos.",
        "atributos": ["String caminhoArquivo"],
        "metodos": [
            "Repositorio(String) - Construtor com nome do arquivo",
            "carregar() : List<T>",
            "salvar(List<T>) : void"
        ]
    },
    "Main": {
        "tipo": "Classe Principal",
        "descricao": "Classe inicial da aplicação. Estende Application do JavaFX e inicializa a janela principal (JanelaPrincipal).",
        "atributos": [],
        "metodos": [
            "start(Stage) : void",
            "main(String[]) : void"
        ]
    }
}

def criar_pdf():
    # Criar documento
    pdf_path = "/Users/vinitrevisan/Documents/pucpr/4semestre/poo/ra3/Documentacao_Projeto_Equipe6.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            rightMargin=0.5*inch, leftMargin=0.5*inch,
                            topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    styles = getSampleStyleSheet()
    story = []
    
    # Estilos personalizados
    titulo_style = ParagraphStyle(
        'TituloCustom',
        parent=styles['Normal'],
        fontSize=28,
        textColor=colors.HexColor('#003366'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitulo_style = ParagraphStyle(
        'SubtituloCustom',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#333333'),
        spaceAfter=12,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'HeadingCustom',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#003366'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    # CAPA
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph(TITULO_PROJETO, titulo_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(f"Equipe {EQUIPE}", subtitulo_style))
    story.append(Spacer(1, 0.8*inch))
    
    # Nomes dos alunos em ordem alfabética
    nomes_ordenados = sorted(ALUNOS)
    for nome in nomes_ordenados:
        story.append(Paragraph(nome, styles['Normal']))
        story.append(Spacer(1, 0.15*inch))
    
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph(DATA, styles['Normal']))
    
    story.append(PageBreak())
    
    # DESCRIÇÃO DO PROJETO
    story.append(Paragraph("Descrição do Projeto", heading_style))
    
    descricao_projeto = """
    <b>Sistema de Gestão Hospitalar</b> é uma aplicação desenvolvida em Java utilizando JavaFX para a interface gráfica. 
    O sistema foi concebido como parte da disciplina de Programação Orientada a Objetos (POO) e visa demonstrar os 
    conceitos fundamentais da OOP, como herança, polimorfismo, encapsulamento e interfaces.<br/><br/>
    
    <b>Objetivo:</b> O projeto propõe-se a resolver a necessidade de gerenciar informações de um hospital, incluindo 
    cadastro de pacientes, funcionários (médicos e enfermeiros), consultas, internações e medicamentos em estoque.<br/><br/>
    
    <b>Funcionalidades Principais:</b><br/>
    • Gestão completa de pacientes (cadastro, edição, exclusão)<br/>
    • Gestão de médicos com informações de especialidade e plantões<br/>
    • Gestão de enfermeiros com turno e nível<br/>
    • Registro de consultas com cálculo de valores e aplicação de descontos<br/>
    • Registro de internações com cálculo de diárias<br/>
    • Controle de estoque de medicamentos<br/>
    • Geração de faturas e recibos para consultas e internações<br/>
    • Persistência de dados em arquivos serializados<br/><br/>
    
    <b>Tecnologias Utilizadas:</b><br/>
    • Linguagem: Java 21<br/>
    • Interface Gráfica: JavaFX 21<br/>
    • Build: Maven<br/>
    • Padrão de Projeto: MVC (Model-View-Controller)<br/>
    • Persistência: Serialização Java<br/>
    """
    
    story.append(Paragraph(descricao_projeto, styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(PageBreak())
    
    # DOCUMENTAÇÃO DE CLASSES
    story.append(Paragraph("Documentação de Classes", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    for indice, aluno in enumerate(sorted(ALUNOS)):
        if indice > 0:
            story.append(PageBreak())
        story.append(Paragraph(f"Classes Implementadas por {aluno}", heading_style))
        story.append(Spacer(1, 0.15*inch))
        
        # Classes Model
        if DISTRIBUICAO[aluno]["model"]:
            story.append(Paragraph("<b>Classes de Modelo (Model):</b>", styles['Normal']))
            for classe_nome in DISTRIBUICAO[aluno]["model"]:
                nome_limpo = classe_nome.split(" (")[0]
                if nome_limpo in DESCRICOES_CLASSES:
                    descricao = DESCRICOES_CLASSES[nome_limpo]
                    
                    story.append(Spacer(1, 0.25*inch))
                    story.append(Paragraph(f"<b>{classe_nome}</b> ({descricao['tipo']})", heading_style))
                    
                    # Descrição
                    story.append(Paragraph(f"<b>Descrição:</b><br/>{descricao['descricao']}", styles['Normal']))
                    story.append(Spacer(1, 0.1*inch))
                    
                    # Atributos
                    if descricao['atributos']:
                        atributos_text = "<b>Atributos:</b><br/>" + "<br/>".join(f"• {attr}" for attr in descricao['atributos'])
                        story.append(Paragraph(atributos_text, styles['Normal']))
                        story.append(Spacer(1, 0.1*inch))
                    
                    # Métodos
                    metodos_text = "<b>Métodos Principais:</b><br/>" + "<br/>".join(f"• {met}" for met in descricao['metodos'][:8])
                    story.append(Paragraph(metodos_text, styles['Normal']))
            
            story.append(Spacer(1, 0.2*inch))
        
        # Classes UI
        if DISTRIBUICAO[aluno]["ui"]:
            story.append(PageBreak())
            story.append(Paragraph(f"<b>Classes de Interface (UI) - {aluno}:</b>", heading_style))
            
            for ui_nome in DISTRIBUICAO[aluno]["ui"]:
                story.append(Spacer(1, 0.2*inch))
                story.append(Paragraph(f"<b>{ui_nome}</b> (Interface Gráfica)", heading_style))
                
                if ui_nome in DESCRICOES_CLASSES:
                    descricao = DESCRICOES_CLASSES[ui_nome]
                    story.append(Paragraph(f"<b>Descrição:</b><br/>{descricao['descricao']}", styles['Normal']))
                    story.append(Spacer(1, 0.1*inch))
                    
                    metodos_text = "<b>Métodos Principais:</b><br/>" + "<br/>".join(f"• {met}" for met in descricao['metodos'])
                    story.append(Paragraph(metodos_text, styles['Normal']))

        # Outras classes
        if DISTRIBUICAO[aluno]["outras"]:
            story.append(PageBreak())
            story.append(Paragraph(f"<b>Outras Classes - {aluno}:</b>", heading_style))
            
            for outras_nome in DISTRIBUICAO[aluno]["outras"]:
                if outras_nome in DESCRICOES_CLASSES:
                    descricao = DESCRICOES_CLASSES[outras_nome]
                    
                    story.append(Spacer(1, 0.2*inch))
                    story.append(Paragraph(f"<b>{outras_nome}</b> ({descricao['tipo']})", heading_style))
                    story.append(Paragraph(f"<b>Descrição:</b><br/>{descricao['descricao']}", styles['Normal']))
                    story.append(Spacer(1, 0.1*inch))
                    
                    metodos_text = "<b>Métodos:</b><br/>" + "<br/>".join(f"• {met}" for met in descricao['metodos'])
                    story.append(Paragraph(metodos_text, styles['Normal']))
    
    # Compilar PDF
    doc.build(story)

if __name__ == "__main__":
    criar_pdf()
