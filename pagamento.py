import uuid


class ResultadoPagamento:
    """Classe que representa o retorno de uma tentativa de pagamento."""

    def __init__(self, sucesso: bool, mensagem: str, codigo_pix: str = None):
        self.sucesso = sucesso
        self.mensagem = mensagem
        self.codigo_pix = codigo_pix


def calcular_split(valor_total: float, taxa_app_percentual: float = 10.0):
    """
    Calcula a divisão do pagamento entre o profissional e a plataforma.
    Exemplo: 10% de taxa do app.
    """
    try:
        valor_total = float(valor_total)
        taxa_app = valor_total * (taxa_app_percentual / 100.0)
        valor_profissional = valor_total - taxa_app
        return {
            "total": valor_total,
            "taxa_app": taxa_app,
            "profissional": valor_profissional
        }
    except (ValueError, TypeError):
        return {"total": 0.0, "taxa_app": 0.0, "profissional": 0.0}


def processar_pagamento_pix(valor: float, descricao: str = "Serviço Clean") -> ResultadoPagamento:
    """Simula a geração de um código Copia e Cola do Pix para o cliente."""
    if valor <= 0:
        return ResultadoPagamento(False, "Valor do pagamento inválido.")

    # Simula uma chave aleatória Pix (Copia e Cola)
    codigo_random = uuid.uuid4().hex
    pix_copia_e_cola = f"00020126580014BR.GOV.BCB.PIX0114servicecleanapp{codigo_random}5204000053039865405{valor:.2f}5802BR5913ServiceClean6009Sao_Paulo62070503***6304"

    return ResultadoPagamento(
        sucesso=True,
        mensagem="Pix gerado com sucesso! Copie o código para pagar no seu banco.",
        codigo_pix=pix_copia_e_cola
    )