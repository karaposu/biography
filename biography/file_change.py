import subprocess

class FileChange:
    def __init__(self, file_path, commit_hash, repo_path='.', file=None):
        self.file_path = file_path
        self.commit_hash = commit_hash
        self.repo_path = repo_path
        self.file = file  # Reference to the parent File object
        self.diff = self.get_diff()
        self.summary = ''
        self.commit = None  # Reference to the parent Commit object
        self.mistakes = ''
        self.previous_version = self.get_file_version(self.commit_hash + '^')
        self.current_version = self.get_file_version(self.commit_hash)

    def get_diff(self):
        """Retrieve the diff of the file for the given commit."""
        try:
            diff_output = subprocess.check_output(
                ['git', '-C', self.repo_path, 'diff', self.commit_hash + '^', self.commit_hash, '--', self.file_path],
                universal_newlines=True
            )
            return diff_output
        except subprocess.CalledProcessError as e:
            print(f"Error getting diff for {self.file_path} at {self.commit_hash}: {e}")
            return ''

    def get_file_version(self, ref):
        """Retrieve the file content at a specific reference (commit hash or branch)."""
        try:
            file_content = subprocess.check_output(
                ['git', '-C', self.repo_path, 'show', f'{ref}:{self.file_path}'],
                universal_newlines=True
            )
            return file_content
        except subprocess.CalledProcessError as e:
            print(f"Error getting file version for {self.file_path} at {ref}: {e}")
            return ''
