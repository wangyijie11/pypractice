var page = require('webpage').create();

page.viewportSize = {width: 1024, height: 768};
page.clipRect = {top: 0, left: 0, width: 1024, height: 768};
page.open('http://cuiqingcai.com/', function() {
    page.render('germy.png');
    phantom.exit();
});