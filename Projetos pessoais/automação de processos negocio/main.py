import os
import glob
import pandas as pd
from extractor import extract_text_from_pdf
from parser import parse_invoice_text

DATA_DIR = "data"
OUTPUT_DIR = "output"

def main():
    print("Iniciando o processamento de Notas Fiscais...")
    
    # Garante a existência dos diretórios
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Busca por PDFs
    pdf_files = glob.glob(os.path.join(DATA_DIR, "*.pdf"))
    if not pdf_files:
        print(f"Nenhum arquivo PDF encontrado na pasta '{DATA_DIR}/'.")
        print("Por favor, adicione os arquivos PDF e execute novamente.")
        return
        
    results = []
    
    for pdf_path in pdf_files:
        filename = os.path.basename(pdf_path)
        print(f"Processando: {filename}...")
        
        # 1. Extrai o Texto
        text = extract_text_from_pdf(pdf_path)
        
        if not text:
            print(f"  Aviso: Não foi possível extrair texto de {filename}")
            continue
            
        # 2. Faz o parsing com Regex
        parsed_data = parse_invoice_text(text)
        
        # 3. Adiciona o nome do arquivo aos dados
        row = {
            "Arquivo": filename,
            "CNPJ": parsed_data.get("CNPJ", "Não encontrado"),
            "Data": parsed_data.get("Data", "Não encontrado"),
            "Valor Total": parsed_data.get("Valor Total", "Não encontrado")
        }
        results.append(row)
        
    if results:
        # 4. Salva em Excel
        df = pd.DataFrame(results)
        output_file = os.path.join(OUTPUT_DIR, "relatorio.xlsx")
        df.to_excel(output_file, index=False)
        print(f"\nProcessamento concluído! O relatório foi salvo em: {output_file}")
    else:
        print("Nenhum dado extraído.")

if __name__ == "__main__":
    main()
