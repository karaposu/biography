
import subprocess

class File:
    def __init__(self, file_path, repo_path='.'):
        self.file_path = file_path
        self.repo_path = repo_path
        self.changes = []  # List of FileChange objects
        self.current_content = self.get_current_content()
        self.generic_summary_text = ''
        self.pseudo_summary_text = ''
        self.aim_summary_text = ''

    def add_change(self, file_change):
        self.changes.append(file_change)

    def get_current_content(self):
        """Retrieve the current content of the file from the repository."""
        try:
            content = subprocess.check_output(
                ['git', '-C', self.repo_path, 'show', f'HEAD:{self.file_path}'],
                universal_newlines=True
            )
            return content
        except subprocess.CalledProcessError as e:
            print(f"Error getting current content for {self.file_path}: {e}")
            return ''

    def get_change_history(self):
        return self.changes

    def analyze_file(self):
        """Perform file-level analysis."""
        # Implement analysis logic here
        pass

    def get_total_changes(self):
        return len(self.changes)

    def get_authors(self):
        authors = set()
        for change in self.changes:
            authors.add(change.commit.author_name)
        return authors

    def generate_generic_summary(self, llm_processor):
        """Generate a natural language summary of the file."""
        prompt = f"Provide a detailed summary of the following code:\n{self.current_content}"
        self.generic_summary_text = llm_processor.generate_summary(prompt)
        return self.generic_summary_text

    def generate_pseudo_summary(self, llm_processor):
        """Generate a pseudocode explanation of each method in the file."""
        prompt = f"Convert the following code into pseudocode, explaining each method:\n{self.current_content}"
        self.pseudo_summary_text = llm_processor.generate_summary(prompt)
        return self.pseudo_summary_text

    def generate_aim_summary(self, llm_processor):
        """Explain each method in terms of its aim or purpose."""
        prompt = f"Explain the purpose of each class and method in the following code:\n{self.current_content}"
        self.aim_summary_text = llm_processor.generate_summary(prompt)
        return self.aim_summary_text




# Relationship Between File and FileChange
# File Class: Represents a file in the repository over its entire history.
#
# Maintains a list of all changes (FileChange instances) that have occurred to the file.
# Holds the current content of the file.
# Provides methods for file-level analysis.
# FileChange Class: Represents a specific change made to a file in a particular commit.
#
# Contains details about the change, such as the diff, summary, mistakes, and versions before and after the change.
# Is associated with a specific Commit and File.
# Compatibility comes from the fact that FileChange instances are linked to both Commit and File instances:
#
# Each FileChange knows which File it belongs to (through the file_path attribute).
# The File maintains a collection of FileChange instances that represent its change history.