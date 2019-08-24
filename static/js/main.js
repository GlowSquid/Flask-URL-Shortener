const copyEl = document.querySelector(".btn");
copyEl.addEventListener("click", function() {
  if (copyEl.classList.contains("btn__copy")) {
    copyEl.classList.remove("btn__copy");
    copyEl.classList.add("btn__copied");
    copyEl.textContent = "Copied";
  }

  setTimeout(function() {
    copyEl.textContent = "Copy";
    copyEl.classList.remove("btn__copied");
    copyEl.classList.add("btn__copy");
  }, 2500);
});
