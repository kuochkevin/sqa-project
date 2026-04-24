# sqa-project
COMP-5710 Project by Kevin Kuoch and Alex

In this project, we designed a pipeline that from an input CFR Markdown file parses requirements, designs an expected structure, and produces a number of corresponding test cases. Those saved files are automatically verified and validated using GitHub Actions.

Using the provided script "generate_requirements.py", we produced twenty-six requirements saved to "requirements.json". The script was modified to also generate the expected structure, placed in "expected_structure.json". We selected the first ten atomic rules as the expected structure; the script "generate_test_cases.py" was used to create ten test cases that corresponded to them. The output test cases are found in "test_cases.json".

The verification and validation scripts from Assignment 6 were hooked to the GitHub repository's workflow actions to automatically execute them upon a git push or pull command. They ensured that our output files were correctly satisfied and built. The relevant logs can be seen under the Actions section of this repository.

forensick integration here

Individually, each team member generated LLM test cases using Mistral and quantized Mistral and compared their coverage, correctness, and completeness. The code is in the Jupyter Notebook "SQA2026.ipynb", but the individual reports are submitted via Canvas.
