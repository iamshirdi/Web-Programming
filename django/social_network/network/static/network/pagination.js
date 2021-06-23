var url = window.location.href 
document.addEventListener('DOMContentLoaded', function() {
    let n = document.querySelector("#next")
    if (n!== null){
    n.addEventListener('click',()=>next_load());
    }
    let p = document.querySelector("#prev")
    if (p!== null){
        p.addEventListener('click',()=>prev_load())
    }
    
})

function next_load(){
    console.log("next is clicked")
    console.log(url.slice(-8,-1))
    if (url.slice(-8,-1) === "/?page="){
        var num = parseInt(url.slice(-1))+1
    }
    else{
        var num = 2
    }
    location.href = `${url}?page=${num}`
    
}

function prev_load(){
    console.log("previous is clicked")
  
    var num = parseInt(url.slice(-1))-1
  
    location.href = `${url}?page=${num}`
    // location.href = `/?page=${count}`
}
