fetch(`https://api.launchpencil.f5.si/waitdisplay/`, {
  mode: 'cors'
})
.then(response => response.text())
.then(data => {
        a = data.split(',');
        document.getElementById('message').innerHTML = a[0]
        //document.getElementById('message').innerText = 'ここにテキストを入力\nhogehuga'

        //syncstatus(a[1]);
        syncstatus(75);
        
})
.catch(error => {
    document.getElementById('message').innerText = 'ここにテキストを入力';
});


function syncstatus(percentage) {
    switch (percentage) {
        case percentage = '100':
            document.getElementById('status').src = 'images/100.png'
            document.getElementById('main').style.backgroundColor = '#954eca'
            break;
        case percentage = '75':
            document.getElementById('status').src = 'images/75.png'
            document.getElementById('main').style.backgroundColor = '#ff5b5b'
            break;
        case percentage = '50':
            document.getElementById('status').src = 'images/50.png'
            document.getElementById('main').style.backgroundColor = '#ED7D31'
            break;
        case percentage = '25':
            document.getElementById('status').src = 'images/25.png'
            document.getElementById('main').style.backgroundColor = '#5b9bd5'
            break;
    
        default:
            document.getElementById('status').style.display = 'none'
            document.getElementById('message').style.width = '100%'
            document.getElementById('message').style.paddingRight = '0'
            document.getElementById('main').style.backgroundColor = '#A5A5A5'
            break;
    }
    
}