import bcrypt
import re


def criptografar_senha(senha: str) -> str:
    """Transforma a senha em um hash seguro."""
    bytes_senha = senha.encode('utf-8')
    sal = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(bytes_senha, sal)
    return hash_senha.decode('utf-8')


def verificar_senha(senha_digitada: str, senha_banco: str) -> bool:
    """Verifica se a senha digitada corresponde ao hash do banco."""
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_banco.encode('utf-8'))


def sanitizar_entrada(texto: str) -> str:
    """
    Limpa o texto de entrada (como e-mail ou nome) removendo caracteres
    comuns em ataques de invasão (SQL Injection) e espaços desnecessários.
    """
    if not texto:
        return ""
    texto_limpo = texto.strip()
    texto_limpo = re.sub(r"['\";\-]", "", texto_limpo)
    return texto_limpo


def validar_forca_senha(senha: str):
    """
    Valida se a senha atende aos critérios mínimos de segurança.
    Retorna uma tupla: (bool indicando se é válida, 'mensagem de motivo caso seja inválida')
    """
    if not senha or len(senha) < 6:
        return False, "A senha deve ter pelo menos 6 caracteres."

    # Verifica se contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False, "A senha deve conter pelo menos um número."

    return True, "Senha válida."