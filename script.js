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
  const btnText = document.querySelectorAll(".btn-container a");
  const btnHoverElements = document.querySelectorAll(".btn");
  const accordionBody = document.querySelectorAll(".accordion-body");
  const socials = document.querySelectorAll(".social-links");

  if (isBlackLime) {
    // If it is Black and Lime, change it to the Original theme
    for (let element of elements) {
      element.style.backgroundColor = "";
      element.style.color = "";
    }
    // Image
    image.src = "Alessio_Leodori_logo.png";
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
    image.src = "Alessio_Leodori_Logo_Black.png";
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
    // Contact me
    for (let s of socials) {
      s.style.color = "white";
    }
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
  const card1 = document.querySelector("#card1");
  const card2 = document.querySelector("#card2");
  const card3 = document.querySelector("#card3");
  const card4 = document.querySelector("#card4");
  const card5 = document.querySelector("#card5");
  const card6 = document.querySelector("#card6");
  const card7 = document.querySelector("#card7");
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
  const cardText5 = document.querySelector("#card-text5");
  const cardText6 = document.querySelector("#card-text6");
  const cardText7 = document.querySelector("#card-text7");
  const cardText8 = document.querySelector("#card-text8");
  const cardText9 = document.querySelector("#card-text9");
  const cardText10 = document.querySelector("#card-text10");
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
  const contact = document.querySelector("#contact");
  const contactTitle = document.querySelector("#contact-title");
  const contactText1 = document.querySelector("#contact-text1");
  const contactText2 = document.querySelector("#contact-text2");
  const contactText3 = document.querySelector("#contact-text3");
});
