// Light/Dark Theme section

const btn = document.querySelector(".btn-toggle");
let isBlackLime = false;

btn.addEventListener("click", function () {
  const elements = document.querySelectorAll("*");
  const navbar = document.querySelector("#navbar");
  const navbarNav = document.querySelector("#navbarNav");
  const navbarBrand = document.querySelector(".navbar-brand");
  const navItem = document.querySelectorAll(".nav-item");
  const navLink = document.querySelectorAll(".nav-link");
  const container = document.querySelectorAll(".container");
  const image = document.querySelector(".img-fluid");
  const par = document.querySelectorAll(".p");
  const cards = document.querySelectorAll(".card-body");
  const cardTitle = document.querySelectorAll(".card-title");
  const cardText = document.querySelectorAll(".card-text");
  const btnContainer = document.querySelectorAll(".btn-container");
  const btnText = document.querySelectorAll(".btn-container *");
  const btnHoverElements = document.querySelectorAll(".btn");
  const accordionBody = document.querySelectorAll(".accordion-body");
  const socials = document.querySelectorAll(".social-links");
  const email = document.querySelector(".email");
  const linkedin = document.querySelector(".linkedin");
  const github = document.querySelector(".github");

  if (isBlackLime) {
    // If it is Black and Lime, change it to the Original theme
    for (let element of elements) {
      element.style.backgroundColor = "";
      element.style.color = "";
    }
    // Image
    image.src = "Assets/Alessio_Leodori_logo.png";
    btn.title = "Dark mode";

    isBlackLime = false;
  } else {
    // If it is not Black and Lime, change it to Black and Lime theme
    for (let element of elements) {
      element.style.backgroundColor = "#171810";
      element.style.color = "#00F26B";
    }
    // Navbar
    navbar.style.backgroundColor = "#2f2e2e";
    navbarNav.style.backgroundColor = "#2f2e2e";
    navbarBrand.style.backgroundColor = "#2f2e2e";
    for (let n of navItem) {
      n.style.backgroundColor = "#2f2e2e";
    }
    for (let n of navLink) {
      n.style.backgroundColor = "#2f2e2e";
    }
    // Navbar Brand and Nav Links hover effect
    function mouseEnter() {
      this.style.color = "rgb(220, 255, 17)";
    }
    navbarBrand.addEventListener("mouseenter", mouseEnter);
    function mouseLeave() {
      this.style.color = "#00F26B";
    }
    navbarBrand.addEventListener("mouseleave", mouseLeave);
    navLink.forEach(function (n) {
      n.addEventListener("mouseenter", mouseEnter);
      n.addEventListener("mouseleave", mouseLeave);
    });
    function removeEventListeners() {
      navLink.forEach(function (n) {
        n.removeEventListener("mouseenter", mouseEnter);
        n.removeEventListener("mouseleave", mouseLeave);
      });
    }
    btn.addEventListener("click", function () {
      removeEventListeners();
      navbarBrand.removeEventListener("mouseenter", mouseEnter);
      navbarBrand.removeEventListener("mouseleave", mouseLeave);
    });
    // Btn hover effect
    btn.addEventListener("mouseenter", mouseEnter);
    btn.addEventListener("mouseleave", mouseLeave);
    btn.addEventListener("click", function () {
      btn.removeEventListener("mouseenter", mouseEnter);
      btn.removeEventListener("mouseleave", mouseLeave);
    });
    // Containers
    for (let cont of container) {
      cont.style.backgroundColor = "#2f2e2e";
    }
    for (let p of par) {
      p.style.backgroundColor = "#2f2e2e";
    }
    // Image
    image.src = "Assets/Alessio_Leodori_Logo_Black.png";
    // Cards
    for (let card of cards) {
      card.style.backgroundColor = "#2f2e2e";
    }
    for (let cardT of cardTitle) {
      cardT.style.backgroundColor = "";
    }
    for (let card of cardText) {
      card.style.backgroundColor = "";
    }
    for (let btn of btnContainer) {
      btn.style.backgroundColor = "";
    }
    for (let b of btnText) {
      b.style.backgroundColor = "#00F26B";
      b.style.color = "#2f2e2e";
    }
    // Buttons hover effect
    function handleMouseEnter() {
      this.style.backgroundColor = "#171810";
      this.style.color = "white";
    }
    function handleMouseLeave() {
      this.style.backgroundColor = "#00F26B";
      this.style.color = "#2f2e2e";
    }
    btnHoverElements.forEach(function (btnHover) {
      btnHover.addEventListener("mouseenter", handleMouseEnter);
      btnHover.addEventListener("mouseleave", handleMouseLeave);
    });
    function removeHoverEventListeners() {
      btnHoverElements.forEach(function (btnHover) {
        btnHover.removeEventListener("mouseenter", handleMouseEnter);
        btnHover.removeEventListener("mouseleave", handleMouseLeave);
      });
    }
    btn.addEventListener("click", function () {
      removeHoverEventListeners();
    });
    // Accordion
    for (acc of accordionBody) {
      acc.style.backgroundColor = "#2f2e2e";
    }
    // Socials
    for (let s of socials) {
      s.style.color = "white";
    }

    email.style.color = "white";
    linkedin.style.color = "white";
    github.style.color = "white";

    btn.title = "Light mode";
    isBlackLime = true;
  }
});

