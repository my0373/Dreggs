# Dreggs
Playing with  Django by creating a bakery

## Installing with pipenv
### Cloning the stable branch
```[shell]
[myork@laptop ~]$ git clone https://github.com/my0373/Dreggs.git
```
### Switch to the project directory

```[shell]
[myork@laptop ~]$ cd Dreggs/
[myork@laptop Dreggs]$ 
```


### Installing the project dependencies using pipenv

```[shell]
[myork@laptop Dreggs]$ pipenv install

Creating a virtualenv for this project...
Pipfile: /home/myork/Dreggs/Pipfile
Using /usr/bin/python3 (3.12.0) to create virtualenv...
⠙ Creating virtual environment...created virtual environment CPython3.12.0.final.0-64 in 101ms
  creator CPython3Posix(dest=/home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(extra_search_dir=/usr/share/python-wheels,download=False, pip=bundle, via=copy, app_data_dir=/home/myork/.local/share/virtualenv)
    added seed packages: pip==23.2.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c
Installing dependencies from Pipfile.lock (efb681)...

```
## Troubleshooting pipenv

### Enter the pipenv shell
```[shell]
[myork@laptop Dreggs]$ pipenv shell

Launching subshell in virtual environment...
 . /home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c/bin/activate
[myork@laptop Dreggs]$  . /home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c/bin/activate

(Dreggs) [myork@laptop Dreggs]$ 
```


### To leave the current pipenv shell

```[shell]
(Dreggs) [myork@laptop Dreggs]$ deactivate
```

### To rebuild the lockfile from the original Pipenv
```[shell]
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
```[shell]
[myork@laptop Dreggs]$ pipenv --rm
Removing virtualenv (/home/myork/.local/share/virtualenvs/Dreggs-V9WQHE1c)...
```