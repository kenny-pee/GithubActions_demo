# GithubActions_demo

## Continuous Integration

Continuous Integration (CI) is a software practice that requires frequently committing code to a shared repository.

When you commit a code to your repo, you can continuously build and test the code to make sure that the commit doesnt introduce errors. Your tests can include code linters (that checks for style formatting), security checks, code coverage, functional test, and other custom tests.

Building and testing code requires a server. You can build and test updates locally before pushing code to a repo, or use a CI server that checks for new code commits in a repo.

## Continuous Deployment

CD is a strategy for software releases wherein any code commit that passes the automated testing phase is automatically released into the prod env, making changes that are visible to the software users.

## Github Actions:

1) Runs github checkout
2) Setup CPython
3) Install dependencies
4) Check for syntax errors / undefined variables
5) Test app with Pytest
6) Deploy onto Heroku
