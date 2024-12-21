# 1. Clone the Repository (If Not Already Cloned)
Open git bash
Go to desktop folder or wherever you want to store the repository
clone the repository:
```bash 
git clone https://github.com/YUKTHI-PRABHU/AI-analyser.git
```

Navigate into the repository folder:
```bash 
cd AI-analyser
```


# 2. Create a New Branch
Create a new branch locally with the desired name (e.g., new-feature):
``` bash 
git checkout -b <branch_name>
git checkout -b new-feature
```
This command does two things:
Creates a new branch called new-feature.
Switches to this branch.

# 3. Make Your Changes
Edit your code or add new files to the repository as needed.
After making changes, check the status of modified files:
```bash 
git status
```


# 4. Stage and Commit Changes
Stage the files you want to commit:
```bash 
git add .
```

Commit the changes with a meaningful message:
```bash 
git commit -m <message>
git commit -m "Add a description of the changes made"
```


# 5. Push the New Branch to GitHub
Push the new branch to your GitHub repository:
``` bash
git push -u origin <branch_name>
git push -u origin new-feature
```
here branch name is new-feature.
The -u flag sets the upstream branch for easier future pushes and pulls.

# 6. Verify on GitHub
Go to your GitHub repository AI-analyser.
You should now see the new branch (new-feature) listed in the branches section.
