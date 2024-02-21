# Flask

## My environments (os, sw version) ✅

> Windows 11
> python 3.10.7
> pip version 23.1.1
> ELK stack 8.4.2
> Visual Studio Code

## How to install virtualenv 🤔

```shell
pip install virtualenv
```

```shell
virtualenv venv
```

```shell
venv/Scripts/Activate.ps1
```

## Install the packages 📖

```shell
pip install -r requirements.txt
```

## Set the python interpreter in Visual Studio Code ✅

First, if you didn't install Python extension, you need to install [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

And if you installed it, press F1 and search for "Python: Select Interpreter".  
Press enter and set it to "venv/Script/python.exe" in the "venv" directory you just created

## How to run server 🤔

You can run server when press F5 in visual studio code

After you run the server, you can access the following URLs

* [http://localhost:5000/api/swagger](http://localhost:5000/api/swagger)
* [http://localhost:5000/api/common](http://localhost:5000/api/common)
