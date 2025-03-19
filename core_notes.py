# core_notes.py
# Модуль управления пользователями и создания/редактирования заметок
 
#Удалил основные функции для создания необратимых изменений
 
if __name__ == '__main__':
    register_user("testuser", "password123")
    create_note("Test Note", "This is a sample note.")
    group_notes_into_book("My Book", ["Test Note"])
