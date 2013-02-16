function harlemshake() {
  function injectCSS() {
    var css = document.createElement("link");
    css.setAttribute("type", "text/css");
    css.setAttribute("rel", "stylesheet");
    css.setAttribute("href", f);
    css.setAttribute("class", addedCSS);
    document.body.appendChild(css)
  }
  function removeAddedCSS() {
    var added = document.getElementsByClassName(addedCSS);
    for (var i = 0; i < added.length; i++) {
      document.body.removeChild(added[i])
    }
  }
  function p() {
    var e = document.createElement("div");
    e.setAttribute("class", a);
    document.body.appendChild(e);
    setTimeout(function () {
      document.body.removeChild(e)
    }, 100)
  }
  function getDimensions(e) {
    return {
      height: e.offsetHeight,
      width: e.offsetWidth
    }
  }
  function fits(i) { //v
    var d = getDimensions(i);
    return d.height > minHeight && d.height < maxHeight && d.width > minWidth && d.width < maxWidth
  }
  function m(e) {
    var t = e;
    var n = 0;
    while ( !! t) {
      n += t.offsetTop;
      t = t.offsetParent
    }
    return n
  }
  function g() {
    var e = document.documentElement;
    if ( !! window.innerWidth) {
      return window.innerHeight
    } else if (e && !isNaN(e.clientHeight)) {
      return e.clientHeight
    }
    return 0
  }
  function y() {
    if (window.pageYOffset) {
      return window.pageYOffset
    }
    return Math.max(document.documentElement.scrollTop, document.body.scrollTop)
  }
  function E(e) {
    var t = m(e);
    return minWidth >= w && minWidth <= b + w
  }
  function playAudio() {
    var audio = document.createElement("audio");
    audio.setAttribute("class", addedCSS);
    audio.src = mp3;
    audio.loop = false;
    audio.addEventListener("canplay", function () {
      setTimeout(function () {
        x(k)
      }, 500);
      setTimeout(function () {
        N();
        p();
        for (var e = 0; e < O.length; e++) {
          T(O[e])
        }
      }, 15500)
    }, true);
    audio.addEventListener("ended", function () {
      N();
      removeAddedCSS()
    }, true);
    audio.innerHTML = " <p>If you are reading this, it is because your browser does not support the audio element. We recommend that you get a new browser.</p> <p>";
    document.body.appendChild(audio);
    audio.play()
  }
  function x(e) {
    e.className += " " + s + " " + o
  }
  function T(e) {
    e.className += " " + s + " " + effects[Math.floor(Math.random() * effects.length)]
  }
  function N() {
    var e = document.getElementsByClassName(s);
    var t = new RegExp("\\b" + s + "\\b");
    for (var n = 0; n < e.length;) {
      e[n].className = e[n].className.replace(t, "")
    }
  }
  var minHeight = 0;
  var minWidth = 0;
  var maxHeight = 3500;
  var maxWidth = 3500;
  var mp3 = "//s3.amazonaws.com/moovweb-marketing/playground/harlem-shake.mp3"; //"harlemshake.mp3";
  var s = "mw-harlem_shake_me";
  var o = "im_first"; // first
  var effects = ["im_drunk", "im_baked", "im_trippin", "im_blown"]; //effects
  var a = "mw-strobe_light";
  var f = "//s3.amazonaws.com/moovweb-marketing/playground/harlem-shake-style.css"; //"harlemshake.css";
  var addedCSS = "mw_added_css";
  var b = g();
  var w = y();
  var C = document.getElementsByTagName("*");
  var k = null;
  for (var L = 0; L < C.length; L++) {
    var A = C[L];
    k = document.getElementById('dance-baby');
    // if (fits(A)) {
    //   if (E(A)) {
    //     k = A;
    //     break
    //   }
    // }
  }
  if (A === null) {
    console.warn("Could not find a node of the right size. Please try a different page.");
    return
  }
  injectCSS();
  playAudio();
  var O = [];
  for (var L = 0; L < C.length; L++) {
    var A = C[L];
    if (fits(A)) {
      O.push(A)
    }
  }
}
