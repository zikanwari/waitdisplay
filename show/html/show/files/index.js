fetch(`https://api.launchpencil.f5.si/waitdisplay/`, {
  mode: 'cors'
})
.then(response => response.text())
.then(data => {
        a = data.split(',');
        document.getElementById('message').innerHTML = a[0]
        //document.getElementById('message').innerText = 'ここにテキストを入力\nhogehuga'

        syncstatus(a[1]);
        
})
.catch(error => {
    document.getElementById('message').innerText = 'ここにテキストを入力';
});


function syncstatus(percentage) {
    if (percentage === '100') {
        document.getElementById('status').src = 'images/100.png';
        document.getElementById('main').style.backgroundColor = '#954eca';
    } else if (percentage === '75') {
        document.getElementById('status').src = 'images/75.png';
        document.getElementById('main').style.backgroundColor = '#ff5b5b';
    } else if (percentage === '50') {
        document.getElementById('status').src = 'images/50.png';
        document.getElementById('main').style.backgroundColor = '#ED7D31';
    } else if (percentage === '25') {
        document.getElementById('status').src = 'images/25.png';
        document.getElementById('main').style.backgroundColor = '#5b9bd5';
    } else {
        document.getElementById('status').style.display = 'none';
        document.getElementById('message').style.width = '100%';
        document.getElementById('message').style.paddingRight = '0';
        document.getElementById('main').style.backgroundColor = '#A5A5A5';
    }    
    
}