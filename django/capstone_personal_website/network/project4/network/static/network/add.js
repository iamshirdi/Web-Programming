var url = window.location.href 

document.addEventListener('DOMContentLoaded', function() {
    add_form()
});


function add_form(){
    button = document.querySelector("#add_job")
    button.addEventListener("click",function(event)
    {
        document.querySelector("#add_job_form").style.display="block"
        
    }) 

    button2 = document.querySelector("#add_edu")
    button2.addEventListener("click",function(event)
    {
        document.querySelector("#add_edu_form").style.display="block"
        
    }) 

    button3 = document.querySelector("#add_skills")
    button3.addEventListener("click",function(event)
    {
        document.querySelector("#add_skills_form").style.display="block"
        document.querySelector("#add_skills_form").querySelector("#skill").value = document.querySelector(".skills").innerText
    }) 

    button4 = document.querySelector("#add_projects")
    button4.addEventListener("click",function(event)
    {
        document.querySelector("#add_projects_form").style.display="block"
        
    }) 

}

