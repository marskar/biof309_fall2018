Syllabus
========
**Introduction to Python Programming - BIOF309 - FAES**

**Fall 2018**

**Time: Thursday 5:30PM - 7:30PM**

*This document is subject to revision!*

Changes are tracked using the git version control system.

To interact with the materials in the repo using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) (via [Binder](https://mybinder.org/)), please click the button below.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/marskar/biof309_fall2018/master?urlpath=lab)

Additionally, the [Jupyter Notebooks (`ipynb` files)](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) in this repo can be opened in [Google colab](https://colab.research.google.com) by clicking the icon below.

<a href="http://colab.research.google.com/github/marskar/biof309_fall2018/blob/master/index.ipynb"><img src="https://colab.research.google.com/img/colab_favicon_256px.png" width="48"></a>

Instructors
-----------

* Martin Skarzynski - marskar at gmail dot com
* Jinping Liu - liu dot jinping at nih dot com
* Michael Chambers - michael dot chambers2 at nih dot gov

Course Description
------------------

This course is designed for non-programmers, biologists, or those without specific knowledge of Python to learn how to program.
Week by week, we will slowly build up your skills and understanding of computer programming and the Python programming language.
There will be in-class demonstrations, using [PyCharm](https://www.jetbrains.com/pycharm/features/) and to a lesser extent [JupyterLab](http://jupyterlab.readthedocs.io), and activities to be completed outside of class, using [DataCamp](https://www.datacamp.com), for you to practice and learn at your own pace.

Learning Objectives
-------------------

By the end of this course you should be able to:
1. Look at a task and determine if you can or should automate it
2. Create working Python programs
3. Understand the difference between Python object types (e.g. lists, dicts)
4. Perform data analysis and visualization with Python
5. Use git for version control and collaboration
6. Demonstrate your Python skills with a project

Communication
------------

**Before contacting us**, please check to see if your question has already been answered elsewhere, e.g. [StackOverflow](https://stackoverflow.com/).

If you cannot find the answer, please make sure to ask your question thoughtfully (https://stackoverflow.com/help/how-to-ask) and provide everything needed to answer e.g. code, error message, dataset, etc.

In general, please use the [course Slack workspace](https://biof309.slack.com) to communicate with classmates and instructors. If you have a course-relevant question or something to share, Slack is simply better than email. In case of personal/private question/concerns, please use Slack direct message (DM).

In case of an emergency, please send a DM on Slack *and* an email.

Logistics
---------

This is a one-semester course starting on the 13th of September 2018 and finishing on 13th of December 2018.

**Class Location: Rathskeller (Room B1A199C), Building 60, NIH Bethesda campus**

Attendance in class is strongly recommended; however, we realize other commitments may occasionally prevent attendance. If you miss a class, please review the materials available at the course [github repository](https://github.com/marskar/biof309_fall2018) and keep up with activities and homework.

NEW THIS SEMESTER! We will be piloting REMOTE ATTENDANCE and CLASS RECORDINGS via [GoToMeeting](https://www.gotomeet.me/biof309) and [WebEx](https://cbiit.webex.com/join/skarzynskimw). These two options are largely the same, you can pick whichever platform you prefer. Please do **NOT** use this as excuse to skip class and just watch the recorded lectures! This course is **NOT** a Massive Online Open Course (MOOC), it will feature a great deal of group work. Additionally, forming groups to complete the final project is highly encouraged! Remote attendance will work best if you can meet with classmates to work through exercises together. We will do our best to answers questions in the GoToMeeting and WebEx chat windows during class. We will also try to answer all questions on Slack, but please try to ask your questions during class, if at all possible.

Important FAES Fall 2018 semester dates:

* July 9 – September 7: Online Registration.
* September 10 – 28: Late Registration (10 dollar late fee per course applies).
* September 10: Classes begin.
* December 14: Classes end.

Required Materials
------------------

**Each student is encouraged to bring their own laptop to each class.**

*Programing without a computer would be an exceptional feat.*

For the course, you will need
1. The [Anaconda Scientific Python Distribution](https://www.continuum.io/downloads)

The Anaconda installer will automatically install most of the software we will use during the course, including [Jupyter Notebooks](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html).

2. The [PyCharm Integrated Development Environment (IDE)](https://www.jetbrains.com/pycharm/)

The very nice folks at [JetBrains](https://www.jetbrains.com) have given us free licenses for the Professional version of [PyCharm Integrated Development Environment (IDE)](https://www.jetbrains.com/pycharm/), the best (in my humble opinion) Python Integrated Development Environment (IDE).

If you have a .edu email address, please install [PyCharm Integrated Development Environment (IDE)](https://www.jetbrains.com/pycharm/) Professional using [this link](https://www.jetbrains.com/student/).

If not, a installation link will be distributed to you by email and made available on [Slack](https://biof309.slack.com/).

3. A [UNIX-like system](https://en.wikipedia.org/wiki/Unix-like)

If you use Windows 10, please try to set up the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). If you use MacOS or Linux, you are all set.

4. A [DataCamp](https://www.datacamp.com) account

The very nice folks at [DataCamp](https://www.datacamp.com) have given us access to their awesome Data Visualization📊, Machine Learning🤖, and Data Science learning materials.

We will discuss the most interesting examples during class and point out others to be reviewed outside of class.

5. A [PluralSight](https://www.pluralsight.com) account

Thanks to the DataCamp-PluralSight partnership, we can get 6 month access to Web Development, Object-Oriented Programming, and Test-Driven Development learning materials on [PluralSight](https://www.pluralsight.com).

6. A [GitHub](https://github.com/) account

All of the course materials are available on [GitHub](https://github.com/).
Before accessing the [course materials repo](https://github.com/marskar/biof309_fall2018), you should know that
* it is likely to be under constant development throughout the semester and
* you are not expected to work through _everything_ contained therein!

7. [Pandoc](https://pandoc.org/), [RStudio](https://www.rstudio.com/products/rstudio/download/) (and the [R programming language](https://www.rstudio.com/products/rstudio/download/)), or [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)

It is also highly suggest that you avoid the horrors of Microsoft Office.

- Instead of using Microsoft Word & Powerpoint and the doc(x) & ppt(x) formats, write documents and [slideshows](https://marskar.github.io/slides/) in [Markdown](https://www.markdownguide.org/) format and then converted into the desired output format using one of the options below:
> - [Pandoc](https://pandoc.org/)
> - [RStudio](https://www.rstudio.com/products/rstudio/download/) (which requires installing the [R programming language](https://www.rstudio.com/products/rstudio/download/))
> - [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) (or the classic [Jupyter Notebook](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html))
- The document you are reading now is written in [Markdown](https://www.markdownguide.org/)!
- Instructions for how to turn [Markdown](https://www.markdownguide.org/), [R Markdown](https://rmarkdown.rstudio.com/lesson-1.html), and [`ipynb`](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) files into slides are available [here](https://marskar.github.io/slides/).
- Instead of using Microsoft Excel and the xls(x) format, save tabular data as comma-separated value (csv) files. [PyCharm](https://www.jetbrains.com/pycharm/features/), [RStudio](https://www.rstudio.com/products/rstudio/download/) and [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) all have csv viewers. These csv viewers are better options for looking at data than Excel, because they do not have the ability to edit or auto-format your raw data.
- Pro-tip 1: You can write [Markdown](https://www.markdownguide.org/) in [PyCharm](https://www.jetbrains.com/pycharm/features/)! Press Ctrl/Cmd+N, then Enter, type out the name of the [Markdown](https://www.markdownguide.org/) file (must end in `.md`) you want to create, and press Enter again. You get [Markdown](https://www.markdownguide.org/) syntax highlighting and a live preview of your rendered [Markdown](https://www.markdownguide.org/)!
- Pro-tip 2: If you create a new Python scratch file in [PyCharm](https://www.jetbrains.com/pycharm/features/) (Press Ctrl/Cmd+Shift+N, then Enter) and change the extension from `.py` to `.md`, PyCharm will continue to treat the file like a Python script giving you syntax highlighting, code completion, and the ability to run code in your [Markdown](https://www.markdownguide.org/) document! As soon as you take the file out of the Scratches folder, [PyCharm](https://www.jetbrains.com/pycharm/features/) will treat it like a [Markdown](https://www.markdownguide.org/) file again! In short, [PyCharm](https://www.jetbrains.com/pycharm/features/) will auto-detect the file type based on its extension, but this does not apply to scratch files!
- Pro-tip 3: To get automatic python syntax highlighting in your [Markdown](https://www.markdownguide.org/) documents on [GitHub](https://github.com/) and in [slideshows](https://marskar.github.io/slides/) created from [Markdown](https://www.markdownguide.org/) files, put three backticks (\`) followed by the word "python" above your code and then a new line below your code put another three backticks (\`). This is called a [code block](https://pandoc.org/MANUAL.html#fenced-code-blocks) in [Markdown](https://www.markdownguide.org/).
- [Tables that are meant to be displayed in documents](https://www.markdownguide.org/extended-syntax/#tables) should be in [Markdown](https://www.markdownguide.org/) format. For example, the schedule below is a [Markdown](https://www.markdownguide.org/extended-syntax/#tables) table.

Schedule
--------

| #  | Date       | Title                                        | Lead              |
|----|------------|----------------------------------------------|-------------------|
| 1  | 2018-09-13 | Integrated Development Environments          | Martin            |
| 2  | 2018-09-20 | Python Basics                                | All Instructors   |
| 3  | 2018-09-27 | Functions, Modules and Packages              | All Instructors   |
| 4  | 2018-10-04 | Loops and Conditionals                       | Liuping & Michael |
| 5  | 2018-10-11 | Biopython and Sequences                      | Martin            |
| 6  | 2018-10-18 | NumPy and Arrays                             | Liuping & Michael |
| 7  | 2018-10-25 | Pandas and DataFrames                        | Michael           |
| 8  | 2018-11-01 | Machine Learning                             | Martin            |
| 9  | 2018-11-08 | Data Visualization                           | All Instructors   |
| 10 | 2018-11-15 | Web Development                              | Martin            |
| 11 | 2018-11-22 | Comprehensions and Lambdas                   | All Instructors   |
| 12 | 2018-11-29 | Iterators and Generators                     | All Instructors   |
| 13 | 2018-12-06 | Requested Topics/Review/Final Project Clinic | All Instructors   |
| 14 | 2018-12-13 | Student Presentations                        |                   |


Homework
--------

This semester we are continuing our free-from approach to homework assignments. The due dates below are guidelines.
By the end of the semester, you must complete at least one career track or at least two skills tracks on [DataCamp](https://www.datacamp.com/tracks/career). The DataCamp career tracks include the [Python Path on PluralSight](https://www.pluralsight.com/paths/python). Pick DataCamp if you want to focus on *Data Analysis* and *Machine Learning*. Choose Pluralsight if are interested in *Object-Oriented Programming* and *Test-Driven Development*.

This will take 28-67 hours total to complete, depending on which you choose to do.

*DataCamp Career Tracks* (complete at least 1):
- PluralSight Python Path, 30 hours, 8 courses
- DataCamp Python Programmer, 36 hours, 10 courses
- DataCamp Data Analyst with Python, 47 hours, 13 Courses
- DataCamp Data Scientist with Python, 67 hours, 20 Courses

*DataCamp Skills Tracks* (complete at least 2):
- Python Programming, 15 hours, 4 courses
- Importing & Cleaning Data with Python, 13 hours, 4 courses
- Data Manipulation with Python, 16 hours, 4 courses
- Machine Learning, 16 hours, 4 courses

**Please start on your chosen track(s) on DataCamp or PluralSight as soon as possible and work towards the certificate(s) throughout the semester. This will require substantial work! Do not wait until the end of the semester!**

Please use the schedule below as a guide to which DataCamp and PluralSight chapters/lessons correspond to what is covered in class.

01. DUE September 13, 2018 (BEFORE Class)
    - Install [Anaconda Scientific Python Distribution](https://www.continuum.io/downloads)
    - Install [PyCharm](https://www.jetbrains.com/student)

02. DUE September 20, 2018 (BEFORE Class)
    - [Python Basics](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-1-python-basics)
    - [Python: Getting Started](https://www.pluralsight.com/courses/python-getting-started)
    - [Python Fundamentals](https://www.pluralsight.com/courses/python-fundamentals)
    - Chapters 01-05 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
    - Chapter 02 in [Python for Data Analysis](https://github.com/wesm/pydata-book)

03. DUE September 27, 2018 (BEFORE Class)
    - [Python Lists](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists)
    - [Functions and Packages](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-3-functions-and-packages)
    - [Python – Beyond the Basics](https://www.pluralsight.com/courses/python-beyond-basics)
    - Chapter 08 & 13 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
    - Chapter 03 in [Python for Data Analysis](https://github.com/wesm/pydata-book)

04. DUE October 4, 2018 (BEFORE Class)
    - [Loops](https://campus.datacamp.com/courses/intermediate-python-for-data-science/loops)
    - [Logic, Control Flow and Filtering](https://campus.datacamp.com/courses/intermediate-python-for-data-science/logic-control-flow-and-filtering)
    - [The Python Developer's Toolkit](https://www.pluralsight.com/courses/python-developers-toolkit)
    - Chapter 06, 07, & 09 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)

05. DUE October 11, 2018 (BEFORE Class)
    - Biopython TBD
    - Chapter 00-02 in [Biopython-Notebook](https://github.com/tiagoantao/biopython-notebook/tree/master/notebooks)
    - [Unit Testing with Python](https://www.pluralsight.com/courses/unit-testing-python)

06. DUE October 18, 2018 (BEFORE Class)
    - [NumPy](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-4-numpy)
    - Chapter 02 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)
    - Chapter 04 in [Python for Data Analysis](https://github.com/wesm/pydata-book)
    - [Full Stack Web Development with Python (WEB2PY)](https://www.pluralsight.com/courses/full-stack-web-development-python-web2py)
    - [Advanced Python](https://www.pluralsight.com/courses/advanced-python)

07. DUE October 25, 2018 (BEFORE Class)
	- [Dictionaries & Pandas](https://campus.datacamp.com/courses/intermediate-python-for-data-science/dictionaries-pandas)
	- Chapter 03 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)
	- Chapter 05-12 in [Python for Data Analysis](https://github.com/wesm/pydata-book)
	- [Django Fundamentals](https://www.pluralsight.com/courses/django-fundamentals-update)

08. DUE November 1, 2018 (BEFORE Class)
    - [Getting Started with Machine Learning in Python](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/getting-started-with-python)
    - [Predicting with Decision Trees](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/predicting-with-decision-trees)
    - [Improving your Predictions through Random Forests](https://campus.datacamp.com/courses/kaggle-python-tutorial-on-machine-learning/improving-your-predictions-through-random-forests)
    - Chapter 05 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)
    - [Testing Django Applications](https://www.pluralsight.com/courses/testing-django-applications)

09. DUE November 8, 2018 (BEFORE Class)
    - [Introduction to Data Visualization with Python](https://www.datacamp.com/courses/introduction-to-data-visualization-with-python)
    - [Data Visualization with Seaborn](https://www.datacamp.com/courses/data-visualization-with-seaborn)
    - Chapter 04 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)

10. WORK ON FINAL PROJECTS
Depending on your final project, you might find the following topics useful:
	- [Error handling](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/09-Errors-and-Exceptions.ipynb)
	- [Comprehensions](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/10-Iterators.ipynb)
	- [Iterators](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/10-Iterators.ipynb) and [Generators](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/12-Generators.ipynb)
	- [Regular Expressions](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/14-Strings-and-Regular-Expressions.ipynb)

Optional Materials
------------------

[GitHub](https://github.com) is offering some free awesome resources to students, that might be of interest to you, depending on your background: [GitHub student pack](https://education.github.com/pack).


Recommended Books
-----------------
**There is no required textbook for this course.**

We do, however, highly recommend [Python for Data Science](https://github.com/jakevdp/PythonDataScienceHandbook) and its companion text [A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython) by Jake Vanderplas. Both of these books are available free on GitHub in Jupyter Notebook form. The code for [Python for Data Analysis](https://github.com/wesm/pydata-book) by Wes McKinney is also on GitHub but the text is only available in the printed copy of the book. For maximum enjoyment, consider working through the relevant chapters before coming to class.

We will link to relevant online resources throughout the course.

If you would like additional material on the basics, the following resources may be useful:

* [Python for Biologists](http://pythonforbiologists.com/) by Martin Jones.
* [Learn Python the Hard Way (ebook freely available from the author)](http://learnpythonthehardway.org/book/) by Zed A. Shaw; a [video course](http://learnpythonthehardway.org/) is also available.
* [Think Python (ebook freely available from the author)](http://www.greenteapress.com/thinkpython/thinkpython.html) by Allen B. Downey.
* [Python for Everybody: Exploring Data in Python 3 (ebook freely available from the author)](https://www.pythonlearn.com/book.php) by Charles Severance.
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/) by Kenneth Reitz and Tanya Schlusser.
* [Automate the Boring Stuff with Python](www.automatetheboringstuff.com) by Al Sweigart.
* [Introduction to Machine Learning with Python](https://github.com/amueller/introduction_to_ml_with_python) by Andreas Mueller and Sarah Guido.

For more information about Python, please see the official [Python Software Foundation website](https://www.python.org/).

Grading
-----------------------
The emphasis of the course is on learning and mastering the skills covered. We hope that everyone will be able to complete one of the Python tracks on DataCamp or PluralSight and the final project. If some of the material appears unclear, please ask for clarification.

Completion of the Python tracks on DataCamp or PluralSight will be graded in a binary manner (completed/incomplete).

Grading the __final project__ will be done using the following rubric:

* Project description / Specification

  - Goals unclear, difficulty demonstrating functionality (1-3)
  - Goals for the project and functionality are discussed but difficult to follow (4-6)
  - Goals for the project and functionality are discussed (7-9)
  - Goals for the project and functionality are logically presented and clearly communicated (10-12)

* Documentation

  - Only comments embedded in the code (1-3)
  - Objects and methods have docstrings (4-6)
  - Objects and methods have docstrings, additional standalone documentation (7-9)
  - Objects and methods have docstrings, extensive standalone documentation with example usage (10-12)

* Readability
  - The code is poorly organized and very difficult to read (1-3)
  - The code is readable, but challenging to understand (4-6)
  - The code is fairly easy to read (7-9)
  - The code is well organized and very easy to read (10-12)

* Reusability

  - The code is not organized for reusability (1-3)
  - Some parts of the code could be reused (4-6)
  - Most of the code could be reused (7-9)
  - Each part of the code, and the whole, could be reused (10-12)

* Performance

  - Program does not run (1-6)
  - Program runs, but does not produce correct output (7-12)
  - Program runs, produces correct output under most conditions (13-18)
  - Program runs, produces correct output with robust error checking (19-24)

Course Materials
----------------

Course materials are available in the course [GitHub repository](https://github.com/marskar/biof309_fall2018).
