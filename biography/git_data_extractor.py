import subprocess
import re
import json


class GitDataExtractor:
    def __init__(self, repo_path='.'):
        self.repo_path = repo_path

    def get_commits(self):
        try:
            # Run git log to get commit hashes, dates, messages, author name, and email
            git_log = subprocess.check_output(
                ['git', '-C', self.repo_path, 'log', '--pretty=format:%H|||%ad|||%an|||%ae|||%s', '--date=iso'],
                universal_newlines=True
            )
            biographies = []
            for line in git_log.strip().split('\n'):
                parts = line.split('|||')
                if len(parts) == 5:
                    commit_hash, date, author_name, author_email, message = parts
                    # Get changed files
                    changed_files = self.get_changed_files(commit_hash)
                    # Process changes
                    change_summary = self.process_changes(commit_hash, changed_files)
                    # Extract issue IDs from the message
                    issue_ids = self.extract_issue_ids(message)
                    # Create a Biography instance
                    bio = Biography(
                        commit_hash=commit_hash.strip(),
                        date=date.strip(),
                        author_name=author_name.strip(),
                        author_email=author_email.strip(),
                        message=message.strip(),
                        change_summary=change_summary,
                        aim='',
                        mistakes='',
                        project_context='',
                        issue_ids=issue_ids
                    )
                    biographies.append(bio)
            return biographies
        except subprocess.CalledProcessError as e:
            print("An error occurred while running git commands:", e)
            return []

    def get_changed_files(self, commit_hash):
        git_show = subprocess.check_output(
            ['git', '-C', self.repo_path, 'show', '--pretty=format:', '--name-only', commit_hash],
            universal_newlines=True
        )
        changed_files = [f for f in git_show.strip().split('\n') if f]
        return changed_files

    def process_changes(self, commit_hash, changed_files):
        # Placeholder for your custom LLM summarizer logic
        change_summaries = []
        for file in changed_files:
            diff = self.get_diff_for_file(commit_hash, file)
            # Replace the following line with your LLM summarizer function
            summary = f"Summary for {file}"
            change_summaries.append(summary)
        return ' '.join(change_summaries)

    def get_diff_for_file(self, commit_hash, file):
        diff_output = subprocess.check_output(
            ['git', '-C', self.repo_path, 'show', f'{commit_hash}', '--', file],
            universal_newlines=True
        )
        return diff_output

    def extract_issue_ids(self, message):
        # Example regex for IDs like PROJ-123 or #123
        issue_ids = re.findall(r'\b[A-Z]+-\d+\b|#\d+', message)
        return issue_ids

    def save_biographies(self, biographies, filename='biographies.json'):
        # Serialize biographies to a JSON file
        with open(filename, 'w') as f:
            json.dump([bio.to_dict() for bio in biographies], f, indent=4)

    def load_biographies(self, filename='biographies.json'):
        # Load biographies from a JSON file
        with open(filename, 'r') as f:
            bio_dicts = json.load(f)
            biographies = [Biography(**bio_dict) for bio_dict in bio_dicts]
            return biographies
