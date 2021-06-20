document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');



});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#email-view').innerHTML = '';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // Add compose post request
  document.querySelector('#compose-form').onsubmit = () =>{
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: document.querySelector('#compose-recipients').value,
          subject: document.querySelector('#compose-subject').value,
          body: document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
        // Load sent mailbox
        load_mailbox('sent');
    });
    return false;
  }

}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#email-view').innerHTML = '';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get Request to mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails and check mailbox type
      console.log(emails);
      var check = true
      if (`${mailbox}` === "sent"){
        var check = false;
      }
      //view
      view_emails(emails,check)
  });

}

function view_emails(emails,check) {

  emails.forEach(function(email){

    const element = document.createElement('div');
    element.setAttribute("class", "div_view")
    element.setAttribute("id", `${email.id}`)
    console.log(check)
    if (check){
    var sender = email.sender
    }
    else{
    var sender = email.recipients[0]
    }
    
    const timestamp = email.timestamp
    const subject = email.subject
    element.innerHTML = `<div class= "sender">${sender}</div> 
    <div class="subject"> ${subject} </div> 
    <div class="time"> ${timestamp} </div> `;
    // read color
    if (email.read){
      element.style.backgroundColor = "gray";
    }
  
    // view email
    element.addEventListener('click', function() {
        console.log('This element has been clicked!')
        view(this.id,check)
    });
    document.querySelector('#emails-view').append(element);

  })
}

function view(email_id,check){

  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#email-view').style.display = 'block';
      document.querySelector('#compose-view').style.display = 'none';
      const element = document.createElement('div');
      const sender = email.sender
      const reciever = email.recipients[0]
      const timestamp = email.timestamp
      const subject = email.subject
      const body = email.body


      element.innerHTML = `<div><b>From: </b>${sender}</div> 
      <div><b>To: </b> ${reciever} </div>
      <div> <b>Subject: </b> ${subject} </div> 
      <div><b>Timestamp: </b> ${timestamp} </div>
      <div id="add">  </div>
      <hr>
      <div> ${body} </div> `;
      document.querySelector('#email-view').append(element);

  
      // Put and change to read
      fetch(`/emails/${email_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })
      
      // archive button add to all other except sent
      if (check){
        const buton = document.createElement("button");
        buton.setAttribute("class","btn btn-sm btn-outline-primary")
        buton.setAttribute("id","mark")
        if (email.archived){
          buton.innerHTML = "UnArchive";
        }
        else{
          buton.innerHTML = "Archive";
        }
        document.querySelector('#add').append(buton);

        // Reply button add
        const rep = document.createElement("button");
        rep.setAttribute("class","btn btn-sm btn-outline-primary")
        rep.setAttribute("id","reply")
        rep.innerHTML = "Reply";
        document.querySelector('#add').append(rep);
      

    }
   
      // archive put
      document.querySelector('#mark').onclick = () => {
        if (email.archived){
        var a =Boolean(false);
        }
        else{
        console.log("archived")
        var a = Boolean(true);
        }
        console.log(a)
        fetch(`/emails/${email_id}`, {
          method: 'PUT',  
          body: JSON.stringify({
              archived: a
          })
        })
        load_mailbox('inbox')
        return false
      }

      // reply function
      document.querySelector('#reply').onclick = () => {
        compose_email()
        // fill empty prefill fields
        document.querySelector('#compose-recipients').value = email.sender;
        // no need to add re if subject contains it
        let sub = email.subject 
        console.log(sub.substring(0,3))
        if (sub.substring(0,3) !== "Re:"){
        document.querySelector('#compose-subject').value = "Re: "+email.subject;
        }
        else{
          document.querySelector('#compose-subject').value = email.subject;
        }
        document.querySelector('#compose-body').value = "On "+email.timestamp+" "+email.sender+" wrote: "+email.body;

        return false
      }

    

  });
  return false;
}