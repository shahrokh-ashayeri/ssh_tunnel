import flet as ft


def main(page: ft.Page):
    page.title = "Mani SSH Tunnel Client"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "light"
    drp_ssh = ft.Dropdown(
        label="SSH Version",
        options=[ft.dropdown.Option("Version 1"), ft.dropdown.Option("Version 2")],
    )
    txt_server = ft.TextField(label="Server IP or URL")
    txt_username = ft.TextField(label="Username")
    txt_password = ft.TextField(label="Password", password=True)
    txt_port = ft.TextField(label="Port", value="444")
    txt_local_port = ft.TextField(label="local port", value=8080)
    btn_connect = ft.FilledButton(text="Connect")
    col = ft.Column(
        [
            txt_server,
            txt_username,
            txt_password,
            txt_port,
            txt_local_port,
            drp_ssh,
            btn_connect,
        ]
    )

    page.add(col)


ft.app(target=main)
