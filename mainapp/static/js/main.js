// Mobile menu toggle
const toggle = document.querySelector('.menu-toggle');
const navList = document.querySelector('.nav-list');

if (toggle) {
    toggle.addEventListener('click', () => {
        navList.classList.toggle('active');
    });
}

// Newsletter form
const form = document.getElementById('newsletter-form');
const emailInput = document.getElementById('newsletter-email');
const msg = document.getElementById('subscribe-message');

if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = emailInput.value.trim();
    const regex = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
    if (regex.test(email)) {
      msg.textContent = "Thanks for subscribing!";
      msg.style.color = "green";
      emailInput.value = "";
    } else {
      msg.textContent = "Please enter a valid email.";
      msg.style.color = "red";
    }
  });
}
