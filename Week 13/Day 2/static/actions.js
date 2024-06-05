//DOM
let button = document.querySelector("span")
let body = document.querySelector("body")

button.addEventListener("click", (e) => {
    function changeColor() {
        return Math.floor(Math.random() * 255) + 1
    }
    body.style.backgroundColor = `rgb(${changeColor()}, ${changeColor()}, ${changeColor()})`
})