  var typed = new Typed(".typing", {
    strings: ["Machine Learning Engineer", "Full Stack Developer", "Backend Developer"],
    typeSpeed: 100,
    backSpeed: 60,
    loop: true
  });

  document.getElementById("hueSlider").addEventListener("input", function () {
  document.documentElement.style.setProperty("--hue-color", this.value);
});