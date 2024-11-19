
import subprocess
import re

def get_git_commits():
    try:
        # Run git log to get commit hashes, dates, messages, author name, and email
        git_log = subprocess.check_output(
            ['git', 'log', '--pretty=format:%H|||%ad|||%an|||%ae|||%s', '--date=iso'],
            universal_newlines=True
        )
        commits = []
        for line in git_log.strip().split('\n'):
            parts = line.split('|||')
            if len(parts) == 5:
                commit_hash, date, author_name, author_email, message = parts
                # Get changed files
                changed_files = get_changed_files(commit_hash)
                # Process changes
                # change_summary = process_changes(commit_hash, changed_files)
                change_summary= "bla bla"
                # Extract issue IDs from the message
                issue_ids = extract_issue_ids(message)
                # Construct commit dictionary
                commit_dict = {
                    'commit_hash': commit_hash.strip(),
                    'date': date.strip(),
                    'author_name': author_name.strip(),
                    'author_email': author_email.strip(),
                    'message': message.strip(),
                    'change_summary': change_summary,
                    'aim': '',
                    'mistakes': '',
                    'project_context': '',
                    'issue_ids': issue_ids,
                    # Additional fields can be added here
                }
                commits.append(commit_dict)
        return commits
    except subprocess.CalledProcessError as e:
        print("An error occurred while running git commands:", e)
        return []

def get_changed_files(commit_hash):
    git_show = subprocess.check_output(
        ['git', 'show', '--pretty=format:', '--name-only', commit_hash],
        universal_newlines=True
    )
    changed_files = [f for f in git_show.strip().split('\n') if f]
    return changed_files

def process_changes(commit_hash, changed_files):
    # Placeholder for your custom LLM summarizer logic
    change_summaries = []
    for file in changed_files:
        diff = get_diff_for_file(commit_hash, file)
        # Replace the following line with your LLM summarizer function
        summary = f"Summary for {file}"
        change_summaries.append(summary)
    return ' '.join(change_summaries)

def get_diff_for_file(commit_hash, file):
    diff_output = subprocess.check_output(
        ['git', 'show', f'{commit_hash}', '--', file],
        universal_newlines=True
    )
    return diff_output

def extract_issue_ids(message):
    # Example regex for IDs like PROJ-123 or #123
    issue_ids = re.findall(r'\b[A-Z]+-\d+\b|#\d+', message)
    return issue_ids

if __name__ == '__main__':
    commits = get_git_commits()
    for commit in commits:
        print(commit)

