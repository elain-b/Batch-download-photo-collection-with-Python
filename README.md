#  Batch Download Photozou with Python

"Photozou Batch Download" is a script that automatically downloads the photos in the album using Selenium and Pyautogui and stores them in a folder for each album.

# DEMO

It creates a folder with the album name in the folder called "Album" and stores the downloaded photos.

![]()

When you run this script, you don't have to do anything from launching the browser to closing it.

# Features

This script will reduce your download time.

```python
import os
import pyautogui
import pyperclip
```
[pyautogui] is a module for Python that can operate GUI automatically.
[selenium] is an automation tool that can automatically operate the browser.

# Requirement

* Python 3.7.0b5
* pyautogui 0.9.50
* selenium 3.141.0

```bash
conda create -n auto pip python=3.7 Anaconda
activate auto
```

# Installation

Install selenium with pip command.

```bash
pip3 install pyautogui
pip3 install selenium
pip3 install pyperclip
```

# Usage

Please create python code named "auto.py" and "__init__.py".

# Note

I don't test environments under Linux and Widonws.

# Author

* Bern
* Twitter : https://twitter.com/bern673

# License

Impress you with automation!

Thank you!
