
# Installation Steps for Python

## Windows
### Installing Python from Python.org

1. Visit the Python Downloads page.
2. Download the latest version of Python for Windows.
3. Run the installer and check the box that says "Add Python to PATH" during installation.
4. Click "Install Now" to start the installation process.
5. Once the installation is complete, open a command prompt and type: `python --version`

### Installing Python using Anaconda

1. Download and install Anaconda from the Anaconda website.
2. Follow the Anaconda installation wizard.
3. Once installed, open the Anaconda Navigator or the Anaconda Prompt.
4. To check Python version, type: `python --version`

### Creating a Virtual Environment (Windows)

```
python -m venv myenv
```

## macOS
### Installing Python from Python.org
1. Visit the Python Downloads page.
2. Download the latest version of Python for macOS.
3. Run the installer.
4. Open the Terminal and check Python version: `python3 --version`

### Installing Python using Anaconda
1. Download and install Anaconda from the Anaconda website.
2. Follow the Anaconda installation wizard.
3. Once installed, open the Terminal.
4. To check Python version, type: `python3 --version`

### Creating a Virtual Environment (macOS)
```
python3 -m venv myenv
```

## Linux (Ubuntu)
### Installing Python from Python.org
1. Open the terminal.
2. Update package lists: `sudo apt update`
3. Install prerequisites: `sudo apt install python3 python3-pip`
4. Check Python version: `python3 --version`

### Installing Python using Anaconda
1. Download the Anaconda installer for Linux from the Anaconda website.
2. Open the terminal and navigate to the directory containing the downloaded file.
3. Run the installer script: `bash Anaconda3-<version>-Linux-x86_64.sh`
4. Follow the installation prompts.
5. Open a new terminal window.
6. To check Python version, type: `python --version`

### Creating a Virtual Environment (Linux)
```
python3 -m venv myenv
```

## Checking Virtual Environment Activation (All Platforms)
### Activate the virtual environment:
- **Windows**: `myenv\Scripts\activate`
- **macOS/Linux**: `source myenv/bin/activate`

> The terminal prompt should change, indicating that the virtual environment is active.

To deactivate the virtual environment, simply type `deactivate` in the terminal.


# Discuss different IDEs and the features

| Feature                        | VS Code                          | PyCharm                         | Jupyter Notebook               |
|--------------------------------|----------------------------------|----------------------------------|----------------------------------|
| **Code Editing**               | IntelliSense, Snippets           | Smart Code Completion, Refactoring | Code cells, Markdown support     |
| **Debugging**                  | Integrated Debugger              | Powerful Debugger, Visual Debugger | Limited, cell-wise debugging    |
| **Project Management**         | Integrated Git, Extensions       | Project Navigation, VCS Support   | N/A (Primarily for notebooks)   |
| **Language Support**           | Multi-language, Extensible       | Python, Web, Database            | Python, R, Julia, Markdown       |
| **Extensions and Plugins**     | Vast Marketplace                 | Rich Plugin Ecosystem            | Limited, but growing            |
| **Performance**                | Lightweight, Fast                | Resource Intensive               | Lightweight for notebooks       |
| **User Interface**             | Customizable, Modern             | Feature-rich, Traditional        | Web-based, Interactive          |
| **Integrated Terminal**        | Yes                              | Yes                              | No (Terminal available separately) |
| **Code Version Control**       | Git, GitHub, GitLab integration  | Git, GitHub, GitLab integration  | Limited (Not the primary focus) |
| **Cost**                       | Free and Open Source             | Freemium Model                  | Free and Open Source            |
| **Learning Curve**             | Beginner-Friendly                | Moderate to Advanced            | Beginner-Friendly               |


# Installation step for VSCode, Jupyter Notebook, PyCharm

## VS Code Installation Guide

### Windows

1. Download the Visual Studio Code installer from the VS Code website.
2. Run the installer and follow the installation wizard.
3. Open VS Code after installation.
4. Optional: Install Python extension for VS Code from the Extensions marketplace.

### macOS
1. Download the Visual Studio Code installer from the VS Code website.
2. Open the downloaded .dmg file and drag VS Code to the Applications folder.
3. Open VS Code from the Applications folder.
4. Optional: Install Python extension for VS Code from the Extensions marketplace.

### Linux (Ubuntu)
1. Open the terminal.
2. Download and install VS Code: 
```
sudo apt update
sudo apt install code
```
3. Open VS Code: `code`
4. Optional: Install Python extension for VS Code from the Extensions marketplace.

## Jupyter Notebook Installation Guide

### All Operating Systems

1. Install Jupyter using pip: `pip install jupyter`
2. Start Jupyter Notebook: `jupyter notebook`
3. Jupyter Notebook will open in your default web browser.

## PyCharm Installation Guide

### Windows

1. Download the PyCharm installer from the JetBrains website.
2. Run the installer and follow the installation wizard.
3. Open PyCharm after installation.
4. Optional: Configure Python interpreter and create a virtual environment within PyCharm.

### macOS
1. Download the PyCharm installer from the JetBrains website.
2. Open the downloaded .dmg file and drag PyCharm to the Applications folder.
3. Open PyCharm from the Applications folder.
4. Optional: Configure Python interpreter and create a virtual environment within PyCharm.

### Linux (Ubuntu)
1. Download the PyCharm installer from the JetBrains website.
2. Extract the downloaded tar.gz file.
3. Navigate to the extracted directory and run the bin/pycharm.sh script.
4. Follow the PyCharm setup wizard.
5. Optional: Configure Python interpreter and create a virtual environment within PyCharm.

## Checking Installations

1. **VS Code**: Open VS Code and check for the presence of the Python extension in the Extensions sidebar.

2. **Jupyter Notebook**: Open a Jupyter Notebook and ensure that it opens successfully in the web browser.

3. **PyCharm**: Open PyCharm and create a new Python project. Verify that the Python interpreter is configured correctly.