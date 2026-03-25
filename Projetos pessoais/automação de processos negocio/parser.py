import re

def parse_invoice_text(text):
    """
    Usa Expressões Regulares para extrair CNPJ, Data e Valor Total do texto.
    """
    result = {
        "CNPJ": None,
        "Data": None,
        "Valor Total": None
    }
    
    # regex pattern para CNPJ: XX.XXX.XXX/XXXX-XX ou XXXXXXXXXXXXXX
    cnpj_pattern = r'\b(\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2})\b'
    cnpj_matches = re.findall(cnpj_pattern, text)
    if cnpj_matches:
        # Podemos pegar o primeiro CNPJ listado (geralmente o emissor)
        result["CNPJ"] = cnpj_matches[0]
        
    # regex pattern para Data no formato DD/MM/AAAA ou DD-MM-AAAA
    date_pattern = r'\b(\d{2}[/-]\d{2}[/-]\d{4})\b'
    date_matches = re.findall(date_pattern, text)
    if date_matches:
        result["Data"] = date_matches[0]
        
    # regex pattern para Valores (R$ 1.234,56 ou 1234,56) - Tenta pegar o maior valor como Total
    # Isso pode variar de acordo com a NFe, mas procuramos "Valor Total", "TOTAL" ou pegamos o maior valor
    value_pattern = r'(?:R\$\s*)?(\d{1,3}(?:\.\d{3})*,\d{2})\b'
    
    # Busca por contexto de "TOTAL" ou algo assim
    total_context_pattern = r'(?i)(?:total.*?)(?:R\$\s*)?(\d{1,3}(?:\.\d{3})*,\d{2})\b'
    total_match = re.search(total_context_pattern, text)
    
    if total_match:
        result["Valor Total"] = total_match.group(1)
    else:
        # Se não achou com a palavra TOTAL, pegar todos os valores e pegar o maior (heurística)
        all_values = re.findall(value_pattern, text)
        if all_values:
            # Converter de string "1.234,56" para float para achar o max
            def to_float(val_str):
                return float(val_str.replace('.', '').replace(',', '.'))
            
            try:
                max_val_str = max(all_values, key=to_float)
                result["Valor Total"] = max_val_str
            except:
                pass
                
    return result
