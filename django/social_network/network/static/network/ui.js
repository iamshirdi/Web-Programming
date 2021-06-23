document.addEventListener('DOMContentLoaded', function() {
    document.querySelector(".follow").addEventListener('click', function(event) {
        console.log(this.id)
        change(this.id)});

});

function change(usr){
    fetch(`/follow/${usr}`).then(response => response.json())
    .then(result => {
        console.log(result);
        let r = result.check
        fetch(`/follow/${usr}`, {
            method: 'POST',
            body: JSON.stringify({
                data: r
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log("json changed result is ",result);
            if (result.changed == "True"){
                document.querySelector(`#${usr}`).innerHTML="Unfollow"
                
            } 
            if (result.changed == "False"){
                document.querySelector(`#${usr}`).innerHTML="Follow"
            } 
        });
        return false;

    })
}

