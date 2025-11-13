
import flet as ft
import sqlite3

# CRIAÇÃO DO BANCO
def criar_tabela():
    conn = sqlite3.connect("escola.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            email TEXT       
        )
    """)
    conn.commit()
    conn.close()

def inserir_usuario(nome, idade, email):
    conn = sqlite3.connect("escola.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, idade, email) VALUES (?, ?)", (nome, idade, email))
    conn.commit()
    conn.close()

def listar_usuarios():
    conn = sqlite3.connect("escola.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()
    conn.close()
    return dados

def main(page: ft.Page):
    page.title = "Cadastro com SQLite"
    page.theme_mode = "dark"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    criar_tabela()

    nome = ft.TextField(label="Nome", width=300)
    idade = ft.TextField(label="Idade", width=150)
    gmail = ft.TextField(label="Email", width=300)
    resultado = ft.Column()

    def atualizar_lista():
        resultado.controls.clear()
        usuarios = listar_usuarios()
        for u in usuarios:
            resultado.controls.append(ft.Text(f"ID: {u[0]} | Nome: {u[1]} | Idade: {u[2]} | Email: {u[3]}",size=20,color="Yellow"))
        page.update()

    def salvar_dados(e):
        if nome.value and idade.value and email.value:
            inserir_usuario(nome.value, idade.value, email.value)
            nome.value = ""
            idade.value = ""
            email.value = ""
            atualizar_lista()
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()

    botao_salvar = ft.ElevatedButton("Salvar", on_click=salvar_dados,bgcolor="green",color="white",width=200)

    page.add(
        ft.Text("Cadastro de Usuários", size=25, weight=ft.FontWeight.BOLD),
        ft.Row([nome, idade, email],alignment="center"),
        ft.Row([botao_salvar],alignment="center"),
        ft.Text("Usuários Cadastrados:", size=20, weight=ft.FontWeight.BOLD),
        resultado
    )

    atualizar_lista()

ft.app(target=main)