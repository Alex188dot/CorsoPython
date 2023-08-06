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
