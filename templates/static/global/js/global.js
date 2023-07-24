globalMessage = document.querySelector('#globalMessage')


window.onload = function(){
    setTimeout(() =>{
        globalMessage.remove()
    }, 5000)
}