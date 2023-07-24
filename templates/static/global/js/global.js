globalMessage = document.querySelector('#globalMessage')

window.onload = () => {
    setTimeout(() =>{
        globalMessage.remove()
    }, 5000)
}