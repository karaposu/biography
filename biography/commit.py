# Commit class
class Commit:
    def __init__(self, commit_hash, date, author_name, author_email, message):
        self.commit_hash = commit_hash
        self.date = date
        self.author_name = author_name
        self.author_email = author_email
        self.message = message
        self.file_changes = []  # List of FileChange objects
        self.summary = ''
        self.mistakes = ''
        self.project_context = ''


    def add_file_change(self, file_change):
        self.file_changes.append(file_change)
        file_change.commit = self  # Set back-reference if needed
