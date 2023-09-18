header = document.querySelector("header")
button = document.getElementById("red_header")
button.addEventListener("click", addClass)
function addClass()
{
    header.className = "red"
}
