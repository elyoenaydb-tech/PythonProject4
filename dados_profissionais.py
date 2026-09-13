# Lista simples exigida pelo seu main.py (Linha 279)
PROFISSOES = [
    "Diarista",
    "Faxineiro(a)",
    "Passador(a) de Roupa",
    "Lavador(a) de Sofá/Estofados",
    "Limpador(a) de Piscina",
    "Jardineiro(a)",
    "Organizador(a) de Ambientes (Personal Organizer)",
    "Pintor(a)",
    "Eletricista (Residencial)",
    "Encanador(a)"
]

# Listas padrões para alimentar o banco de dados
HORARIOS_PADRAO = ["08:00", "10:00", "14:00", "16:00"]
COMENTARIOS_PADRAO = [
    "Excelente profissional, muito pontual!",
    "Serviço impecável, recomendo com certeza.",
    "Muito educado(a) e caprichoso(a)."
]

# Dicionário completo contendo absolutamente todas as chaves exigidas pelo seu database.py
PROFISSIONAIS_POR_CATEGORIA = {
    "Limpeza": [
        {"nome": "Diarista", "avaliacao": "5.0", "preco": "150.00", "preco_valor": "150.00", "bairro": "Centro", "pix_key": "diarista@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO},
        {"nome": "Faxineiro(a)", "avaliacao": "4.8", "preco": "130.00", "preco_valor": "130.00", "bairro": "Vila Nova", "pix_key": "faxina@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO},
        {"nome": "Passador(a) de Roupa", "avaliacao": "4.7", "preco": "80.00", "preco_valor": "80.00", "bairro": "Jardins", "pix_key": "passador@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO}
    ],
    "Manutenção": [
        {"nome": "Limpador(a) de Piscina", "avaliacao": "4.9", "preco": "120.00", "preco_valor": "120.00", "bairro": "Centro", "pix_key": "piscina@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO},
        {"nome": "Jardineiro(a)", "avaliacao": "4.6", "preco": "100.00", "preco_valor": "100.00", "bairro": "Alvorada", "pix_key": "jardim@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO},
        {"nome": "Pintor(a)", "avaliacao": "4.8", "preco": "200.00", "preco_valor": "200.00", "bairro": "Planalto", "pix_key": "pintor@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO},
        {"nome": "Eletricista (Residencial)", "avaliacao": "5.0", "preco": "180.00", "preco_valor": "180.00", "bairro": "Vila Rica", "pix_key": "eletrica@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO},
        {"nome": "Encanador(a)", "avaliacao": "4.7", "preco": "140.00", "preco_valor": "140.00", "bairro": "Centro", "pix_key": "encanador@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO}
    ],
    "Organização": [
        {"nome": "Organizador(a) de Ambientes (Personal Organizer)", "avaliacao": "4.9", "preco": "250.00", "preco_valor": "250.00", "bairro": "Jardins", "pix_key": "organizer@email.com", "horarios": HORARIOS_PADRAO, "horários": HORARIOS_PADRAO, "comentarios": COMENTARIOS_PADRAO, "comentários": COMENTARIOS_PADRAO}
    ]
}