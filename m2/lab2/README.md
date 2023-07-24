# Lab 2: Dependencies, Inheritance, and Version Control

## Introduction

In this lab, you will practice basic git commands for a version control protected workflow. This lab will set the standard for how all future assignments are submitted, so it is important that you understand the process and ask questions whenever you get stuck. You will also practice object oriented programming and dependency management in Python. You will need to pay close attention to documentation and the instructions provided.

## Task 1: Installing Git, Creating a GitHub Account, and Setting Up Keys

**THIS TASK IS HARD. PAY CLOSE ATTENTION TO THE INSTRUCTIONS.**

- Install Git on your local machine.
  - **NOTE:** If you are on a Mac with Homebrew installed, you can run `brew install git` to install Git.
  - **NOTE:** If you are on a Mac without Homebrew installed, you can download the Git installer from [here](https://git-scm.com/download/mac).
  - **NOTE:** If you are on a Linux machine (including WSL), you can run `sudo apt-get install git` to install Git from the Ubuntu terminal.
- Create a GitHub account if you do not already have one.
  - **TIP:** DO NOT USE YOUR SCHOOL EMAIL ADDRESS. USE A PERSONAL EMAIL ADDRESS.
- Set up your SSH keys on your local machine.
  - **TIP:** Follow the official instructions on github [here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).
  - **TIP:** See the `gitGoing.md` document in this week's directory for more information on this process.
- Add your SSH key to your GitHub account.
  - **TIP:** Follow the official instructions on github [here](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
  - **TIP:** See the `gitGoing.md` document in this week's directory for more information on this process.

## Task 2: Repository Setup

- **TIP:** See the lab video on Canvas for a demonstration of this process.
- Go to [github](https://github.com) and login to your account.
- Create a new repository called `itsc-3155` and make it private.
- Copy the SSH clone URL for your new repository.
- In your terminal, navigate to your local course folder.
- Run `git init` to initialize a new git repository.
- Run `git remote add origin <your_clone_url>` to add your remote repository to your local repository.

## Task 3: Tracking, Committing, and Pushing Changes

- Add all of your files to the staging area by running `git add .`.
- Commit your changes by running `git commit -m "<your_commit_message>"`.
- Push your changes to the remote repository by running `git push -u origin main`.

## Task 4: Calculator Application

- Unzip the `m2.zip` file in your local course folder as you did in the previous lab.
- In your terminal, navigate to the `m2/calculator` directory.
- Open the `simple_operations.py` file.
- Complete `TODO 1` by finishing the subtraction operation.
- Complete `TODO 2` by finishing the multiplication operation.
- Complete `TODO 3` by finishing the division operation but make sure to handle the case where the denominator is zero.
- Open the `scientific_operations.py` file.
- Complete `TODO 4` by finishing the cosine operation using the `math` module.
  - **TIP:** See the `math` module documentation [here](https://docs.python.org/3.10/library/math.html).
- Complete `TODO 5` by finishing the tangent operation using the `math` module.
- Complete `TODO 6` by finishing the natural log operation using the `math` module.
- Test that your calculator works by running `python3.10 gui.py`.
- Add, commit, and push the changes you have made to your repository (just like you did in the previous task).

## Task 5: Package Installation and Dependency Management

- In your terminal, navigate to the `m2/polygon` directory.
  - **TIP:** If you are currently in the `calculator` directory, you can run `cd ../polygons` to go up one directory and then into the `polygons` directory.
- Use pip to install the Pygame module. Shown below are a few variations of how the `pip` command may work on your machine. If the first doesn't work, move on to the next. If none of them work, ask for help.
  - `pip install pygame`
  - `py -m pip install pygame`
  - `python -m pip install pygame`
  - `python3 -m pip install pygame`
  - `python3.10 -m pip install pygame`
- Remember which command you used to install Pygame. This will be important for later tasks and future labs.
- Install all packages listed in the `requirements.txt` file using `pip`. You can do this by running a command like the following (may vary depending on which command worked for you earlier):
  - `pip install -r requirements.txt`
- Once you have successfully run the command above, run a command like the following to write the list of packages you have installed to a file called `freeze.txt`:
  - `pip freeze > freeze.txt`

## Task 6: Polygon Visualizer Basics

- Open the `polygons.py` file.
- Complete `TODO 7` in the `Polygons` class by adding an attribute called `num_sides` and setting it equal to the parameter `num_sides` that is passed into the constructor.
- Complete `TODO 8` in the `Polygons` class by adding an attribute called `side_length` and setting it equal to the parameter `side_length` that is passed into the constructor.
- Complete `TODO 9` in the `Polygons` class by adding an attribute called `radius` and setting it equal to the result of the equation provided in the comments.
- Complete `TODO 10` in the `Polygons` class by adding an attribute called `area` and setting it equal to the result of the `polygon_area` method.

## Task 7: Fixing GUIs

- Open the `tkinterGUI.py` file.
- Complete `TODO 11` in the `TkinterGUI` class by fixing the object's definition so that it inherits from the `Polygons` class.
- Complete `TODO 12` in the `TkinterGUI` class by fixing its constructor so that it calls the `Polygons` constructor and passes in the correct parameters. Use standard Python inheritance syntax to do this.
- Open the `pygameGUI.py` file.
- Complete `TODO 13` in the `PygameGUI` class by fixing the object's definition so that it inherits from the `Polygons` class.
- Complete `TODO 14` in the `PygameGUI` class by fixing its constructor so that it calls the `Polygons` constructor and passes in the correct parameters. Use standard Python inheritance syntax to do this.
- Add, commit, and push the changes you have made to your repository.

## Submission Details

- On Canvas, submit the following:
  - The URL to your GitHub repository.
  - Make sure that the TAs have been included as collaborators on your repository.
