// static/js/partner.js
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("partner-form");
  if (!form) return;

  const nameInput = form.querySelector("input[name='name']");
  const phoneInput = form.querySelector("input[name='phone']");
  const emailInput = form.querySelector("input[name='email']");
  const pinInput = form.querySelector("input[name='pincode']");

  function showError(input, message) {
    let el = input.parentElement.querySelector(".error");
    if (!el) {
      el = document.createElement("div");
      el.className = "error";
      input.parentElement.appendChild(el);
    }
    el.textContent = message;
  }
  function clearError(input) {
    let el = input.parentElement.querySelector(".error");
    if (el) el.remove();
  }

  form.addEventListener("submit", function (e) {
    // client-side quick validation; server will still validate
    let ok = true;

    const nameVal = nameInput.value.trim();
    if (!/^[A-Za-z\s]{3,15}$/.test(nameVal)) {
      showError(nameInput, "Name must be 3-15 letters only.");
      ok = false;
    } else clearError(nameInput);

    const phoneVal = phoneInput.value.trim();
    if (!/^\d{10}$/.test(phoneVal)) {
      showError(phoneInput, "Phone number must be 10 digits.");
      ok = false;
    } else clearError(phoneInput);

    const emailVal = emailInput.value.trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailVal)) {
      showError(emailInput, "Enter a valid email.");
      ok = false;
    } else clearError(emailInput);

    const pinVal = pinInput.value.trim();
    if (!/^\d{6}$/.test(pinVal)) {
      showError(pinInput, "Pin code must be 6 digits.");
      ok = false;
    } else clearError(pinInput);

    if (!ok) {
      e.preventDefault();
      return false;
    }
    // allow natural POST to server (which will send email and return success message)
  });
});
