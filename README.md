# sqa-project
COMP-5710 Project by Kevin Kuoch and Alex

In this project, we designed a pipeline that from an input CFR Markdown file parses requirements, designs an expected structure, and produces a number of corresponding test cases. Those saved files are automatically verified and validated using GitHub Actions.

Using the provided script "generate_requirements.py", we produced twenty-six requirements saved to "requirements.json". The script was modified to also generate the expected structure, placed in "expected_structure.json". We selected the first ten atomic rules as the expected structure; the script "generate_test_cases.py" was used to create ten test cases that corresponded to them. The output test cases are found in "test_cases.json".

The verification and validation scripts from Assignment 6 were hooked to the GitHub repository's workflow actions to automatically execute them upon a git push or pull command. They ensured that our output files were correctly satisfied and built. The relevant logs can be seen under the Actions section of this repository.

To complete/fix CI (forensick integration) required examining CI failed build logs.
<img width="1459" height="986" alt="Screenshot 2026-04-24 204422" src="https://github.com/user-attachments/assets/40ead537-fa68-4341-8836-a138efb2476f" />
Original error was caused by verification script not following the correct requirement_id format for the CFR, so it was modified to respect the format.
<img width="802" height="1040" alt="Screenshot 2026-04-24 204530" src="https://github.com/user-attachments/assets/898e6aef-f8d8-4ed8-a254-0e8798b13b96" />
After CI runs again, one last issue in the script was caused by long numbers in some requirement_id, which was also fixed in the validation script.
<img width="802" height="1040" alt="Screenshot 2026-04-24 204530" src="https://github.com/user-attachments/assets/eefe7bb6-eb71-4c43-9c69-07859805537c" />
Finally, after assigning our test cases, the requirements.json was not updated and caused CI to fail again, this was fixed by updating the json file to the correct requirements.
<img width="813" height="839" alt="Screenshot 2026-04-24 204553" src="https://github.com/user-attachments/assets/406ce116-8c5b-4c8e-99a5-4512344c2267" />
Afterward, CI passes successfully.

Individually, each team member generated LLM test cases using Mistral and quantized Mistral and compared their coverage, correctness, and completeness. The code is in the Jupyter Notebook "SQA2026.ipynb", but the individual reports are submitted via Canvas.
