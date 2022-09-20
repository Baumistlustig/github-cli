#! /usr/bin/python

import argparse
import os
from git import Repo
from github import Github
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')

# Connect to GitHub Account
g = Github(os.getenv('ACCESS_TOKEN'))

# Create the parser
parser = argparse.ArgumentParser(description='List the content of a folder')

user = g.get_user()


def createRepo(args):
    # Execute the parse_args() method
    args = parser.parse_args()

    input_path = args.Path
    repo_name = args.RepoName

    remote_repo = user.create_repo(repo_name)

    os.mkdir(input_path)

    local_repo = Repo.init(os.path.join(input_path))
    url = f'https://github.com/{username}/{repo_name}'

    origin = local_repo.create_remote('origin', url)

    assert origin.exists()
    assert origin == local_repo.remotes.origin == local_repo.remotes['origin']
    origin.fetch()

    # Create README.md in remote
    remote_repo.create_file('README.md', 'Added README.md', f'# {repo_name} | Created by CLI', branch='master')

    origin.fetch()

    print(f'Created empty repository named {repo_name} under {url}')


def deleteRepo(args):
    name = args.Name

    args = parser.parse_args()

    repo = user.get_repo(name)
    repo.delete()
    print(f"Deleted {name} repository!")


# Create Subparser
subparser = parser.add_subparsers()

# Create Repo arguments
create_repo = subparser.add_parser('create-repo')
delete_repo = subparser.add_parser('delete-repo')

create_repo.add_argument('RepoName',
                         metavar='repository_name',
                         type=str,
                         help='The name of the repository you want to create'
                         )

create_repo.add_argument('Path',
                         metavar='repository_path',
                         type=str,
                         help='The path of the repository you want to create'
                         )

create_repo.set_defaults(func=createRepo)

# Delete Repo Arguments
delete_repo.add_argument('Name',
                         metavar='repository_name',
                         type=str,
                         help='The name of the repository you want to delete')

delete_repo.set_defaults(func=deleteRepo)

cmd = parser.parse_args()
cmd.func(cmd)
