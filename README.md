# Dreggs
Playing with  Django by creating a bakery

## Assumptions
These installation instructions assume you are using a Linux distro.
PR's are welcome for other OS's.

## Installing with pipenv

### Install pipenv on your local system
```console
[myork@laptop Dreggs]$ pip install pipenv

Collecting pipenv
  Obtaining dependency information for pipenv from https://files.pythonhosted.org/packages/0c/d8/d4e463d4c36da799ae45e27c226f4dbd2d894c47ca67aeb6edfdb5103f86/pipenv-2023.10.20-py3-none-any.whl.metadata
  Downloading pipenv-2023.10.20-py3-none-any.whl.metadata (16 kB)
Collecting certifi (from pipenv)
  Obtaining dependency information for certifi from https://files.pythonhosted.org/packages/4c/dd/2234eab22353ffc7d94e8d13177aaa050113286e93e7b40eae01fbf7c3d9/certifi-2023.7.22-py3-none-any.whl.metadata
  Downloading certifi-2023.7.22-py3-none-any.whl.metadata (2.2 kB)
Collecting setuptools>=67 (from pipenv)
  Obtaining dependency information for setuptools>=67 from https://files.pythonhosted.org/packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl.metadata
  Downloading setuptools-68.2.2-py3-none-any.whl.metadata (6.3 kB)
Collecting virtualenv>=20.24.2 (from pipenv)
  Obtaining dependency information for virtualenv>=20.24.2 from https://files.pythonhosted.org/packages/4e/8b/f0d3a468c0186c603217a6656ea4f49259630e8ed99558501d92f6ff7dc3/virtualenv-20.24.5-py3-none-any.whl.metadata
  Downloading virtualenv-20.24.5-py3-none-any.whl.metadata (4.5 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv>=20.24.2->pipenv)
  Obtaining dependency information for distlib<1,>=0.3.7 from https://files.pythonhosted.org/packages/43/a0/9ba967fdbd55293bacfc1507f58e316f740a3b231fc00e3d86dc39bc185a/distlib-0.3.7-py2.py3-none-any.whl.metadata
  Downloading distlib-0.3.7-py2.py3-none-any.whl.metadata (5.1 kB)
Collecting filelock<4,>=3.12.2 (from virtualenv>=20.24.2->pipenv)
  Obtaining dependency information for filelock<4,>=3.12.2 from https://files.pythonhosted.org/packages/5e/5d/97afbafd9d584ff1b45fcb354a479a3609bd97f912f8f1f6c563cb1fae21/filelock-3.12.4-py3-none-any.whl.metadata
  Downloading filelock-3.12.4-py3-none-any.whl.metadata (2.8 kB)
Collecting platformdirs<4,>=3.9.1 (from virtualenv>=20.24.2->pipenv)
  Obtaining dependency information for platformdirs<4,>=3.9.1 from https://files.pythonhosted.org/packages/56/29/3ec311dc18804409ecf0d2b09caa976f3ae6215559306b5b530004e11156/platformdirs-3.11.0-py3-none-any.whl.metadata
  Downloading platformdirs-3.11.0-py3-none-any.whl.metadata (11 kB)
Downloading pipenv-2023.10.20-py3-none-any.whl (3.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 5.1 MB/s eta 0:00:00
Downloading setuptools-68.2.2-py3-none-any.whl (807 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 8.0 MB/s eta 0:00:00
Downloading virtualenv-20.24.5-py3-none-any.whl (3.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.7/3.7 MB 6.1 MB/s eta 0:00:00
Downloading certifi-2023.7.22-py3-none-any.whl (158 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 158.3/158.3 kB 9.5 MB/s eta 0:00:00
Downloading distlib-0.3.7-py2.py3-none-any.whl (468 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 468.9/468.9 kB 5.6 MB/s eta 0:00:00
Downloading filelock-3.12.4-py3-none-any.whl (11 kB)
Downloading platformdirs-3.11.0-py3-none-any.whl (17 kB)
Installing collected packages: distlib, setuptools, platformdirs, filelock, certifi, virtualenv, pipenv
Successfully installed certifi-2023.7.22 distlib-0.3.7 filelock-3.12.4 pipenv-2023.10.20 platformdirs-3.11.0 setuptools-68.2.2 virtualenv-20.24.5

```

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
## Installing the developer tools
If you are planning to develop, or contribute to the project then you'll want these additional libraries installed.
```console
[myork@laptop Dreggs]$ pipenv install --dev

Installing dependencies from Pipfile.lock (efb681)...
Installing dependencies from Pipfile.lock (efb681)...
```

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