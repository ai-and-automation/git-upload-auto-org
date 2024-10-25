
# GitHub Repository Automation Script

This Python script automates the process of creating GitHub repositories for multiple local projects and pushing their content to the corresponding repositories in a specified GitHub organization.

## Features
- **Repository Creation**: Automatically creates private repositories in a GitHub organization for each project folder.
- **Git Operations**: Initializes a Git repository for each project, commits all files, and pushes the content to the newly created GitHub repository.
- **.gitignore Management**: Automatically adds a `.gitignore` file to each project if one does not exist, using a specified template.

## Prerequisites
Before running the script, ensure you have the following:
- Python 3.x installed.
- The required Python packages installed. You can install them using:
  ```bash
  pip install gitpython python-dotenv requests
  ```
- A `.env` file in the root of your project to store environment variables (see below for structure).

## Environment Variables
Create a `.env` file in the root directory of your script with the following variables:

```plaintext
PROJECTS_DIRECTORY=path/to/your/projects
GITIGNORE_TEMPLATE_PATH=path/to/your/gitignore/template
GITHUB_ORG=your-github-organization
GITHUB_TOKEN=your-personal-access-token
GITHUB_USERNAME=your-github-username
GITHUB_API_URL=https://api.github.com
```

### Explanation:
- **`PROJECTS_DIRECTORY`**: Path to the directory containing all project folders.
- **`GITIGNORE_TEMPLATE_PATH`**: Path to a `.gitignore` template that will be added to each project.
- **`GITHUB_ORG`**: Name of your GitHub organization where repositories will be created.
- **`GITHUB_TOKEN`**: Your GitHub personal access token (with repository creation permissions).
- **`GITHUB_USERNAME`**: Your GitHub username.

## How to Run the Script
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/yourusername/repository.git
   cd repository
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create and populate your `.env` file (as mentioned above).
4. Run the script:
   ```bash
   python script.py
   ```
   The script will loop through each project folder in the `PROJECTS_DIRECTORY`, create a corresponding private repository on GitHub, and upload the project files.

## Example Output
```plaintext
Added .gitignore to project1
Repository project1 created successfully in organization my-org.
Successfully uploaded project1 to https://github.com/my-org/project1.git
```

## Requirements

The main packages used in this project are:

- **GitPython**: For Git operations like initializing repositories, committing files, and pushing to remote repositories.
- **python-dotenv**: To load environment variables from a `.env` file.
- **requests**: For making HTTP requests to the GitHub API (for creating repositories).

These packages, along with their dependencies, are listed in the `requirements.txt` file.

## Troubleshooting
- **Repository Creation Failure**: If a repository fails to be created, the script will log the error returned by GitHub.
- **Failed Upload**: The script catches errors during repository initialization and pushing, providing the error details.

## Acknowledgements
This project was developed with the assistance of [ChatGPT](https://chatgpt.com/).

## License
This project is licensed under the MIT License.
