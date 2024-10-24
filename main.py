import os
import git
import requests
from dotenv import load_dotenv

# Run code on 17-Oct-2024 -> works! (created 15 repositories)

# Load environment variables from .env file
load_dotenv()

# Directory containing your project folders from .env file
PROJECTS_DIRECTORY = os.getenv('PROJECTS_DIRECTORY')
# Path to the .gitignore template from .env file
GITIGNORE_TEMPLATE_PATH = os.getenv('GITIGNORE_TEMPLATE_PATH')

# GitHub configuration from .env
GITHUB_ORG = os.getenv('GITHUB_ORG')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_API_URL = os.getenv('GITHUB_API_URL')

# Function to create a new repository on GitHub (modified for org)
def create_repository(repo_name):
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    data = {
        'name': repo_name,
        'private': True  # Change to False if you want the repo to be public
    }

    # Use the organization-specific endpoint
    org_api_url = f'https://api.github.com/orgs/{GITHUB_ORG}/repos'

    response = requests.post(org_api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f'Repository {repo_name} created successfully in organization {GITHUB_ORG}.')
        return True
    else:
        # Log the detailed error message from GitHub
        print(f'Failed to create repository {repo_name} in organization {GITHUB_ORG}: {response.json()}')
        return False

# Function to add a .gitignore file if not present
def add_gitignore(project_path_input):
    gitignore_path = os.path.join(project_path_input, '.gitignore')
    if not os.path.exists(gitignore_path):
        with open(GITIGNORE_TEMPLATE_PATH, 'r') as template_file:
            gitignore_content = template_file.read()
        with open(gitignore_path, 'w') as file:
            file.write(gitignore_content)
        print(f'Added .gitignore to {project_path_input}')

# Change to the projects directory
os.chdir(PROJECTS_DIRECTORY)

# Loop through each folder in the projects directory
for project in os.listdir():
    project_path = os.path.join(PROJECTS_DIRECTORY, project)
    
    # Check if it's a directory (project folder)
    if os.path.isdir(project_path):
        # Add .gitignore if it doesn't exist
        add_gitignore(project_path)
        
        # Create a new repository with the folder name (modified for org)
        if create_repository(project):
            try:
                # Initialize or open the Git repository
                repo = git.Repo.init(project_path)

                # Add all files
                repo.git.add(A=True)
                repo.index.commit('Automated commit: Uploading project')

                # Check if the 'origin' remote exists
                try:
                    remote = repo.remote('origin')
                    print(f"Remote 'origin' already exists, using the existing remote.")
                except ValueError:
                    # Create the remote URL for the organization
                    remote = repo.create_remote('origin',
                                                f'https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_ORG}/{project}.git')
                    print(f"Created new remote 'origin' for {project} in organization {GITHUB_ORG}.")

                # Push to the remote repository
                remote.push(refspec='master')
                print(f'Successfully uploaded {project} to https://github.com/{GITHUB_ORG}/{project}.git')

            except Exception as e:
                print(f'Failed to upload {project}: {str(e)}')
        else:
            print(f'Could not create repository for {project}.')
    else:
        print(f'{project} is not a directory.')
