<script>
function encode() {
  var t = input.value;
  if (/^[-.]+$/.test(t)) {
    alert("Your text is already e'coded!");
  } else {
    input.value = _encode(t);
  }
  return false;
}

function decode() {
  var t = input.value;
  if (/^[-.]*$/.test(t)) {
    input.value = _decode(t);
  } else {
    alert("Your text is not e'coded!");
  }
  return false;
}

function _encode(input) {
  var a=[];
  for (var i=0; i<input.length; i++) {
    var t = input.charCodeAt(i);
    for (var j=0; j<8; j++) {
      if ((t >> j) & 1) {
        a.push(1 + j + (input.length - 1 - i) * 8);
      }
    }
  }

  var b = [];
  while (a.length) {
    var t = (Math.random() * a.length)|0;
    b.push(a[t]);
    a = a.slice(0, t).concat(a.slice(t+1));
  }

  var r = '';
  while (b.length) {
    var t = b.pop();
    r = r + "-".repeat(t) + ".";
  }
  return r;
}

// Everything below this line was lost due to cosmis radiation. The engineer who knows
// where the backups are stored already left.
function _decode(input) {
  return "";
}
</script>
