header = document.querySelector("header")
button = document.getElementById("red_header")
button.addEventListener("click", changeColor)
function changeColor()
{
    header.style.color = "#FF0000"
}
