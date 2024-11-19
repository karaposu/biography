# Biography

Biography is a Python tool designed for following purposes
       - Extract and convert `git diff` results into meaningful project evolution summaries (with LLMs) for whole codebase
       - Keep track of early and late version of each file to analyze  "mistakes" while storing  "commit_goal"
       - Facilitates deeper insights into the development process by capturing not just what changed, but also the intent, mistakes, and context behind each commit.
       - compile and then export project evolution  into visualizable json format

and it has these extra features 
       - Ability to regenerate commit messages from beginnging to until the end of project 
     


## Features

- **Extract Commit Information**: Retrieves commit date, message, and changes per file.
- **Custom Processing**: Integrates with custom functions (e.g., LLM summarizers) to process commit diffs.
- **Structured Output**: Generates dictionaries with fields like `date`, `message`, `change_summary`, `aim`, `mistakes`, and `project_context`.
- **Extensible**: Easily modify or extend to include additional commit metadata.
- **No Branch Complexity**: Assumes all commits are merged into the main branch, simplifying the commit history.



## Installation

   ```
   pip install biography
   ```

## Usage

### Basic Usage

Run the script in the root directory of the git repository you want to analyze:

```bash
python make_biography.py
```

This will generate a timelime.yaml file containing the extracted commit data with the following structure:

project_description
major_change_1 (major changes contains multiple commit changes summarized together. )
     "date": "2023-10-01 12:34:56 +0000",
    "message": "Initial commit",
    "change_summary": "Changes in README.md",
    "aim": "",
    "mistakes": "",
    "project_context": ""
major_change_2
major_change_3

(i am not sure how this part should be structured)
```

```

*Biography helps you narrate the evolution of your codebase by enriching commit history with meaningful summaries and insights.*


Strengths:

Enhanced Commit Understanding: By extracting and converting git diff results into meaningful summaries using Large Language Models (LLMs), the tool goes beyond traditional version control logs. It captures the intent, mistakes, and context behind each commit, which is invaluable for understanding the development journey.

Structured Data Output: Generating outputs in visualizable JSON or YAML formats makes it easier to integrate with other tools or create custom visualizations. This can help teams to visualize the project's evolution over time effectively.

Regeneration of Commit Messages: The ability to regenerate commit messages can standardize the commit history and make it more informative, which is beneficial for both current team members and future contributors.

Error and Goal Tracking: Keeping track of early and late versions of each file to analyze mistakes while storing commit_goal can help in identifying common pitfalls and improving coding practices.

Potential Applications:

Project Retrospectives: Teams can use the insights provided to conduct more meaningful retrospectives, focusing on what went well and what could be improved.

Onboarding New Members: New team members can get up to speed faster by reviewing the summarized project evolution, understanding the rationale behind decisions.

Educational Purposes: Can be used as a teaching tool to show the development process of a project, highlighting challenges and how they were overcome.

Future features planned:

Clarify Output Structure: The description of the output structure is a bit unclear. Providing a concrete example of the generated timelime.yaml (perhaps with a small sample project) would help users understand what to expect.

Branch Handling: Since the tool assumes all commits are merged into the main branch, it might miss out on the complexities introduced by feature branches and parallel development. Supporting multiple branches could provide a more comprehensive view.

Integration with Visualization Tools: Offering built-in support or guidance for visualizing the JSON/YAML data can enhance the user experience, making it easier to derive insights without additional effort.

Performance Optimization: For large repositories with extensive histories, performance might become an issue. Providing options to limit the scope (e.g., date ranges, specific files) or optimizing the data processing could be beneficial.

Expand Documentation: Including more detailed installation steps, usage examples, and potential pitfalls can make it more accessible to a wider audience.