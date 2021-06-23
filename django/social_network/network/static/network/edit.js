var url = window.location.href 

document.addEventListener('DOMContentLoaded', function() {
    edit_post();
    edit_like()
});

function edit_like(){
document.querySelectorAll(".like").forEach(button => { 
    button.addEventListener('click', function(event) {   
    var c = parseInt(button.parentElement.querySelector(".count").innerHTML)
    var token = button.parentElement.getElementsByTagName("input").csrfmiddlewaretoken.value
    var id2 = button.id
    fetch("/edit_like", {
        method: 'POST',
        headers: {
            'X-CSRFToken': token 
       },
        body: JSON.stringify({
            id: `${id2}`
        })
    }).then(response => response.json())
    .then(result => {
        button.parentElement.querySelector(".count").innerHTML= result.changed
        if (result.added){
            button.parentElement.querySelector("button").innerHTML ="UnLike"
        }
        else{
            button.parentElement.querySelector("button").innerHTML ="Like"
        }
    })

})
})
}


function edit_post(){

    document.querySelectorAll(".edit").forEach(div => { 
        div.addEventListener('click', function(event) {
            var parent = div.parentElement
            var id = parent.querySelector(".edit button").id
            console.log(id)
            var post = parent.querySelector(".post_desc")
            console.log(post)
            var pre_data = parent.querySelector(".post_desc").innerHTML.slice(12)
            // console.log("pre_data is",pre_data)
            post.innerHTML = "<b>Post:</b> <input type='text' value='"+`${pre_data}`+"'>"
            parent.querySelector(".edit button").innerHTML ="Save"
            parent.querySelector(".post_desc input").style.width="75%"
            parent.querySelector(".post_desc input").style.height="100px"
            
            parent.querySelector(".edit button").addEventListener('click',function(event){
                var dat = parent.querySelector(".post_desc input").value

                var token = parent.getElementsByTagName("input").csrfmiddlewaretoken.value

                fetch("/edit_post", {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': token 
                   },
                    body: JSON.stringify({
                        post: `${dat}`,
                        id: `${id}`
                    })
                }).then(response => response.json())
                .then(result => {
                    console.log(result.changed)
                    parent.querySelector(".post_desc input").value =result.changed
    
                })
            })
           
        })
        })
}