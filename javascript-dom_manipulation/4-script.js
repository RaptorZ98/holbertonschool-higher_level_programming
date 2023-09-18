button = document.getElementById("add_item")
button.addEventListener("click", addItem)
function addItem()
{
    list = document.querySelector(".my_list")
    li = document.createElement("li")
    li.textContent = "Item"
    list.appendChild(li)
}