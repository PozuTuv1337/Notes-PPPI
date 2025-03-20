"""
core_notes.py
Модуль управления пользователями и создания/редактирования заметок.
"""

def register_user(username, password):
    """
    Регистрирует нового пользователя.

    Args:
        username (str): Имя пользователя.
        password (str): Пароль пользователя.

    Returns:
        None
    """
    print(f"User {username} registered successfully.")


def create_note(note_title, note_content):
    """
    Создает новую заметку.

    Args:
        note_title (str): Заголовок заметки.
        note_content (str): Содержимое заметки.

    Returns:
        None
    """
    print(f"Note '{note_title}' created with content: {note_content}")


def group_notes_into_book(book_title, notes):
    """
    Объединяет заметки в книгу.

    Args:
        book_title (str): Название книги.
        notes (list): Список заметок.

    Returns:
        None
    """
    print(f"Book '{book_title}' created with notes: {notes}")


if __name__ == '__main__':
    register_user("testuser", "password123")
    create_note("Test Note", "This is a sample note.")
    group_notes_into_book("My Book", ["Test Note"])
