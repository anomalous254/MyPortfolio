/**
 * code by: anomalous254 | Nyando | am_request
 * github: www.github.com/anomalous254
 */
// Typing effect on home page
var typed = new Typed('.profession-title', {
      strings: ['A Software Engineer','A Mathematician','A Bug Bounty Hunter','A Pentester', 'A Philosopher','A Physicist','A Gamer', 'A Reggae Lover'],
      typeSpeed: 60,
      backSpeed: 90,
      loop: true,
    });
    
// Stats addition block
let values = document.querySelectorAll('.num');
let interval = 100;

values.forEach((value) => {
  let startValue = 0;
  let endValue = parseInt(value.getAttribute("data_val"));
  let duration = Math.floor(interval / endValue);
  console.log(endValue)
  counter = setInterval(function () {
    startValue += 1;
    value.innerText = startValue;
    if (startValue === endValue) {
      clearInterval(counter);
    }
  },duration)

});

// Menu bar toggle logic
function change() {
  console.log('btn clicked')
  $("#small-view").toggle(500);
}