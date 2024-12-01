function checkAnswer(isPhishing) {
  const feedback = document.getElementById('feedback');
  if (isPhishing) {
    feedback.textContent = "Correct! This is a phishing email.";
    feedback.style.color = "green";
  } else {
    feedback.textContent = "Incorrect! Always verify sender details.";
    feedback.style.color = "red";
  }
}
