function infrafun(event) {
  var x = document.getElementById(event);
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
