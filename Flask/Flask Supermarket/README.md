# Flask Supermarket

This project is a Flask Application that makes use of both the Front End (to get the data from the users) and the Backend
(to save the data, for validation and statistical purposes).

Below I will illustrate how this application works. On the homepage the user is prompted to either register or login. Let's start with Register:

<img width="2216" alt="register" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/e04c054f-208e-4c9c-9899-cc72a8722653">

The program will set a cookie on the user's browser so that when they are logged in the site will recognize the username, the email and the last time they accessed the site.  

Once successfully registered, the user will be redirected to the login page, where they will be able to login with the credentials previously created:

<img width="2221" alt="login" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/eb2f9979-7861-4b16-8fa4-a3f774961817">

On successful login the user will be able to select the products they want for their groceries, among packaged, fresh and refrigerated products and/or appliances:

<img width="2221" alt="choose products" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/2e08ca1d-296b-47f4-8a73-535c2f1f3d0d">

It is important to note that the user can also leave any of these select options blank, as they are not all mandatory. The user will then be directed to an order recap webpage:  

<img width="2216" alt="order confirmation" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/fefd0124-527b-4814-8fa0-bf3e50c2c6f6">

And will also receive an automated confirmation email:

<img width="1903" alt="email-confirmation" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/84b675e2-43a3-479a-a739-f95be3d3b413">

The Manager on the other hand, by clicking on the top right link on the Navbar (Area Riservata), will reach this staff login screen:

<img width="2216" alt="Admin login" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/0b9325ae-8fb4-456c-b757-606f3c1a502e">

By logging in with their credentials, they will be able to see the revenue of the current day (updated automatically):

<img width="505" alt="revenue-stats" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/7bd1c516-4168-4589-969f-a61ff2882368">

The amount of purchases per hour of the day (between 9 and 22):

![purchases_per_hour_linegraph](https://github.com/Alex188dot/CorsoPython/assets/117444853/4c23e7b5-4a5a-4cbe-9119-d37638ec8b48)

The purchases per hour, in percentage, in the form of a pie chart: 

![purchases_per_hour_piechart](https://github.com/Alex188dot/CorsoPython/assets/117444853/954f1c63-4012-4312-990d-dc5791606788)


