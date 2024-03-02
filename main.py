import flet as ft
from lib.connection import Connection

def main(page: ft.Page):
    page.title = "Mani SSH Tunnel Client"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "light"
    
    # Dropdown for SSH version selection
    ssh_options = [ft.dropdown.Option("Version 1"), ft.dropdown.Option("Version 2")]
    drp_ssh = ft.Dropdown(label="SSH Version", options=ssh_options)
    
    # Text fields for user input
    txt_server = ft.TextField(label="Server IP or URL")
    txt_username = ft.TextField(label="Username")
    txt_password = ft.TextField(label="Password", password=True)
    txt_port = ft.TextField(label="Port", value="444")
    txt_local_port = ft.TextField(label="Local Port", value="8080")
    
    # Button for initiating connection
    btn_connect = ft.FilledButton(text="Connect")
    
    # Text field for displaying connection status
    txt_status = ft.TextField(value=Connection().is_alive(), readonly=True)
    
    # Organize elements into a column layout
    col = ft.Column([
        txt_status,
        txt_server,
        txt_username,
        txt_password,
        txt_port,
        txt_local_port,
        drp_ssh,
        btn_connect
    ])

    page.add(col)

# Run the Flet application
ft.app(target=main)

