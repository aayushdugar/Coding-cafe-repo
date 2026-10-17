# Lab 4: Git & GitHub

## Question 1
`--global` means the setting is saved for my user account and applies to all Git repositories I use, unless a repository overrides it. If I leave it out, Git sets the value in the configuration for the current repo (local repo) if  I am inside one.

## Question 2
`ls -a` shows hidden files and folders that ordinary `ls` leaves out, including the `.git` directory. `.git` stores the repository's info.

## Question 3
Git listed the files and folders in `coding-cafe` that were not yet tracked. The exact count depends on the contents of my folder, so I should use the count shown by my own `git status`; entries inside `.venv/` are generated environment files rather than code I wrote and should not be committed.

following output: 
"git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.venv/
	Readme.md
	week02/
	week04/

nothing added to commit but untracked files present (use "git add" to track)"


## Question 4
After I created `.gitignore`, the contents of `.venv/` no longer appeared in `git status` as untracked files. Git now ignores the virtual environment, along with `__pycache__/`, `*.pyc`, and `.DS_Store`, according to the ignore rules.

## Question 5
Yes, `.gitignore` should be committed because it records which generated or unnecessary files Git should ignore. Committing it lets everyone using the repository share the same ignore rules; it should not be ignored itself.

## Question 6
After `git add README.md`, `README.md` moved from Untracked files to Changes to be committed in `git status`. In the three-places model, `git add` copied the file's current contents from the working directory into the staging area (index), ready for the next commit.

## Question 7
After `git commit -m "Lab work so far"`, Git displayed a summary of the new commit, including its abbreviated commit ID, branch, commit message, and the number of files changed. The exact number depends on the files that were staged in my repository. it shows no commits yet with changes to be commited with new file under it: "Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   Readme.md
"

OUTPUT: 
git log --oneline
commit fcd8529e50c9036fb985ced027b3ca8246ddab49 (HEAD -> master)
Author: Aayush Dugar <aayush.dugar.ug26@plaksha.edu.in>
Date:   Mon Oct 12 20:44:02 2026 +0530

    Lab work so far
fcd8529 (HEAD -> master) Lab work so far


## Question 8
The first seven characters are the abbreviated commit hash (or commit ID). They provide a shorter way to identify a particular commit; Git can usually use the abbreviation as long as it uniquely identifies that commit in the repository.

## Question 9
The four steps are **edit, stage, commit, and repeat**. I change files in the working directory, use `git add` to select changes for the staging area, and use `git commit` to save the staged snapshot in the repository's history.

## Question 10
`README.md` is a conventional project overview file that GitHub automatically displays on the repository's front page. Its special name makes it easy for people to find the project's purpose, contents, and basic instructions without opening other files.

## Question 11
`gh auth login` authenticated GitHub CLI (`gh`) with my GitHub account and configured authentication for Git operations. This allows Git to use the saved authentication method when pushing over the network, instead of asking me to enter my GitHub account password for every push.

## Question 12
The repository's front page displays `README.md` as formatted Markdown- which comes . GitHub recognises this standard filename and renders it automatically so visitors can quickly understand the repository and browse its contents.

## Question 13
No, pushing did not change my local commit history. `git push` uploaded my existing commits to the remote GitHub repository; the local commits and their IDs remained the same.

## Question 14
A private repository exists on GitHub but is only accessible to its owner and people or teams who have access to it. A repository that does not exist on GitHub has no online repository page or remote copy there; making a repository private restricts access rather than removing the repository.
