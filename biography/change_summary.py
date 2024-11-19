class ChangeSummary:
    def __init__(self, summary_text='', related_commits=None, context=''):
        self.summary_text = summary_text
        self.related_commits = related_commits if related_commits else []
        self.context = context

    def add_related_commit(self, commit):
        self.related_commits.append(commit)

    def generate_summary(self):
        """Generate a summary based on related commits."""
        # Implement summary generation logic here
        pass
