const close_x = document.querySelector("#close_x");
const nav_list = document.querySelector("#nav-links");
const nav_bg = document.querySelector("#nav-bg");
const nav_inner = document.querySelector("#nav-inner");
const cart = document.querySelector("#nav-cart");

const toggleBurgerMenu = () => {
  if (nav_list.classList.contains("hidden")) {
    nav_list.classList.remove("hidden");
    close_x.src = "/static/images/close_x.svg";
    cart.classList.add("hidden");
    nav_inner.classList.remove("justify-between");
    nav_inner.classList.add("flex-col");
    nav_bg.classList.add("pb-[7em]");
  } else {
    nav_list.classList.add("hidden");
    nav_bg.classList.remove("pb-[7em]");
    close_x.src = "/static/images/burger-icon.svg";
    cart.classList.remove("hidden");
    nav_inner.classList.remove("flex-col");
    nav_inner.classList.add("justify-between");
  }
};

close_x.addEventListener("click", toggleBurgerMenu);

console.log(close_x);
