#!/usr/bin/env python3
import subprocess

#definindo uma varíavel para usuário e senha
novo_usuario = "amanda"
nova_senha = "password123"

#cria o usuário e senha no sistema Linux
subprocess.run(["sudo", "useradd",novo_usuario])
subprocess.run(["sudo", "passwd", novo_usuario],input=f"{nova_senha}\n{nova_senha}\n".encode())
