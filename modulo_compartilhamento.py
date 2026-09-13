import urllib.parse


def gerar_texto_compartilhamento(nome_profissional: str, servico: str, valor: float) -> str:
    """Gera a mensagem de texto padronizada para compartilhar."""
    texto = (
        f"Olá! Gostaria de compartilhar o serviço de *{servico}* "
        f"com o profissional *{nome_profissional}* pelo app Service Clean.\n"
        f"Valor estimado: R$ {valor:.2f}\n"
        f"Baixe o app e agende também!"
    )
    return texto


def gerar_link_whatsapp(telefone: str, texto_mensagem: str) -> str:
    """Formata o link da API do WhatsApp para abrir direto na conversa."""
    # Remove caracteres não numéricos do telefone
    telefone_limpo = "".join(filter(str.isdigit, str(telefone)))

    # Codifica o texto para o formato de URL (substitui espaços por %20, etc.)
    texto_codificado = urllib.parse.quote(texto_mensagem)

    link = f"https://whatsapp.com{telefone_limpo}&text={texto_codificado}"
    return link