# Plagiarism Detection

It is relatively simple to detect code copying, where two students have shared the same or similar code. Detecting other forms of plagiarism is much more complicated.

## Detect code copying

There are a variety of code similarity analysis tools. We recommend using [compare50](https://cs50.readthedocs.io/projects/compare50/en/latest/index.html), an open source project that runs locally and is similar in functionality to the more-famous closed-source frequently malfunctioning [moss](https://theory.stanford.edu/~aiken/moss/) system.

To analyze code similarity of any assignment:

1. Assuming Python is already installed, install `compare50` by running the following command on the command line: `pip install -U compare50`. See their documentation for further installation details.
1. Place all student submissions for an assignment into a single parent directory (note that this is how [GitHub Classroom Assistant](https://classroom.github.com/assistant), which we recommend using, already organizes student submissions).
1. Place any given code into a sub-directory named `given-code` within this same parent directory.
1. Open a command line tool (i.e. `Terminal` on Mac or [Git Bash](https://gitforwindows.org/) or [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) on Windows) and navigate into the parent directory.
1. Analyze the results by running `python -m compare50 **/*.py -d given-code`, where `*.py` can be changed to any filename you want to compare across submissions, such as `python -m compare50 **/solution.py -d given-code`
1. `compare50` will generate a `results` directory containing results as HTML web pages. Open the `index.html` page in a web browser to view results.
1. Click on any results to see the details of the analysis. Report any that look highly similar.
