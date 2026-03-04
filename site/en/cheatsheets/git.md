# Git Cheatsheet

Quick reference for Git commands.

## Setup

```bash
# Global configuration
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# View configuration
git config --list
git config user.name
```

## Getting Started

```bash
# Initialize a new repo
git init

# Cloning
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git my-folder
```

## Basic Commands

```bash
# Status
git status
git status -s  # short format

# Adding files
git add file.txt
git add .
git add -A
git add *.py

# Commit
git commit -m "Message"
git commit -am "Add and commit"  # tracked files only

# History
git log
git log --oneline
git log --graph --oneline --all
git log -n 5  # last 5

# Diff
git diff              # unstaged changes
git diff --staged     # staged changes
git diff HEAD~1       # with previous commit
```

## Branches

```bash
# List branches
git branch        # local
git branch -a     # all (including remote)

# Create
git branch feature
git checkout -b feature  # create and switch
git switch -c feature    # new syntax

# Switch
git checkout main
git switch main

# Delete
git branch -d feature    # safe delete
git branch -D feature    # force delete

# Rename
git branch -m old-name new-name
```

## Merge & Rebase

```bash
# Merge
git checkout main
git merge feature

# Merge without fast-forward
git merge --no-ff feature

# Rebase
git checkout feature
git rebase main

# Interactive rebase
git rebase -i HEAD~3

# Abort merge
git merge --abort

# Abort rebase
git rebase --abort
```

## Remote

```bash
# List remotes
git remote -v

# Add remote
git remote add origin https://github.com/user/repo.git

# Fetch changes
git fetch origin
git pull origin main

# Push changes
git push origin main
git push -u origin main  # set upstream

# Delete remote branch
git push origin --delete feature
```

## Stash

```bash
# Save changes
git stash
git stash push -m "WIP: feature"

# List stashes
git stash list

# Apply
git stash pop          # apply and remove
git stash apply        # apply and keep
git stash apply stash@{2}

# Delete
git stash drop stash@{0}
git stash clear  # all
```

## Undoing Changes

```bash
# Unstage file
git restore --staged file.txt
git reset HEAD file.txt  # old syntax

# Discard changes in file
git restore file.txt
git checkout -- file.txt  # old syntax

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert (creates a new commit)
git revert HEAD
git revert abc1234
```

## Tags

```bash
# List tags
git tag

# Create
git tag v1.0.0
git tag -a v1.0.0 -m "Release 1.0.0"

# Push tags
git push origin v1.0.0
git push origin --tags

# Delete
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## Cherry-pick

```bash
# Apply a specific commit
git cherry-pick abc1234

# Without auto-commit
git cherry-pick --no-commit abc1234
```

## Useful Commands

```bash
# Find commit with a bug
git bisect start
git bisect bad          # current commit is bad
git bisect good abc123  # this commit is good
# ... git automatically finds it

# Blame (who changed a line)
git blame file.txt

# Show commit
git show abc1234
git show HEAD~2

# Compare branches
git diff main..feature

# Clean untracked files
git clean -n  # dry run
git clean -f  # force
git clean -fd # including directories
```

## .gitignore

```gitignore
# Files
*.log
*.pyc
.env

# Directories
__pycache__/
node_modules/
.venv/
dist/

# Exceptions
!important.log

# Patterns
docs/*.txt
**/temp/
```

## Aliases (recommended)

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"
```
