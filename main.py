import flet as ft


def main(page: ft.Page):
    page.title = "Mani SSH Tunnel Client"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    welcome_message = ft.Text("GUI SSH Tunnel Client", size=30)

    page.add(welcome_message)


ft.app(target=main)
