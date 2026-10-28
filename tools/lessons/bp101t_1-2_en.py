"""Lesson 1.2 (English). Run to write content/bp101t/1-2/en.json."""
import json
import os

L = {
    "id": "1-2",
    "course": "bp101t",
    "unit": "Unit I",
    "unitTitle": "Introduction to Python programming",
    "number": "1.2",
    "title": "Installing Python and IDEs",
    "minutes": 12,
    "free": True,
    "audioLanguages": ["en", "hi", "kn"],
    "hook": {
        "title": "Set up your coding workspace",
        "md": "By the end of this lesson, you will know how to **install Python** on a laptop, **choose an IDE** (Jupyter Notebook, PyCharm or VS Code), and explain **why IDEs are better than plain text editors**, a favourite exam question.\n\nNo laptop? No problem. Everything in this course also works in **Champ Lab**, right on your phone.",
    },
    "learn": [
        "How to **install Python** and check that it works",
        "What an **IDE** is, and the three popular ones: **Jupyter Notebook, PyCharm and VS Code**",
        "The **advantages of IDEs over text editors**",
    ],
    "explanation": [
        {
            "heading": "What does \"installing Python\" mean?",
            "md": "In Lesson 1.1 you learned that the **interpreter** reads and runs your code. Installing Python simply means putting this interpreter on your computer.\n\n**Steps (Windows):**\n1. Go to **python.org → Downloads** and download the latest Python 3 installer.\n2. Open the installer and **tick \"Add python.exe to PATH\"** at the bottom of the first screen. This one checkbox saves a lot of trouble.\n3. Click **Install Now** and wait for it to finish.\n4. Open **Command Prompt** and type `python --version`. If you see something like `Python 3.12.4`, Python is ready.\n\nOn a Mac, use the installer from python.org and check with `python3 --version` in Terminal.",
            "callout": {"type": "tip", "title": "Tip", "md": "Always install **Python 3**. Old tutorials use Python 2, which is no longer supported."},
        },
        {
            "heading": "Text editor vs IDE",
            "md": "You can write Python in any **text editor**, like Notepad. But a text editor only stores plain text. It cannot run your code, colour it or point out mistakes.\n\nAn **IDE** gives you everything in one place: an editor, a way to run code, error hints and tools to find bugs.\n\nThink of it this way: writing a prescription on **plain paper** works, but **pharmacy software** checks spellings, warns about interactions and prints the label for you. A text editor is the paper; an IDE is the software.",
            "callout": {"type": "definition", "title": "IDE", "md": "**Integrated Development Environment**: one application that combines a code editor, a way to run programs, error checking and debugging tools."},
        },
        {
            "heading": "Three popular IDEs",
            "md": "| IDE | Best for | Good to know |\n|---|---|---|\n| **Jupyter Notebook** | Data analysis, graphs, step-by-step experiments | Code runs in small **cells**, and each cell's output or graph appears right below it. Comes with **Anaconda**, and runs free online in **Google Colab**. |\n| **PyCharm** | Larger projects | A full-featured Python IDE by **JetBrains**. The **Community** edition is free. |\n| **VS Code** | All-round coding | A free, lightweight editor by **Microsoft**. Add the **Python extension** and it becomes a powerful Python IDE. |\n\nFor this course, **Jupyter Notebook** (or Google Colab) is the most useful, because pharmacy work is mostly about data and graphs.",
            "callout": {"type": "definition", "title": "Anaconda", "md": "A free bundle that installs Python together with Jupyter Notebook and popular science libraries in one go."},
        },
        {
            "heading": "Advantages of IDEs over text editors",
            "md": "| Feature | Text editor | IDE |\n|---|---|---|\n| **Syntax highlighting** (code in colours) | ❌ | ✅ |\n| **Auto-completion** (suggests words as you type) | ❌ | ✅ |\n| **Error hints** while you type | ❌ | ✅ |\n| **Run with one click** and see output | ❌ | ✅ |\n| **Debugger** (run line by line to find bugs) | ❌ | ✅ |\n| **Project and file management** | ❌ | ✅ |\n| **Install libraries** and extensions easily | ❌ | ✅ |\n\nIn short, an IDE helps you **write faster, make fewer mistakes and find bugs sooner**.",
        },
        {
            "heading": "No laptop? Use the browser",
            "md": "You don't need to install anything to learn this course:\n\n- **Champ Lab** runs Python inside your browser, even on a phone.\n- **Google Colab** gives you a free Jupyter Notebook online, using your Google account.\n\nInstall Python on a laptop when you can, because your practical exams may use one.",
        },
    ],
    "walkthrough": {
        "intro": "After installing Python and an IDE, programmers run a tiny program to check that everything works. Here is ours.",
        "filename": "setup_check.py",
        "code": "# Setup check\nprint(\"Python is installed!\")\nprint(\"Test sum:\", 250 + 250)\nprint(\"All set for BP101T\")",
        "output": "Python is installed!\nTest sum: 500\nAll set for BP101T",
        "steps": [
            {"line": None, "say": "You have installed Python and opened an IDE. Let's run a quick setup check.", "output": None, "audio": "step-01.mp3"},
            {"line": 1, "say": "The first line is a comment, a note for us. In an IDE, comments appear in a different colour, so they are easy to spot.", "output": None, "audio": "step-02.mp3"},
            {"line": 2, "say": "This print confirms that Python is working. In an IDE, you press the Run button, and the output appears in a panel below your code.", "output": "Python is installed!", "audio": "step-03.mp3"},
            {"line": 3, "say": "Here, Python adds two hundred and fifty and two hundred and fifty. If you see five hundred, calculations are working too.", "output": "Test sum: 500", "audio": "step-04.mp3"},
            {"line": 4, "say": "The last line tells us we are ready for the course.", "output": "All set for BP101T", "audio": "step-05.mp3"},
            {"line": None, "say": "This same code runs the same way in Jupyter Notebook, PyCharm, VS Code, or Champ Lab. Only the buttons look different.", "output": None, "audio": "step-06.mp3"},
        ],
        "keyTerms": [
            {"term": "IDE", "meaning": "Integrated Development Environment: write, run and fix code in one place."},
            {"term": "Run button", "meaning": "Runs your program and shows the output."},
            {"term": "Cell", "meaning": "A small block of code in Jupyter that runs on its own."},
            {"term": "PATH", "meaning": "The list of places Windows looks in to find programs like python."},
        ],
    },
    "errors": {
        "intro": "Most setup problems are small and easy to fix once you recognise the message.",
        "examples": [
            {
                "title": "Typing a terminal command inside Python",
                "code": "python --version",
                "output": "NameError: name 'python' is not defined",
                "errorLine": 1,
                "md": "`python --version` is a **terminal command**. It works in Command Prompt or Terminal, but here it was typed inside Python itself (the `>>>` prompt or a code cell). Python reads `python` as an unknown name. Type `exit()` to leave the Python prompt, then run the command in the terminal.",
            },
            {
                "title": "A library that isn't installed (or is misspelt)",
                "code": "import numpyy",
                "output": "ModuleNotFoundError: No module named 'numpyy'",
                "errorLine": 1,
                "md": "Python looked for a library called `numpyy` and couldn't find it. Here the name is simply misspelt (it should be `numpy`). If the spelling is right, the library isn't installed yet. You'll learn to install libraries with **pip** in Lesson 1.7.",
                "callout": {"type": "definition", "title": "Library", "md": "Ready-made code that adds new abilities to Python, such as NumPy for numbers or Matplotlib for graphs."},
            },
        ],
    },
    "mistakes": [
        {"mistake": "Not ticking **Add python.exe to PATH** during installation", "see": "'python' is not recognized as an internal or external command, operable program or batch file.", "fix": "Run the installer again, choose **Modify** (or reinstall) and tick **Add python.exe to PATH**. You can also try the `py` command instead of `python`."},
        {"mistake": "Copying code from an old Python 2 tutorial", "see": "SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?", "fix": "In Python 3, `print` always needs brackets: `print(\"Hello\")`."},
        {"mistake": "Saving a file from Notepad as `program.py.txt`", "see": "The file opens in Notepad instead of running as Python", "fix": "Choose **Save as type: All Files** and name it `program.py`, or simply use an IDE."},
        {"mistake": "Typing `python --version` inside Python (`>>>`)", "see": "NameError: name 'python' is not defined", "fix": "Type `exit()` first, then run the command in Command Prompt or Terminal."},
    ],
    "tasks": [
        {
            "id": "t1",
            "title": "Your first IDE message",
            "md": "Write a program that prints exactly:",
            "expectedOutput": "My IDE is ready!",
            "starterCode": "# Write your code below\n",
            "hints": ["Use print() with the message inside quotes."],
            "solution": "print(\"My IDE is ready!\")",
            "check": {"type": "exactOutput", "mustContain": []},
        },
        {
            "id": "t2",
            "title": "Setup check report",
            "md": "Write a program that prints this report. Let Python **calculate** the test sum (250 + 250); don't type 500 yourself.",
            "expectedOutput": "=== SETUP CHECK ===\nPython  : installed\nIDE     : VS Code\nTest sum: 500",
            "starterCode": "# Setup check report\n",
            "hints": ["Use one print() for each line.", "For the last line, try print(\"Test sum:\", 250 + 250)."],
            "solution": "# Setup check report\nprint(\"=== SETUP CHECK ===\")\nprint(\"Python  : installed\")\nprint(\"IDE     : VS Code\")\nprint(\"Test sum:\", 250 + 250)",
            "check": {"type": "exactOutput", "mustContain": ["250 + 250"]},
        },
        {
            "id": "t3",
            "title": "Fix the old tutorial code",
            "md": "This line was copied from an old Python 2 tutorial. Fix it so it prints `Python is ready`.",
            "expectedOutput": "Python is ready",
            "starterCode": "print \"Python is ready\"",
            "hints": ["In Python 3, print needs brackets."],
            "solution": "print(\"Python is ready\")",
            "solutionNote": "Python 3 needs brackets around what you print.",
            "check": {"type": "exactOutput", "mustContain": []},
        },
    ],
    "quiz": [
        {"q": "What does IDE stand for?", "options": ["Integrated Development Environment", "Internal Data Editor", "Integrated Drug Encyclopedia", "Interactive Design Engine"], "answer": 0, "why": "IDE stands for Integrated Development Environment: one place to write, run and fix code."},
        {"q": "Which tool runs code in small cells and shows the output or graph right below each cell?", "options": ["Notepad", "Jupyter Notebook", "Command Prompt", "Microsoft Word"], "answer": 1, "why": "Jupyter Notebook runs code cell by cell and shows results directly below, which is great for data and graphs."},
        {"q": "While installing Python on Windows, which option prevents the error \"'python' is not recognized\"?", "options": ["Install for all users", "Add python.exe to PATH", "Disable path length limit", "Download debug binaries"], "answer": 1, "why": "Adding python.exe to PATH lets Windows find the python command from any folder."},
        {"q": "Which of these is NOT an advantage of an IDE over a text editor?", "options": ["Syntax highlighting", "Auto-completion", "Debugging tools", "Running programs without Python installed"], "answer": 3, "why": "An IDE still needs Python installed. It makes writing, running and fixing code easier, but it doesn't replace the interpreter."},
        {"q": "Which IDE is a free editor made by Microsoft?", "options": ["PyCharm", "Jupyter Notebook", "VS Code", "Anaconda"], "answer": 2, "why": "VS Code (Visual Studio Code) is a free editor by Microsoft. With the Python extension it works as a full Python IDE."},
    ],
    "exam": {
        "note": "Important questions for practice. Actual university questions may differ.",
        "short": [
            {"q": "Define IDE. Give two examples.", "marks": 2, "md": "An **IDE (Integrated Development Environment)** is a software application that combines a code editor, tools to run programs, error checking and a debugger in one place. Examples: **PyCharm**, **VS Code**, **Jupyter Notebook**."},
            {"q": "What is Jupyter Notebook?", "marks": 2, "md": "**Jupyter Notebook** is an interactive, web-based environment where Python code is written and run in separate **cells**. The output of each cell, including tables and graphs, appears directly below it. It is widely used for data analysis and comes with the Anaconda distribution."},
        ],
        "long": [
            {"q": "Explain the steps to install Python and an IDE. List the advantages of IDEs over text editors.", "marks": 5, "md": "**Installing Python (Windows):**\n1. Download the latest Python 3 installer from **python.org**.\n2. Run the installer and select **\"Add python.exe to PATH\"**.\n3. Click **Install Now** and complete the installation.\n4. Verify by typing `python --version` in Command Prompt.\n\n**Installing an IDE:**\n- **Jupyter Notebook:** install the **Anaconda** distribution (includes Python and Jupyter), then launch Jupyter Notebook; or use **Google Colab** online.\n- **PyCharm:** download the free **Community** edition from JetBrains and select the installed Python interpreter.\n- **VS Code:** download from Microsoft, then install the **Python extension** and select the interpreter.\n\n**Advantages of IDEs over text editors:**\n1. **Syntax highlighting:** code is coloured, making it easier to read.\n2. **Auto-completion:** suggests keywords and names while typing.\n3. **Error detection:** highlights mistakes before running.\n4. **Integrated execution:** run programs with one click and view output in the same window.\n5. **Debugging tools:** breakpoints and step-by-step execution to find bugs.\n6. **Project management:** organise multiple files and folders.\n7. **Library and extension management:** install packages and tools easily."},
        ],
    },
    "mindmap": {
        "label": "Lesson 1.2 · Setup",
        "children": [
            {"label": "Install Python", "children": [{"label": "python.org"}, {"label": "Tick Add to PATH"}, {"label": "Check: python --version"}]},
            {"label": "Text editor vs IDE", "children": [{"label": "Editor: plain text only"}, {"label": "IDE: all tools in one place"}]},
            {"label": "Popular IDEs", "children": [{"label": "Jupyter Notebook", "children": [{"label": "Cells + graphs"}, {"label": "Anaconda / Colab"}]}, {"label": "PyCharm", "children": [{"label": "Full-featured, JetBrains"}]}, {"label": "VS Code", "children": [{"label": "Free, Microsoft"}, {"label": "Python extension"}]}]},
            {"label": "IDE advantages", "children": [{"label": "Syntax highlighting"}, {"label": "Auto-completion"}, {"label": "Error hints"}, {"label": "One-click run"}, {"label": "Debugger"}]},
            {"label": "No laptop?", "children": [{"label": "Champ Lab"}, {"label": "Google Colab"}]},
            {"label": "Setup errors", "children": [{"label": "python not recognized: PATH"}, {"label": "ModuleNotFoundError: missing library"}]},
        ],
    },
    "summary": [
        "**Installing Python** means putting the interpreter on your computer; on Windows, tick **Add python.exe to PATH**.",
        "Check your installation with **`python --version`** in Command Prompt or Terminal.",
        "An **IDE** (Integrated Development Environment) lets you write, run and fix code in one place.",
        "Popular IDEs: **Jupyter Notebook** (cells and graphs), **PyCharm** (full-featured) and **VS Code** (free, by Microsoft).",
        "IDEs beat text editors with **syntax highlighting, auto-completion, error hints, one-click run and debugging**.",
    ],
    "video": {
        "videoUrl": None,
        "searchTerms": ["how to install python on windows add to path", "jupyter notebook tutorial for beginners"],
    },
    "animations": [
        {
            "id": "ide",
            "title": "Text editor vs IDE",
            "canvas": {"desktop": {"w": 800, "h": 460}, "mobile": {"w": 360, "h": 600}},
            "actors": [
                {"id": "editor", "type": "card", "title": "Text editor", "icon": "📝", "color": "amber", "mono": True,
                 "lines": ["print(\"Hello from my IDE!\")", "(no colours, no hints, no Run)"],
                 "desktop": {"x": 40, "y": 40, "w": 320, "h": 240}, "mobile": {"x": 16, "y": 16, "w": 328, "h": 130}},
                {"id": "ide", "type": "card", "title": "IDE", "icon": "🧰", "color": "indigo",
                 "lines": ["Syntax colours", "Auto-complete", "Error hints", "One-click Run", "Debugger"],
                 "desktop": {"x": 440, "y": 40, "w": 320, "h": 240}, "mobile": {"x": 16, "y": 166, "w": 328, "h": 236}},
                {"id": "out", "type": "terminal", "title": "Output",
                 "desktop": {"x": 40, "y": 310, "w": 720, "h": 120}, "mobile": {"x": 16, "y": 422, "w": 328, "h": 130}},
            ],
            "steps": [
                {"say": "A text editor, like Notepad, is just a blank page. It stores your code as plain text.", "audio": "anim-ide-01.mp3",
                 "actions": [{"do": "show", "target": "editor"}]},
                {"say": "An IDE is an Integrated Development Environment. It is a complete workspace for writing code.", "audio": "anim-ide-02.mp3",
                 "actions": [{"do": "show", "target": "ide"}]},
                {"say": "It colours your code, suggests words as you type, warns you about mistakes, and helps you find bugs.", "audio": "anim-ide-03.mp3",
                 "actions": [{"do": "scanLines", "target": "ide", "intervalMs": 900}]},
                {"say": "And with one click, it runs your program and shows the output, right there.", "audio": "anim-ide-04.mp3",
                 "actions": [{"do": "highlightLine", "target": "ide", "line": 3}, {"do": "show", "target": "out"}, {"do": "appendOutput", "target": "out", "text": "Hello from my IDE!"}]},
                {"say": "That's why programmers prefer IDEs. They save time and catch mistakes early.", "audio": "anim-ide-05.mp3",
                 "actions": [{"do": "connect", "id": "upgrade", "from": "editor", "to": "ide", "label": "Upgrade", "color": "emerald"}, {"do": "pulse", "target": "ide"}]},
            ],
        }
    ],
}

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(__file__), "..", "..")
    out = os.path.join(root, "content", "bp101t", "1-2", "en.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(L, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", out)
