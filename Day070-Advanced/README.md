# `Day 70 - Advanced`
# Introduction to Git

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. It is easy to learn and has a tiny footprint with lightning-fast performance. This document serves as a quick start guide to using Git for version control in your projects.

## Setting Up a Repository

To begin using Git, you need to create a repository. Here's how:

### Initialize a Local Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create your project.
3. Run the following command to initialize a new Git repository:


---

# Git Cheat Sheet
A comprehensive guide to various Git commands for efficient version control management.

## Configuration
Configure your Git environment with these commands.

| Command | Description |
|---------|-------------|
| `git config --global user.name "Your Name"` | Set your global username. |
| `git config --global user.email "youremail@example.com"` | Set your global email address. |

## Branches
Manage your branches efficiently with these commands.

| Command | Description |
|---------|-------------|
| `git branch <branch_name>` | Create a new branch. |
| `git branch -d <branch_name>` | Delete a branch (only if it has been merged). |
| `git switch <branch_name>` | Switch to an existing branch. |
| `git switch -c|--create <branch_name>` | Create and switch to a new branch. |
| `git restore <file_path>` | Discard changes in the working directory. |
| `git checkout <file_path>` | Discard changes in the working directory (deprecated, use `git restore`). |
| `git merge <branch_name>` | Merge a branch into the current branch. |

## Pulling
Update your local repository with these commands.

| Command | Description |
|---------|-------------|
| `git pull --rebase --prune` | Update your local branch with the latest changes from the remote, rebase any local changes on top, and prune deleted remote-tracking branches. |

## Staged Changes
Manage staged changes with these commands.

| Command | Description |
|---------|-------------|
| `git add <file_path>` | Stage the specified file(s) for commit. |
| `git add -p <file_path>` | Partially stage specific changes within a file. |
| `git mv <old_file_path> <new_file_path>` | Rename/move a file and stage the change. |
| `git rm --cached <file_path>` | Unstage a file without deleting it. |
| `git rm --force <file_path>` | Unstage and delete a file. |
| `git reset HEAD` | Unstage all changes. |
| `git reset --hard HEAD` | Unstage and discard all changes. |
| `git clean -f|--force -d` | Remove untracked files and directories. |
| `git clean -f|--force -d -x` | Remove untracked and ignored files/directories. |

## Changing Commits
Alter commit history with these commands.

| Command | Description |
|---------|-------------|
| `git reset <commit_hash>` | Reset the current branch to a specific commit. |
| `git reset HEAD~1` | Reset the current branch to the previous commit. |
| `git reset --hard <commit_hash>` | Reset both the current branch and the working directory to a specific commit. |
| `git commit --amend -m "New message"` | Amend the most recent commit with a new message. |
| `git commit --fixup <commit_hash> -m "New message"` | Amend a specific commit with a new message. |
| `git revert <commit_hash>` | Create a new commit that undoes the changes made in a specific commit. |
| `git rebase --interactive [branch_name]` | Start an interactive rebase session. |
| `git cherry-pick <commit_hash>` | Apply the changes introduced by a specific commit onto the current branch. |

## Compare
Compare changes with these commands.

| Command | Description |
|---------|-------------|
| `git diff` | Show differences between the working directory and the index/last commit. |
| `git diff HEAD HEAD~2` | Show differences between the current commit and the one before it. |
| `git diff <branch_name>..<other_branch_name>` | Show differences between two branches. |

## View
View commit history and changes with these commands.

| Command | Description |
|---------|-------------|
| `git log` | Show commit history. |
| `git log --patch` | Show commit history along with line-level changes. |
| `git log --decorate --graph --oneline` | Show a graphical representation of the commit history. |
| `git log --grep="pattern"` | Filter commit history by messages containing a specific pattern. |
| `git show <commit_hash>` | Display the changes made in a specific commit. |
| `git blame <file_path>` | Show which commit last modified each line in a file. |

## Stash
Save and reapply changes with these commands.

| Command | Description |
|---------|-------------|
| `git stash push -m "stash_message"` | Save changes in a new stash. |
| `git stash --include-untracked` | Include untracked files in the stash. |
| `git stash --staged` | Only stash staged changes. |
| `git stash list` | List all saved stashes. |
| `git stash apply` | Reapply the most recently stashed changes. |
| `git stash apply <stash@{n}>` | Reapply a specific stash. |
| `git stash clear` | Remove all stashes. |

## Tags
Manage tags with these commands.

| Command | Description |
|---------|-------------|
| `git tag` | List all tags. |
| `git tag -a <tag_name> -m "tag_message"` | Create a new annotated tag. |
| `git tag -d <tag_name>` | Delete a tag. |
| `git push --tags` | Push all tags to the remote repository. |

## Remote
Manage remote repositories with these commands.

| Command | Description |
|---------|-------------|
| `git remote -v` | List all configured remotes. |
| `git remote show <remote_name>` | Show information about a specific remote. |
| `git remote add <remote_name> <url>` | Add a new remote repository. |
| `git fetch <remote_name>` | Fetch all branches from a remote repository. |
| `git rebase <remote_name>/<branch_name>` | Rebase your current branch onto a remote branch. |
| `git push --force` | Force-push changes to the remote repository. |
| `git push --force-with-lease` | Safe force-push: only if the remote branch is at the expected state. |
| `git push --tags` | Push all tags to the remote repository. |

## Submodules
Manage submodules with these commands.

| Command | Description |
|---------|-------------|
| `git submodule status` | Show the status of all submodules. |
| To pull submodules: |
| 1. `git submodule sync` |
| 2. `git submodule init` |
| 3. `git submodule update` |
| To change branch in a submodule: |
| 1. `cd <submodule_path>` |
| 2. `git fetch origin <branch_name>` |
| 3. `git checkout <branch_name>` |
| 4. `cd ..` |
