button = document.getElementById("update_header")
header = document.querySelector("header")
button.addEventListener("click", changeText)
function changeText()
{
    header.textContent = "New Header!!!"
}
