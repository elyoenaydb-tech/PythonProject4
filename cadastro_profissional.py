import customtkinter as ctk
from tkinter import messagebox
import seguranca


class TelaCadastroProfissional(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Título da Tela
        lbl_titulo = ctk.CTkLabel(self, text="Cadastro de Profissional", font=("Arial", 24, "bold"))
        lbl_titulo.pack(pady=20)

        # Campos de Entrada de Dados
        self.txt_nome = ctk.CTkEntry(self, placeholder_text="Nome completo", width=300)
        self.txt_nome.pack(pady=10)

        self.txt_email = ctk.CTkEntry(self, placeholder_text="E-mail", width=300)
        self.txt_email.pack(pady=10)

        self.txt_profissao = ctk.CTkEntry(self, placeholder_text="Sua Profissão (Ex: Eletricista)", width=300)
        self.txt_profissao.pack(pady=10)

        self.txt_bairro = ctk.CTkEntry(self, placeholder_text="Bairro de Atendimento", width=300)
        self.txt_bairro.pack(pady=10)

        self.txt_preco = ctk.CTkEntry(self, placeholder_text="Preço Médio do Serviço (Ex: 150.00)", width=300)
        self.txt_preco.pack(pady=10)

        self.txt_pix = ctk.CTkEntry(self, placeholder_text="Chave Pix para Recebimento", width=300)
        self.txt_pix.pack(pady=10)

        self.txt_senha = ctk.CTkEntry(self, placeholder_text="Senha (letras e números)", show="*", width=300)
        self.txt_senha.pack(pady=10)

        # Botões da tela
        btn_cadastrar = ctk.CTkButton(self, text="Cadastrar Profissional", command=self.salvar_cadastro,
                                      fg_color="#5a4a42", hover_color="#453832", width=300)
        btn_cadastrar.pack(pady=20)

        btn_voltar = ctk.CTkButton(self, text="← Voltar para o Login", command=lambda: self.controller.exibir_login(),
                                   fg_color="transparent", text_color="#5a4a42", hover_color="#e0e0e0", width=300)
        btn_voltar.pack(pady=5)

    def salvar_cadastro(self):
        nome = self.txt_nome.get()
        email = seguranca.sanitizar_entrada(self.txt_email.get().lower())
        profissao = self.txt_profissao.get()
        bairro = self.txt_bairro.get()
        preco = self.txt_preco.get()
        pix = self.txt_pix.get()
        senha = self.txt_senha.get()

        if not all([nome, email, profissao, bairro, preco, pix, senha]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        senha_valida, motivo = seguranca.validar_forca_senha(senha)
        if not senha_valida:
            messagebox.showerror("Senha Fraca", motivo)
            return

        senha_cripto = seguranca.criptografar_senha(senha)

        messagebox.showinfo("Sucesso", f"Profissional {nome} cadastrado com sucesso!")
        self.controller.exibir_login()