# github-cli

GitHub-CLI is a project to controll GitHub via a Command Line Interface

## Installation

1. Clone the repository
`git clone https://github.com/Baumistlustig/github-cli`

2. Go into the cloned directory
`cd github-cli`

3. Run the install.sh script as root
`sudo bash install.sh`

4. Enter your username and press enter

5. Paste a [personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
and press enter

### Requirements
You need to have installed: `Git, Python`

Works on: `Linux/UNIX`

## Usage

### Creating a remote Repository and a local clone of it
`github create-repo <name> <path>`

name: `the name of the remote-repo e.g. test`

path: `the absolute path to your local clone e.g. /home/johannes/test`

### Deleteing a remote repository
`github delete-repo <name>`

name: `name of the repository e.g. tes`
