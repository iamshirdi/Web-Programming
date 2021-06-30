var url = window.location.href 

document.addEventListener('DOMContentLoaded', function() {
    add_form()
});


function add_form(){

    button4 = document.querySelector("#add_projects")
    button4.addEventListener("click",function(event)
    {
        document.querySelector("#add_projects_form").style.display="block"
        
    }) 

}

