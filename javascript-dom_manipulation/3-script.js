header = document.querySelector("header")
button = document.getElementById("toggle_header")
button.addEventListener("click", togle)
function togle()
{
    if (header.className == "green")
    {
        header.className = "red"
    } else
    {
        header.className = "green"
    }
}
