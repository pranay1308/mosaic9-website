// Mosaic9 — shared site behaviour
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');

  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
      var expanded = links.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });

    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        links.classList.remove('open');
      });
    });
  }

  // Contact form -> friendly confirmation (static hosting has no backend;
  // replace the form "action" with your Formspree/Web3Forms endpoint to go live)
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      var action = form.getAttribute('action') || '';
      if (action.indexOf('YOUR_FORM_ENDPOINT') !== -1) {
        e.preventDefault();
        var note = document.getElementById('form-status');
        if (note) {
          note.textContent = 'Form endpoint not connected yet — see the note below the form.';
          note.style.color = '#A0334D';
        }
      }
    });
  }
});
