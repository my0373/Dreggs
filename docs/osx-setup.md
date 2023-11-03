# Dreggs
Playing with  Django by creating a bakery

## Assumptions
These installation instructions assume you are using a Linux distro.
PR's are welcome for other OS's.

## Installing with pipenv

### Install pipenv on your local system
Follow the instructions here https://stackoverflow.com/questions/67733566/how-to-use-pipenv-on-mac

### Cloning the stable branch
```console
[myork@laptop ~]$ git clone https://github.com/my0373/Dreggs.git
```
### Switch to the project directory

```console
[myork@laptop ~]$ cd Dreggs/
[myork@laptop Dreggs]$ 
```


### Installing the project dependencies using pipenv

```console
➜  Dreggs git:(dev) ✗ pipenv install
Creating a virtualenv for this project...
Pipfile: /Users/myork/Dreggs/Pipfile
Using /Users/myork/.pyenv/versions/3.12.0/bin/python3 (3.12.0) to create virtualenv...
⠹ Creating virtual environment...created virtual environment CPython3.12.0.final.0-64 in 240ms
  creator CPython3Posix(dest=/Users/myork/.local/share/virtualenvs/Dreggs-bEnJ5RSh, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/Users/myork/Library/Application Support/virtualenv)
    added seed packages: pip==23.3.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /Users/myork/.local/share/virtualenvs/Dreggs-bEnJ5RSh
Installing dependencies from Pipfile.lock (690ee7)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

```
## Installing the developer tools
If you are planning to develop, or contribute to the project then you'll want these additional libraries installed.
```console
➜  Dreggs git:(dev) ✗ pipenv install --dev
Installing dependencies from Pipfile.lock (690ee7)...
Installing dependencies from Pipfile.lock (690ee7)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

### Configuring VSCode default interpreter to use the pipenv version of python
```console
➜  Dreggs git:(dev) ✗ pipenv --venv
/Users/myork/.local/share/virtualenvs/Dreggs-bEnJ5RSh

```
### Configuring VSCode default interpreter to use the pipenv version of python
1. Press keys ``` ctrl + shift + p ``` to open the command palette
1. Select: ``` Python: Select interpreter```
1. Select: ``` Enter interpreter path```
1. Paste the output from the venv path above and append ```/bin/python```. 
1. You should end up with a path that looks similar to ```/home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c/bin/python```
1. Press return
1. You can then open the terminal with ``` ctrl+` ``` shortcut and it will load your pipenv automagically. 


## Troubleshooting pipenv

### Enter the pipenv shell
```console
[myork@laptop Dreggs]$ pipenv shell

Launching subshell in virtual environment...
 . /home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c/bin/activate
[myork@laptop Dreggs]$  . /home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c/bin/activate

(Dreggs) [myork@laptop Dreggs]$ 
```

### Check the python packages you have installed. You should see something like this.
```console
(Dreggs) [myork@laptop Dreggs]$ pip freeze

asgiref==3.7.2
Django==4.2.6
sqlparse==0.4.4
```


### To leave the current pipenv shell

```console
(Dreggs) [myork@laptop Dreggs]$ deactivate

[myork@laptop Dreggs]$
```

### To rebuild the lockfile from the original Pipenv
```console
[myork@laptop Dreggs]$ pipenv install

Creating a virtualenv for this project...
Pipfile: /home/myork/Dreggs/Pipfile
Using /usr/bin/python3 (3.12.0) to create virtualenv...
⠙ Creating virtual environment...created virtual environment CPython3.12.0.final.0-64 in 100ms
  creator CPython3Posix(dest=/home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(extra_search_dir=/usr/share/python-wheels,download=False, pip=bundle, via=copy, app_data_dir=/home/myork/.local/share/virtualenv)
    added seed packages: pip==23.2.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c
Installing dependencies from Pipfile.lock (efb681)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

### To clean up pipenv (in case you need to reinstall)
```console
[myork@laptop Dreggs]$ pipenv --rm
Removing virtualenv (/home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c)...
```