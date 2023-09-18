fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
.then(
    function(response)
    {
        return response.json()
    }
)
.then(
    function(name)
    {
        document.getElementById("character").textContent = name.name
    }
)
