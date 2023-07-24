# Extra Credit: Design Patterns in Javascript

## Introduction

In this activity, you will gain familiarity with the Javascript language and some common design patterns in code. It is likely you already have some experience with many of the patterns we will practice (even if you don't realize it), but this activity will help clarify why certain methods are used and how they can be applied to your own code.

This activity focuses on Creational Design Patterns, specifically the Builder, Factory, and Prototype patterns. These are ways to create new objects that will allow greater flexibility and customization in how your codebase uses them. Pay close attention to the documentation, as it will be key to understanding the purpose of each pattern.

At this point, whether you believe it, you are increasing your ability to pick up new languages and technologies. This process gets easier as you gain experience, and this activity will serve as great practice. If you are unfamiliar with Javascript, you may want to take a look at the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript) for a good introduction resource. But we would like to encourage you to try completing this activity with a different method. Instead of finding external lesson plans to teach yourself the language, try going through the activities, reading the comments very carefully, and attempting to mimic the code you see to build your own solutions. When you get stuck, look for helpful information online, consult your peers, or ask your instructor or TAs for help. This is, in many people's opinions, te best way to learn something new.

## Task 1: Builder Pattern

The builder pattern is one you have likely used before, as it is one that works quite well with most language's ownership rules for objects. In this patter, we create methods that allow us to build an object in a step-by-step fashion. This is useful when we want an object to fulfill many different roles, but we don't want to create a lengthy, complicated inheritance chain.

- Navigate to the `builder` folder and open the `script.js` file.
- Read the initial `Student` and `StudentBuilder` classes.
- Finish `TODO 1` by adding the following getter methods to the `Student` class:
  - `getMajor()`: returns the student's major
  - `getGPA()`: returns the student's GPA
  - `getDescription()`: returns a the student description string
  - `getFullName()`: returns the student's full name, no spaces between first and last name
- Finish `TODO 2` by adding the following setter methods to the `StudentBuilder` class:
  - `setMajor(major)`: sets the student's major
  - `setGPA(gpa)`: sets the student's GPA
  - `setDescription(description)`: sets the student's description
- Read the `writeStudentHeader()` function and its documentation very carefully. Look at what it is doing to write HTML elements to the page.
- Finish `TODO 3` by writing the following functions:
  - `writeStudentInfo(major, gpa) { ... }`: this function should write the student's major and GPA to the page.
    - create a div element with the class `student-info`
    - create an unordered list element
    - create a list item element for the major and gpa
    - append the list items to the unordered list
    - append the unordered list to the div
    - return the div
  - `writeStudent(student) { ... }`: this function should write all of the student's information to a div element and return it.
    - create a div element with the class `student`
    - call and append the values of all of the `writeStudent*()` functions to the div
    - return the div
- Finish `TODO 4` by replacing the default information in the `buildPage()` function with your own or some imaginary student's information.
- Finish `TODO 5` by adding your own custom style to the page in the `style.css` file.

## Task 2: Factory Pattern

The factory pattern is similar to the builder pattern, but instead of having direct control over the specific methods that distinguish the objects we create, we instead create a factory that is able to make different types of objects that represent common roles these objects will play in our code. This is useful when we want to create many different objects that share a common set of properties that we already know, but again want to avoid that complex inheritance chain.

- Navigate to the `factory` folder and open the `script.js` file.
- Read the `Worker` and `WorkerFactory` classes and their documentation carefully.
- Finish `TODO 6` by adding the following getter methods to the `Worker` class:
  - `getName()`: returns the worker's name
  - `getTitle()`: returns the worker's title
  - `getSalary()`: returns the worker's salary
- Finish `TODO 7` by adding the following create methods to the `WorkerFactory` class
  - `createCashier(name)`: returns a new `Worker` object with the name given, a title of "Cashier", and a salary random fluctionation stemming from the base value of 55000
  - `createManager(name)`: returns a new `Worker` object with the name given, a title of "Manager", and a salary with a random fluctionation stemming from the base value of 55000
- Read through the `showEmployees()` function and its documentation carefully.
- Finish `TODO 8` by creating elements for the `name`, `title`, and `salary` table headers, setting their text to the appropriate values, and appending them to the `row` element.
- Finish `TODO 9` by creating elements for the `name`, `title`, and `salary` table data, setting their text to the appropriate values, and appending them to the `row` element.
- Finish `TODO 10` by adding your own custom style to the page in the `style.css` file.

## Task 3: Prototype

The prototype pattern is one that is used to create new objects based on existing objects, and Javascript has a built-in method that will allow us to append new properties and methods to an existing object. This is again useful for avoiding unecessary inheritance confusion, but this also allows for a deeper, memory-efficient way to create new objects, extending the ones we already have.

- Navigate to the `prototype` folder and open the `script.js` file.
- Read the first function and its documentation. This function will be used to create new objects that will be used in the prototype pattern.
- Finish `TODO 11` by creating the following methods and using prototype syntax to add them to the `AnyNumber` object.
  - `getImaginary()`: returns the imaginary number
  - `setImaginary(num)`: sets the imaginary number
  - `add(c)`: takes in another `AnyNumber` object and returns a new `AnyNumber` object with the real and imaginary numbers added together
    - **TIP**: you need to add the real and imaginary numbers of the two objects together
  - `magnitude()`: returns the magnitude of the number
    - **TIP**: the formula for this is `sqrt(real^2 + imaginary^2)`
- Carefully read through the entire `script.js` file and its documentation.
- Finish `TODO 12` by adding the following functions to your code. Note that all of these functions must also have a keybinding assigned to them in the `eventHandler` function.
  - `increaseC()`: adds 0.1 to the real number of `c`, which is a global variable, then calls the `reload()` function
  - `decreaseC()`: subtracts 0.1 from the real number of `c`, then calls the `reload()` function
  - `increaseCI()`: adds 0.1 to the imaginary number of `c`, then calls the `reload()` function
  - `decreaseCI()`: subtracts 0.1 from the imaginary number of `c`, then calls the `reload()` function
  - `changeC()`: sets the real and imaginary numbers of `c` to random values between -2 and 2, then calls the `reload()` function
  - `randomizeColorPalette()`: uses the `makeRandomPalette()` function to create a new color palette and sets the global `paletteOptions` list to only include the new palette., then calls the `reload()` function
    - **TIP**: add a key binding for the `reloadColorPalette()` function too so that you are not stuck with the random palette you just created.
  - `increaseMaxIterations()`: doubles the current `maxIterations` value so long as it is less 25600, then calls the `reload()` function
  - `decreaseMaxIterations()`: halves the current `maxIterations` value so long as it is greater than 25, then calls the `reload()` function
  - `zoomIn()`: subtracts 0.5 from the xMin and yMin values, adds 0.5 to the xMax and yMax values, then calls the `reload()` function
  - `zoomOut()`: adds 0.5 to the xMin and yMin values, subtracts 0.5 from the xMax and yMax values, then calls the `reload()` function
  - `increaseBreakPoint()`: doubles the current `breakPoint` , then calls the `reload()` function
  - `decreaseBreakPoint()`: halves the current `breakPoint` , then calls the `reload()` function

## Submission Details

- On Canvas, submit the following:
  - The URL to your GitHub repository, with the latest version of your code pushed to the `main` branch.
  - Make sure that the TAs have been included as collaborators on your repository.
