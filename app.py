import typer
import inquirer
import os


from helper import *



home_page()
Lang = [
    inquirer.List(
        "language",
        message="Choose language",
        choices=[typer.style('Uzbek',fg=typer.colors.GREEN),typer.style("Russian",fg=typer.colors.GREEN),typer.style("English",typer.colors.GREEN)]
    ),
    ]
x = inquirer.prompt(Lang)

if 'Uzbek' in x['language']:
    x = typer.prompt(typer.style("Foydalanuvchi nomini kiriting",fg=typer.colors.CYAN))
    if len(x)<=4:
        typer.secho("Foydalanuvchi nomi juda qisqa 5ta yoki undan ko'p bo'lishi kerak",fg=typer.colors.RED)
    else:
        nick_fast_checker(x)
elif 'Russian' in x['language']:
    x = typer.prompt(typer.style("Введите имя пользователя",fg=typer.colors.CYAN))
    if len(x)<=4:
        typer.secho("Имя пользователя должно быть очень коротким, не менее 5 символов.",fg=typer.colors.RED)
    else:
        nick_fast_checker(x)
elif 'English' in x['language']:
    x = typer.prompt(typer.style("Enter your username",fg=typer.colors.CYAN))
    if len(x)<=4:
        typer.secho("Username must be very short 5 characters or more",fg=typer.colors.RED)
    else:
        nick_fast_checker(x)

