$(document).ready(function(){
    $('input[type="text"]').keyup(function () {
      var spanl = parseInt($('.spanl').val());
      var width = parseInt($('.width').val());
      var pulley = parseInt($('.pulley').val());
      var tq = parseInt($('.tq').val());
              
              var tension = tq / (pulley/2000);
              var freq = Math.sqrt(tension / (width * mass * 4 * ((spanl/1000)^2)));
              $("input#result").val(freq);
    });
    });

    function update(elem) {
      const input = document.getElementById('unit');
      if (elem.value === '1000') {
        input.setAttribute('min', '1');
        input.setAttribute('max', '10');
        input.value /= 1000;
      } else {
        input.setAttribute('min', '1000');
        input.setAttribute('max', '10000');
        input.value *= 1000;
      }
    }