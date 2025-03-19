# core_notes.py
# Модуль управления пользователями и создания/редактирования заметок

def register_user(username, password):
    print(f"User {username} registered successfully.")

def create_note(note_title, note_content):
    print(f"Note '{note_title}' created with content: {note_content}")

def group_notes_into_book(book_title, notes):
    print(f"Book '{book_title}' created with notes: {notes}")

if __name__ == '__main__':
    register_user("testuser", "password123")
    create_note("Test Note", "This is a sample note.")
    group_notes_into_book("My Book", ["Test Note"])
