# La Bella Roma - Restaurant

This project is a Flask Application that makes use of both the Front End (to get the data from the users) and the Backend   
(to register the data and send data to the Admin area to accept/reject orders and for statistics purposes).     

Below I will illustrate how this application works. The customer is prompted to enter their email address and the dishes they want to choose:

<img width="2235" alt="menu-select" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/02c1f5ae-c5b6-40e5-b297-3a04e8d576aa">

Once they have chosen, they will see a recap of their order and they will be told that they will receive a confirmation email shortly.   

<img width="2231" alt="menu-confirmation" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/1c3a0bef-36af-42ba-b1a5-7d59f882f78f">

At this point the Manager, who logs in through the top right link in the navbar, and who has their own credentials:

<img width="2223" alt="admin_login" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/8d24b615-e2c6-454c-a955-9098d7dccfad">

will be able to accept or reject the order. 

![admin-accept-reject-order](https://github.com/Alex188dot/CorsoPython/assets/117444853/77501091-24d0-4ea3-b95a-f8e45be52411)

If they accept the order, the customer will receive an email like the one below:  

<img width="1850" alt="email-body" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/bbf8b3bd-7418-42b2-9262-97a9e4e00cbe">

If they reject the order, the customer will receive another email:   

<img width="1843" alt="rejected order" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/1dd8f363-5816-4938-af03-292ce532fdcf">

Additionally the Manager, by clicking on the "Statistiche" button, will be able to see up-to-date stats on how the business is doing: i.e. Revenue and Sales per dish, in percentage:

<img width="1177" alt="stats1" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/55b55518-09d8-46ff-b955-6a441d49e314">

Sales per dish, in €:

<img width="1131" alt="stats2" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/307b36ce-36de-4412-9553-febf943639b2">

Sales per dish in percentage, divided by category, in order to immediately identify the best-selling products: 

<img width="1120" alt="stats3" src="https://github.com/Alex188dot/CorsoPython/assets/117444853/1ef9ba9b-e3ad-48e0-bdbf-ccbfe2c4f915">
