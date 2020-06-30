const secret=require('./keys.js');

const axios = require('axios');
//http://axios-js.com/docs/index.html#axios-config

const clientId=secret.TWITCH_CLIENT_ID
console.log(clientId)


async function getAuthToken() {
  params = {
    client_id: secret.TWITCH_CLIENT_ID,
    client_secret: secret.TWITCH_CLIENT_SECRET,
    grant_type: "client_credentials",
  }

//axios.post(url[, data[, config]]) otherwise sending data or
//const response = await axios.post("https://id.twitch.tv/oauth2/token?client_id=gp64d2q7abvab5newf48ijvwjs8amf&client_secret=datpb9aupeka2tuq3sim8mfweembk0&grant_type=client_credentials")

/* or
  axios({
  method:"POST",
  baseUrl: "https://id.twitch.tv",
  url: "oauth2/token",
  params
});
*/

try{
  const response = await axios.post("https://id.twitch.tv/oauth2/token",null, {params})
  console.log(response.data);
  }
  catch (error) {
  console.error(error);
}
}
getAuthToken()


/*
params = {
  client_id: secret.TWITCH_CLIENT_ID,
  client_secret: secret.TWITCH_CLIENT_SECRET,
  grant_type: "client_credentials",
}
axios.post("https://id.twitch.tv/oauth2/token", {params}) .then(
respo=>{
console.log('success')
console.log(respo.data);
}
)
.catch(error=>console.log(error))
*/
