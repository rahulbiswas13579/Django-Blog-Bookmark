alert('loaded');
(function () {
  if (window.myBookmarklet !== undefined) {
    alert('executed');
    myBookmarklet();
  } else {
    alert('transfered');
    document.body.appendChild(document.createElement("script")).src="http://www.joshuawhaley.com/bookmarklet bookmarklet.js?r=" + Math.floor(Math.random() * 99999999999999999999);
  }
});

(function(){
    var jquery_version = '2.1.4';
    var site_url = 'http://127.0.0.1:8000/';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;
    function bookmarklet(msg) {
    // Here goes our bookmarklet code
    };