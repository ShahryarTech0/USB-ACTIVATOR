from src.models.user import add_user
from datetime import datetime
import tkinter as tk
from datetime import datetime

from src.gui.LoginPage import LoginPage
from src.models.user import session, add_user

def main():
    # Add Admin user
    add_user(
        name='Admin',
        username='admin4',
        password='admin123',
        email='admin@email.com',
        is_admin=True,
        permitted=True,
        permitted_from=datetime.now(),
        permitted_to=datetime.now(),
        latitude='23.457',
        longitude='24.567'
    )

    # Initialize and start the Tkinter main window
    root = tk.Tk()
    LoginPage(root, session)
    # root.mainloop()

if __name__ == "__main__":
    main()
