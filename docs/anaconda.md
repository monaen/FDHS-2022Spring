# Anaconda

## Introduction
[Anaconda](https://anaconda.org/) is a distribution of packages built for data science. It comes with <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code>, a package and environment manager. You can use conda to create environments for isolating your projects that use different versions of Python and/or different packages. You can also use it to install, uninstall, and update packages in your environments. With Anaconda, your life working with data will be much more pleasant.

In this python course, we use Anaconda to manage packages and environments for use with Python. With Anaconda, it's simple to install the packages that are often used in data science work. You can also use it to create virtual environments that make working on multiple projects much less mind-twisting. Anaconda will simplify your workflow and solve a lot of issues you had dealing with packages and multiple Python versions.

Anaconda is actually a **distribution of software** that comes with <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code>, Python, and over **150** scientific packages and their dependencies. The application <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code> is a package and environment manager. Anaconda is a fairly large download (~500 MB) because it comes with the most common data science packages in Python. If you don't need all the packages or need to conserve bandwidth or storage space, there is also **Miniconda**, a smaller distribution that includes only <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code> and Python. You can still install any of the available packages with <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code>, it just doesn't come with them.

<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">Conda</code> is a program you'll be using exclusively from the command line, so if you aren't comfortable using it, check out this [command prompt tutorial for Windows](https://www.lynda.com/-tutorials/Windows-command-line-basics/497312/513424-4.html) or the [Linux Command Line Basics](https://www.udacity.com/course/linux-command-line-basics--ud595) course for OSX/Linux.

You probably already have Python installed and wonder why you need this at all. First, since Anaconda comes with a bunch of data science packages, you'll be all set to start working with data. Secondly, using <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code> to manage your packages and environments will reduce future issues dealing with the various libraries you'll be using.


### Managing Packages

Package managers are used to install libraries and other software on your computer. You’re probably familiar with [pip](https://pypi.org/project/pip/), it’s the default package manager for Python libraries. <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">Conda</code> is similar to [pip](https://pypi.org/project/pip/) except that the available packages are focused around data science while [pip](https://pypi.org/project/pip/) is for general use. However, <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code> is not Python specific like [pip](https://pypi.org/project/pip/) is, it can also install non-Python packages. It is a package manager for any software stack. That being said, not all Python libraries are available from the Anaconda distribution and <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code>. You can (and will) still use [pip](https://pypi.org/project/pip/) alongside <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda</code> to install packages.

<code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">Conda</code> installs precompiled packages. For example, the Anaconda distribution comes with Numpy, Scipy and Scikit-learn compiled with the MKL library, speeding up various math operations. The packages are maintained by contributors to the distribution which means they usually lag behind new releases. But because someone needed to build the packages for many systems, they tend to be more stable (and more convenient for you).


### Managing Environments

Along with managing packages, <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">Conda</code> is also a virtual environment manager. It's similar to virtualenv and pyenv, other popular environment managers.

Environments allow you to separate and isolate the packages you are using for different projects. Often you’ll be working with code that depends on different versions of some library. For example, you could have code that uses new features in Numpy, or code that uses old features that have been removed. It’s practically impossible to have two versions of Numpy installed at once. Instead, you should make an environment for each version of Numpy then work in the appropriate environment for the project.

This issue also happens a lot when dealing with Python 2 and Python 3. You might be working with old code that doesn’t run in Python 3 and new code that doesn’t run in Python 2. Having both installed can lead to a lot of confusion and bugs. It’s much better to have separate environments.

You can also export the list of packages in an environment to a file, then include that file with your code. This allows other people to easily load all the dependencies for your code. Pip has similar functionality with <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">pip freeze > requirements.txt</code>.



## Installation

Anaconda is available for diverse systems including **Windows**, **Mac OS X**, and **Linux**. You can find the installers at the official webpage [https://www.anaconda.com/download/](https://www.anaconda.com/download/).

And you can also find the installation guidelines from the following links:

* [Installing on Windows](https://docs.anaconda.com/anaconda/install/windows/)
* [Installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
* [Installing on Linux](https://docs.anaconda.com/anaconda/install/linux/)

If you already have Python installed on your computer, this won't break anything. Instead, the default Python used by your scripts and programs will be the one that comes with Anaconda.

Choose the Python 3.8 version (the current version). Also, choose the 64-bit installer if you have a 64-bit operating system, otherwise go with the 32-bit installer. Go ahead and choose the appropriate version, then install it.

After installation, you’re automatically in the default conda environment with all packages installed which you can see below. You can check out your own install by entering conda list into your terminal.


A number of applications are installed along with Anaconda:

* **Anaconda Navigator**, a GUI for managing your environments and packages
* **Anaconda Prompt**, a terminal where you can use the command line interface to manage your environments and packages
* **Spyder**, an IDE geared toward scientific development
* **Notebook**, a web application that allows users to create and share documents that contain live code, equations, visualizations and text
* **JupyterLab**, a web-based interactive development environment (IDE) for Jupyter notebooks, code, and data. [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) helps to configure and arrange the user interface to support a wide range of workflows in data science, scientific computing, and machine learning.

In this course, we will use the **JupyterLab** to manage the course projects and codes. To start the JupyterLab, one can start by opening the **Anaconda Navigator**,
1. Run the **Anaconda Navigator** (for windows)

[<img src="https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/1.png" alt="Anaconda Navigator" width="600">](https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/1.png)

2. From the Navigator, run the **JupyterLab** by clicking the `Launch` button of the JupyterLab.

[<img src="https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/2.png" alt="Anaconda Navigator" width="1000">](https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/2.png)

3. After a while, an webpage will open and you will see the starting page of JupyterLab (for windows)

[<img src="https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/3.png" alt="Anaconda Navigator" width="800">](https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/3.png)

4.(optional) To avoid errors later, it's best to update all the packages in the default environment. Open the **Terminal** application by clicking the button

[<img src="https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/4.png" alt="Anaconda Navigator" width="300">](https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/4.png)


In the prompt, run the following commands:
```python
conda upgrade conda
conda upgrade --all
```
and answer (type) <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">y</code> for "yes" when asked if you want to install the packages. The packages that come with the initial install tend to be out of date, so updating them now will prevent future errors from out of date software.

Note: In the previous step, running <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">conda upgrade conda</code> should not be necessary because <code style="color:#fff;background-color:#2f3d48;border-radius: 4px;border: 1px solid #737b83;padding: 2px 4px">--all</code> includes the conda package itself, but some users have encountered errors without it.

[<img src="https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/5.png" alt="Anaconda Navigator" width="800">](https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/5.png)

[<img src="https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/6.png" alt="Anaconda Navigator" width="800">](https://github.com/monaen/DHLO-2021Spring/raw/main/materials/images/6.png)

From now on, you have successfully installed the Anaconda and updated the conda package. In Session 3, we will use the  JupyterLab to learn python and manage the course projects. You are also encouraged to explore JupyterLab before the session. There are many resources about how to use JupyterLab from both the official websites or the others courses. Have fun with it!




