// const form = document.querySelector('#form');



document.getElementById('phone').addEventListener('blur', function(e) {
    var phone = e.target.value.replace(/\D/g, '');
    var match = phone.match(/^(\d{2})(\d{9})$/);
    if (match) {
      e.target.value = '(' + match[1] + ') ' + match[2];
    }
  });
