# Browser cookie Flask application

This is a very simple Login Flask application where a user can either sign up or sign in to the website.  
Once a user signs up the username and password are saved to the database, together with their last_access which includes date and time. The homepage is a login screen, see below:

<img width="2181" alt="Login 1" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/2288863e-b613-4492-9c1b-0be5a10b635b">

If a user doesn't have an account and clicks on Sign up, they will be redirected to the Register page:

<img width="2185" alt="Register2" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/dfe6794d-67b7-409a-8c35-0dcad6535dc7">

If the user has already registered before and tries to register again, an error message like the one below will appear:

<img width="2187" alt="Register3" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/1f66c287-e078-4288-b896-28c97d7c2cb8">

However, if it is the first time the user signs up, a session cookie will be issued and the user will be redirected to another page where a confirmation message like the one below will appear:

<img width="2211" alt="Register4" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/aab88f7a-ae79-4d0f-8bd1-9e859bd87d19">

Finally, when the user tries to login with their credentials, the cookie will be read and the user will be redirected to another page where they will be welcomed back:

<img width="2194" alt="Login5" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/529870ef-cae6-4036-b0ed-cfcf4638f3a4">

The manager of the website, on the other hand, after running the program will be able to see the access stats, like the ones below:

Total accesses per user:

![access1](https://github.com/Alex188dot/CorsoPython/assets/117444853/89a04c17-5ae0-420d-be2d-806e8175c959)

Total accesses per user, in percentage:

![access2](https://github.com/Alex188dot/CorsoPython/assets/117444853/277b6eb5-58b4-47b3-b2c3-b4a37532c385)

Accesses to the website per time of the day:

![access3](https://github.com/Alex188dot/CorsoPython/assets/117444853/060cb386-ba00-4872-949a-67cfe9c9b013)

