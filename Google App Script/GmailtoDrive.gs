// to run every 1 minute etc automatically . check appscript limitations for daily limits before running
// can schedule triggers simialry based on dcoumentation

//ScriptApp.newTrigger('searchattach').timeBased().everyMinutes(1).create();


function searchattach() {
  var labeltoCheck='distributor'

  //can keep inbox as label to move back to inbox after checking thread and saving attachments to drive
  // saves processing next trigger or run
  var labeltoMove='distributed'

  //calls function and creates labels if not exist
  getLabel(labeltoCheck)

  // moving label created
  getLabel(labeltoMove)

  var query = 'label:'+labeltoCheck;

  //folder name here to save attachments to
  var FolderName='gmail_pdfs'


  var newLabel = GmailApp.getUserLabelByName(labeltoMove);
  var label=GmailApp.getUserLabelByName(labeltoCheck);


  var threads = GmailApp.search(query);
  Logger.log('Threads checking : '+threads.length)
  threads.forEach(function(thread) {

    //updates thread by changing labels to prevent rechecking next run time  for attachments for faster processing
    newLabel.addToThread(thread);

    //removes old label
    label.removeFromThread(thread);



    thread.getMessages().forEach(function(message) {

          var Folder = getFolder(FolderName);
          var attachments = message.getAttachments();
    //      Logger.log(attachments.length)
        attachments.forEach(function(attachment){
         var fileName = attachment.getName()
         var extension=fileName.split('.')[1];

       //   Logger.log('Name: '+fileName+'  extension: '+extension)

          if (extension==='pdf'){
           Logger.log('Name: '+fileName+'  extension: '+extension)
           var Blob = attachment.copyBlob();
           var file = DriveApp.createFile(Blob);
           Folder.addFile(file);

          }

        });
  });
});
}




//This function will create if folder not exists in gdrive
function getFolder(folderName){
  var folder;
  var folder_iterator = DriveApp.getFoldersByName(folderName);
  if(folder_iterator.hasNext()){
    folder = folder_iterator.next();
  }
  else{
    folder = DriveApp.createFolder(folderName);
  }
  return folder;
}


//This function will create if label not exists
//need to enable gmail advanced api if want to access all labels like inbox
//https://developers.google.com/gmail/api/quickstart/apps-script
function getLabel(labl) {
  var response =  GmailApp.getUserLabels();;
  var p=0;
  if (response.length == 0) {
    Logger.log('No user labels found.');
  } else {
    Logger.log('Labels:');
    for (var i = 0; i < response.length; i++) {
      var label = response[i];
  //    Logger.log('- %s', label.name);
      if (label.name===labl){
      p=1;
      }

    }
  }
  if (p===0)
  {
  Logger.log('created label  '+labl)
  GmailApp.createLabel(labl);
  }
}
