import subprocess
import re
import json




class Biography:
    def __init__(self, commit_hash, date, author_name, author_email, message, change_summary, aim='', mistakes='', project_context='', issue_ids=None):
        self.commit_hash = commit_hash
        self.date = date
        self.author_name = author_name
        self.author_email = author_email
        self.message = message
        self.change_summary = change_summary
        self.mistakes = mistakes
        self.project_context = project_context
        self.aim = aim

        self.issue_ids = issue_ids if issue_ids is not None else []

    def to_dict(self):
        return {
            'commit_hash': self.commit_hash,
            'date': self.date,
            'author_name': self.author_name,
            'author_email': self.author_email,
            'message': self.message,
            'change_summary': self.change_summary,
            'aim': self.aim,
            'mistakes': self.mistakes,
            'project_context': self.project_context,
            'issue_ids': self.issue_ids
        }

    def __repr__(self):
        return (f"Biography(commit_hash='{self.commit_hash}', date='{self.date}', "
                f"author_name='{self.author_name}', message='{self.message}', "
                f"change_summary='{self.change_summary}')")


if __name__ == '__main__':
    git_story = GitStory()
    biographies = git_story.get_commits()
    # Print the biographies or save them to a file
    for bio in biographies:
        print(bio)
    # Optionally, save biographies to a JSON file for persistence
    git_story.save_biographies(biographies)
