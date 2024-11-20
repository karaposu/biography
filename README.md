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




--
## LLM based operations
### **1. Summarize a File Change**  
- **Why:** A fundamental feature to provide concise explanations of what changed in a file during a commit.  
- **Importance:** Core to understanding individual changes and building other summaries.  

---

### **2. Generate Accurate Commit Messages**  
- **Why:** Aggregates file change summaries to create meaningful commit messages that are consistent and clear.  
- **Importance:** Ensures a well-documented Git history, crucial for collaboration and maintenance.  

---

### **3. Summarize a File**  
- **Why:** Provides high-level overviews of files, useful for onboarding or understanding the purpose and structure of a codebase.  
- **Importance:** Valuable for larger or frequently modified files to help developers quickly grasp their contents.

---

### **4. Summarize a File Change with Context of the Whole Project**  
- **Why:** Adds depth to summaries by considering how the changes align with the project's goals or existing functionality.  
- **Importance:** Critical for avoiding siloed understanding of changes.  

---

### **5. Cluster File Changes into Major Changes and Milestones**  
- **Why:** Groups related changes into higher-level milestones, simplifying navigation and providing a broader view of development progress.  
- **Importance:** Essential for project retrospectives and release planning.  

---

### **6. Generate Release Notes**  
- **Why:** Aggregates changes from commits to create comprehensive release notes for stakeholders.  
- **Importance:** Directly impacts user communication and product documentation.  

---

### **7. Identify and Summarize Refactoring Efforts**  
- **Why:** Highlights improvements in code quality or structure without changing functionality.  
- **Importance:** Promotes clean code practices and tracks technical debt reduction.  

---

### **8. Detect and Summarize Bug Fixes**  
- **Why:** Identifies commits resolving bugs and explains the root cause and resolution.  
- **Importance:** Aids in debugging similar issues and improves transparency in issue resolution.  

---

### **9. Summarize Pull Requests or Merge Requests**  
- **Why:** Provides an overview of multi-commit efforts, including decisions made during reviews.  
- **Importance:** Facilitates better collaboration and historical understanding of significant changes.  

---

### **10. Extract and Summarize Security Vulnerabilities**  
- **Why:** Identifies and summarizes fixes addressing security concerns.  
- **Importance:** Crucial for compliance, audits, and maintaining a secure codebase.  

---

### **Rationale for Ranking**:

- **Core Operations (1–4):** Focus on fundamental insights about file changes and commits, forming the backbone of the tool.  
- **Project-Level Summaries (5–7):** Build on foundational features to provide higher-level insights, enhancing team communication.  
- **Specific Use Cases (8–10):** Address more targeted needs, such as bug fixes, reviews, or security.  

This prioritization ensures you start with features that deliver the most immediate value while laying the groundwork for more specialized functionalities.






# we need file class and in this class we need methods which will help us represent the whole file in different type of details
# like generic summary where each class and method's code is explained in nlp
# pseudo_summary is where each method is explained using pseudo 
# aim summary is  where each method is explained in terms of aim