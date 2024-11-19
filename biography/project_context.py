class ProjectContext:
    def __init__(self, description='', milestones=None, goals=None, issues=None):
        self.description = description
        self.milestones = milestones if milestones else []
        self.goals = goals if goals else []
        self.issues = issues if issues else []

    def add_milestone(self, milestone):
        self.milestones.append(milestone)

    def add_goal(self, goal):
        self.goals.append(goal)

    def add_issue(self, issue):
        self.issues.append(issue)

    def get_overview(self):
        """Return a summary of the project context."""
        overview = f"Description: {self.description}\n"
        overview += f"Goals: {', '.join(self.goals)}\n"
        overview += f"Milestones: {', '.join(self.milestones)}\n"
        overview += f"Issues: {', '.join(self.issues)}\n"
        return overview