// Italian/English Language section

const lang = document.querySelector("#language");

let isItalian = false;

lang.addEventListener("click", function () {
  const nav1 = document.querySelector("#nav1");
  const nav2 = document.querySelector("#nav2");
  const nav3 = document.querySelector("#nav3");
  const nav4 = document.querySelector("#nav4");
  const jumbo = document.querySelector("#jumbo-section");
  const programs = document.querySelector(".programs");
  const fullStack = document.querySelector(".full-stack");
  const personalProjects = document.querySelector(".personal-projects");
  const contactMe = document.querySelector("#contact-title");
  const card1 = document.querySelector("#card1");
  const card8 = document.querySelector("#card8");
  const card9 = document.querySelector("#card9");
  const card10 = document.querySelector("#card10");
  const card11 = document.querySelector("#card11");
  const card12 = document.querySelector("#card12");
  const card13 = document.querySelector("#card13");
  const card14 = document.querySelector("#card14");
  const card15 = document.querySelector("#card15");
  const cardText1 = document.querySelector("#card-text1");
  const cardText2 = document.querySelector("#card-text2");
  const cardText3 = document.querySelector("#card-text3");
  const cardText4 = document.querySelector("#card-text4");
  const cardText11 = document.querySelector("#card-text11");
  const cardText12 = document.querySelector("#card-text12");
  const cardText13 = document.querySelector("#card-text13");
  const cardText14 = document.querySelector("#card-text14");
  const cardText15 = document.querySelector("#card-text15");
  const cardText16 = document.querySelector("#card-text16");
  const cardText17 = document.querySelector("#card-text17");
  const cardText18 = document.querySelector("#card-text18");
  const cardText19 = document.querySelector("#card-text19");
  const cardText20 = document.querySelector("#card-text20");
  const cardText21 = document.querySelector("#card-text21");
  const cardText22 = document.querySelector("#card-text22");
  const cardText23 = document.querySelector("#card-text23");
  const cardText24 = document.querySelector("#card-text24");
  const cardBtn = document.querySelectorAll(".btn");
  const accordionB1 = document.querySelector("#accordion-button-one");
  const accordionB2 = document.querySelector("#accordion-button-two");
  const accordionB3 = document.querySelector("#accordion-button-three");
  const accordionB4 = document.querySelector("#accordion-button-four");
  const accordionB5 = document.querySelector("#accordion-button-five");
  const accordionBody1 = document.querySelector("#accordion-body-one");
  const accordionBody2 = document.querySelector("#accordion-body-two");
  const accordionBody3 = document.querySelector("#accordion-body-three");
  const accordionBody4 = document.querySelector("#accordion-body-four");
  const accordionBody5 = document.querySelector("#accordion-body-five");
  const contactTitle = document.querySelector("#contact-title");
  const contactText1 = document.querySelector("#contact-text1");
  const contactText2 = document.querySelector("#contact-text2");
  const contactText3 = document.querySelector("#contact-text3");
  const linkedinIcon = document.querySelector(".fa-linkedin");
  const githubIcon = document.querySelector(".fa-github");

  let elems = document.querySelectorAll("[data-original-text]");

  if (isItalian) {
    // If language is Italian, change it to the Original language
    elems.forEach(function (elem) {
      elem.textContent = elem.getAttribute("data-original-text");
    });
    cardBtn.forEach((card) => (card.textContent = "Learn more"));
    let email = document.createElement("a");
    email.setAttribute("href", "mailto:alessio.leodori@gmail.com");
    email.setAttribute("target", "_blank");
    email.textContent = "email ";
    email.classList.add("email");
    let linkedin = document.createElement("a");
    linkedin.setAttribute(
      "href",
      "https://www.linkedin.com/in/alessio-leodori-a04276280/"
    );
    linkedin.classList.add("linkedin");
    linkedin.setAttribute("target", "_blank");
    let or = document.createElement("span");
    or.textContent = "or via ";
    linkedin.textContent = "Linkedin ";
    contactText2.textContent =
      "Feel free to contact me either by sending me an ";
    contactText2.appendChild(email);
    contactText2.appendChild(or);
    contactText2.appendChild(linkedin);
    contactText2.appendChild(linkedinIcon);
    contactText3.textContent = "You can also check out my ";
    let github = document.createElement("a");
    github.setAttribute("href", "https://github.com/Alex188dot");
    github.setAttribute("target", "_blank");
    github.textContent = "Github ";
    github.classList.add("github");
    contactText3.appendChild(github);
    contactText3.appendChild(githubIcon);

    if (isBlackLime) {
      email.style.color = "white";
      linkedin.style.color = "white";
      github.style.color = "white";
    }

    lang.src = "Assets/italy.png";
    lang.alt = "italian";
    lang.title = "Italian";
    isItalian = false;
  } else {
    // If language is not Italian, change it to Italian
    nav1.textContent = "Programmi";
    nav2.textContent = "App Full Stack";
    nav3.textContent = "Progetti Personali";
    nav4.textContent = "Contatti";
    jumbo.textContent = `Benvenuti nel mio portfolio! Mi chiamo Alessio e sono un Full 
    Stack Developer bilingue. Ho una passione per l'apprendimento e per la programmazione di App che hanno un look moderno. Il mio Tech Stack comprende: HTML, CSS, Javascript, MongoDB, ExpressJS, React, NodeJS, PHP, Java e Python. Nella mia carriera ho svolto diverse professioni e mansioni, che mi hanno fornito preziose competenze in ambito di 
    problem solving e comunicazione. Sono sicuro di poter
    applicare queste competenze a qualsiasi progetto di programmazione e fornire risultati di alta qualità. In generale, sono sempre aperto a nuove sfide e alla possibilità di imparare dagli altri.`;
    programs.textContent = "Programmi";
    fullStack.textContent = "App Full Stack";
    personalProjects.textContent = "Progetti Personali";
    contactMe.textContent = "Contatti";
    card1.textContent = "Clone di Netflix";
    card8.textContent = "Ristorante con Grafica";
    card9.textContent = "Autosalone";
    card10.textContent = "Distributore";
    card11.textContent = "Crittografia";
    card12.textContent = "Scuola di Formazione";
    card13.textContent = "Supermercato Flask";
    card14.textContent = "Generatore di QR Code";
    card15.textContent = "App Meteo";
    cardText1.textContent = "Una pagina che riproduce la homepage di Netflix";
    cardText2.textContent =
      "Un sito di un'agenzia di viaggi completamente responsive";
    cardText3.textContent =
      "Un portale per la ricerca di lavoro, con capacità di filtro";
    cardText4.textContent = "Una landing page di una Pizzeria creata con React";
    cardText11.textContent =
      "Un programma di gestione di un ristorante creato con Tkinter";
    cardText12.textContent =
      "Un programma di gestione di un autosalone creato con Tkinter";
    cardText13.textContent = "Un programma di Slot Machine creato con Tkinter";
    cardText14.textContent = "Un distributore automatico con grafica";
    cardText15.textContent = "Un programma di codifica crittografica";
    cardText16.textContent = "Un programma di simulazione di una blockchain";
    cardText17.textContent = "Una web app per un negozio di elettronica online";
    cardText18.textContent = "Una scuola di formazione costruita con Django";
    cardText19.textContent =
      "Un'app di gestione ristorante costruita con Flask";
    cardText20.textContent =
      "Un'app di gestione supermercato costruita con Flask";
    cardText21.textContent = "Uno script Python per la generazione di QR code";
    cardText22.textContent =
      "Uno script Python per lo scraping di link da un sito web";
    cardText23.textContent =
      "Uno script Python per la sentiment analysis di articoli";
    cardText24.textContent = "Un'app Meteo costruita con Tkinter";
    cardBtn.forEach((card) => (card.textContent = "Scopri di più"));
    accordionB1.textContent = "Quali linguaggi e framework utilizzi?";
    accordionB2.textContent = "Qual è il tuo linguaggio preferito?";
    accordionB3.textContent =
      "Perchè hai scelto la programmazione e di diventare uno sviluppatore?";
    accordionB4.textContent =
      "Sei interessato a qualche altra area della programmazione?";
    accordionB5.textContent = "Di che cos'altro sei appassionato?";
    accordionBody1.textContent =
      "Utilizzo Python, Javascript, HTML e CSS ogni giorno. Per quanto riguarda framework e librerie utilizzo React, Flask oppure Django e Bootstrap.";
    accordionBody2.textContent =
      "Python di gran lunga! Adoro la sua semplicità e flessibilità.";
    accordionBody3.textContent =
      "Sono sempre stato interessato alla tecnologia in generale, ma pensavo che siccome non avevo studiato Informatica all'università questa carriera per me non fosse possibile. Invece, poi ho scoperto che sia frequentando corsi in materia, che studiando per conto mio, diventare programmatore è assolutamente possibile!";
    accordionBody4.textContent =
      "Si, sono interessato alla Data Science e all'intelligenza artificiale. Sono affascianto dal modo in cui questi modelli  funzionano ed in particolare da come riescono a prevedere eventi futuri.";
    accordionBody5.textContent =
      "Sono interessato alle criptovalute e alla blockchain, sia per l'utilità che un giorno questa tecnologia potrà apportare, sia per il suo potenziale di crescita.";
    contactTitle.textContent = "Contatti";
    contactText1.textContent =
      "Hai trovato il mio portfolio interessante e vorresti saperne di più. Qual è il prossimo passo?";
    // Contact Text 2
    let email = document.createElement("a");
    email.setAttribute("href", "mailto:alessio.leodori@gmail.com");
    email.setAttribute("target", "_blank");
    email.textContent = "email ";
    email.classList.add("email");
    let linkedin = document.createElement("a");
    linkedin.setAttribute(
      "href",
      "https://www.linkedin.com/in/alessio-leodori-a04276280/"
    );
    linkedin.setAttribute("target", "_blank");
    let or = document.createElement("span");
    or.textContent = "o ";
    linkedin.textContent = "Linkedin ";
    linkedin.classList.add("linkedin");
    contactText2.textContent = "Sentiti libero di contattarmi tramite ";
    contactText2.appendChild(email);
    contactText2.appendChild(or);
    contactText2.appendChild(linkedin);
    contactText2.appendChild(linkedinIcon);
    // Contact Text 3
    let github = document.createElement("a");
    github.setAttribute("href", "https://github.com/Alex188dot");
    github.setAttribute("target", "_blank");
    github.textContent = "Github ";
    github.classList.add("github");
    contactText3.textContent = "Dai un'occhiata alla mia pagina ";
    contactText3.appendChild(github);
    contactText3.appendChild(githubIcon);

    if (isBlackLime) {
      email.style.color = "white";
      linkedin.style.color = "white";
      github.style.color = "white";
    }
    lang.src = "Assets/united-kingdom.png";
    lang.alt = "english";
    lang.title = "English";
    isItalian = true;
  }
});
