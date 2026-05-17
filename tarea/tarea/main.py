from views import MenuPrincipal
from core import Screen

def main():
    Screen.limpiar()
    app = MenuPrincipal()
    app.menuPrincipal()


if __name__ == "__main__":
    main()