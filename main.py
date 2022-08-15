import argparse
import os
from git import Repo
from github import Github
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env")

username = "Baumistlustig"

rw_dir = os.path.dirname(os.path.abspath(__file__))

# Connect to GitHub Account
g = Github(os.environ["ACCESS_TOKEN"])

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('RepoName',
                       metavar='repository_name',
                       type=str,
                       help='The name of the repository you want to create'
                       )

my_parser.add_argument('Path',
                       metavar='repository_path',
                       type=str,
                       help='The path of the repository you want to create'
                       )

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path
repo_name = args.RepoName

user = g.get_user()
remote_repo = user.create_repo(repo_name)

local_repo = Repo.init(os.path.join(rw_dir, input_path))
url = f"https://github.com/{username}/{repo_name}"

origin = local_repo.create_remote('origin', url)

assert origin.exists()
assert origin == local_repo.remotes.origin == local_repo.remotes['origin']
origin.fetch()  # assure we actually have data. fetch() returns useful information

# Create README.md in remote
remote_repo.create_file("README.md", "Added README.md", f"# {repo_name} | Created by CLI", branch="master")

origin.fetch()

print(f"Created empty repository named {repo_name} under {url}")