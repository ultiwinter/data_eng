# Data Enginering Projects

This repository is dedicated to data engineering projects, developed by Abdallah Eid and Ahmed Sheta.

# Creating the Environment

The repository contains the file `.env.template`. This file is a template for
the environment variables that need to be set for the application to run. Copy
this file into a file called `.env` at the root level of this repository and
fill in all values with the corresponding secrets.

To create the virtual environment in this project you must have `pipenv`
installed on your machine. Then run the following commands:

```bash
# for development environment
pipenv install --dev
# for production environment
pipenv install
```

To work within the environment you can now run:

```bash
# to activate the virtual environment
pipenv shell
# to run a single command
pipenv run <COMMAND>
```

# Running the app

To run the application the `pipenv` environment must be installed and all needed
environment variables must be set in the `.env` file. Then the application can
be started via

```bash
pipenv run python src/main.py
```

# Pre-Commit Hooks

This repository uses `pre-commit` hooks to ensure a consistent and clean file organization. Each registered hook will be executed when committing to the repository. To ensure that the hooks will be executed they need to be installed using the following command:

```bash
pre-commit install
```

The following things are done by hooks automatically:

- formatting of python files using black and isort
- formatting of other files using prettier
- syntax check of JSON and yaml files
- adding new line at the end of files
- removing trailing whitespaces
- prevent commits to `dev` and `main` branch
- check adherence to REUSE licensing format


## Branching Strategy

**main**: It contains fully stable production code

- **dev**: It contains stable under-development code

  - **epic**: It contains a module branch. Like high level of feature. For example, we have an authentication module then we can create a branch like "epic/authentication"

    - **feature**: It contains specific features under the module. For example, under authentication, we have a feature called registration. Sample branch name: "feature/registration"

    - **bugfix**: It contains bug fixing during the testing phase and branch name start with the issue number for example "bugfix/3-validate-for-wrong-user-name"

## Commits and Pull Requests

The stable branches `main` and `dev` are protected against direct pushes. To commit code to these branches create a pull request (PR) describing the feature/bugfix that you are committing to the `dev` branch. This PR will then be reviewed by another SD from the project. Only after being approved by another SD a PR may be merged into the `dev` branch. Periodically the stable code on the `dev` branch will be merged into the `main` branch by creating a PR from `dev`. Hence, every feature that should be committed to the `main` branch must first run without issues on the `dev` branch for some time.

## Pull Request Workflow

The **main** and **dev** branches are protected against direct pushes, which means that we want to do a Pull Request (PR) in order to merge a developed branch into these branches. Having developed a branch (let's call it **feature-1**) and we want to merge **feature-1** branch into **main** branch.

Here is a standard way to merge pull requests:

1. Have all your local changes added, committed, and pushed on the remote **feature-1** branch

   ```bash
   git checkout feature-1
   git add .
   git commit -m "added a feature" --signoff  # don't forget the signoff ;)
   git push
   ```

2. Make sure your local main branch up-to-date

   ```bash
   git checkout main
   git pull main
   ```

3. Go to Pull Requests click on "New pull request" > make sure the base is **main** branch (or **dev** branch, depends on which branch you want to update) and the compare to be your **feature-1** branch.

   Make sure to link the issue your PR relates to.

4. Delete the feature branch **feature-1** once it has been merged into the target branch.

_**In case of merge conflict:**_

Should we experience merge conflict after step 3, we should solve the merge conflicts manually, below the title of "This branch has conflicts that must be resolved" click on web editor (you can use vscode or any editor you want).
The conflict should look like this:

```bash
<<<<<<< HEAD
// Your changes at **feature-1** branch
=======
// Data already on the main branch
>>>>>>> main
```

-choose which one of these you would adopt for the merge to the **main** branch, we would be better off solving the merge -conflicts together rather than alone.
-mark it as resolved and remerge the PR again, there shouldn't any problem with it.
