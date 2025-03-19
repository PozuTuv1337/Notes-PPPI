# features.py
# Модуль экспорта в PDF, назначения ярлыков и поиска заметок

def export_to_pdf(note):
    print("Exporting note to PDF...")

def add_tag(note, tag):
    print(f"Tag '{tag}' added to note '{note}'.")

def search_notes(query):
    print(f"Searching for notes with query: '{query}'")

if __name__ == '__main__':
    export_to_pdf("Test Note")
    add_tag("Test Note", "Important")
    search_notes("Test")
