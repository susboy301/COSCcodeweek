let count = 0;

function updateDisplay() {
  document.getElementById("count").textContent = count;
}

function increment() {
  count++;
  updateDisplay();
}

function decrement() {
  if (count > 0) {
    count--;
    updateDisplay();
  }
}

function resetCount() {
  count = 0;
  updateDisplay();
}
