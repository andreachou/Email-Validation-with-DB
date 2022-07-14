# Email Validation with DB

## Coding Dojo Practice 07.12.2022

<br/>

Learning Objectives:
- Students will read from and insert into a database.
- Students will validate user input before adding it to the database.
- Students will use regex.
- Students will implement flash messages.
- Students will redirect the user after going to a POST route.
- Students will evaluate the need for front-end versus back-end validations.

<br/>

Create an application that asks a user to enter an email address and validates it.

![sample](./practice%20sample.gif)

<br/>

**index.html**

A simple form for the user to submit an email.

![index page](./index%20page.png)



**Error**

If the email address is not valid, have a notification "Email is not valid!" to display on the homepage.

![error](./error%20message.png)


**success.html**

Once a valid email address is entered, save to the database the email address the user entered. On the success page, display all the email addresses entered along with the date and the time when the email addresses were entered.

![success message](./success%20message.png)


<br/>

## Step

Create a new Flask project

Create a new database with a table containing an email address field

Set up the root route to display a form to input an email address

Validate that the email is in the correct format

If invalid, redirect to the root route with an error message

If valid, redirect to the success route that displays a success message

Have the success route template also display a list of all the email's in the database

NINJA Bonus: Also validate that the email being added is unique

NINJA Bonus: Add a delete button on the success route allowing for the deletion of a specific email from the database