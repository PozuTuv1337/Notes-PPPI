"""
features.py
Модуль экспорта в PDF, назначения ярлыков и поиска заметок.
"""

def export_to_pdf(note):
    """
    Экспортирует заметку в формат PDF.

    Args:
        note (str): Текст заметки для экспорта.

    Returns:
        None
    """
    print("Exporting note to PDF...")


def add_tag(note, tag):
    """
    Добавляет тег к заметке.

    Args:
        note (str): Текст заметки.
        tag (str): Тег, который необходимо добавить.

    Returns:
        None
    """
    print(f"Tag '{tag}' added to note '{note}'.")


def search_notes(query):
    """
    Выполняет поиск заметок по заданному запросу.

    Args:
        query (str): Строка запроса для поиска.

    Returns:
        None
    """
    print(f"Searching for notes with query: '{query}'")


if __name__ == '__main__':
    export_to_pdf("Test Note")
    add_tag("Test Note", "Important")
    search_notes("Test")
