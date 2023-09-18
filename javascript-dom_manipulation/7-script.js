ul = document.getElementById("list_movies")
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
.then(
    function(response)
    {
        return response.json()
    }
)
.then(
    function(title)
    {
        titles = title.results
        titles.forEach(function(titles)
        {
            li = document.createElement("li")
            li.textContent = titles.title
            ul.appendChild(li)
        })
    }
)
