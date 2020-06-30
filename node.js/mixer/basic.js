//https://dev.mixer.com/guides/core/basictutorial
// https://mixerdev.azurewebsites.net/guides/core/faq
'use strict';
require('dotenv').config();

//
// const Mixer = require('@mixer/client-node');
// const client = new Mixer.Client(new Mixer.DefaultRequestRunner());
//
// client.use(new Mixer.OAuthProvider(client, {
//     clientId:process.env.MIXER_CLIENT_ID
// }))
//
// client.request('GET', `channels`,{
//   qs:{
//     page:1,
//     limit:1,
//     // fields:'typeId',
//     order:'viewersTotal:DESC',
//     where:'typeId:eq:130891',
//
//   },
// }).then(res=>console.log(res.body))

const axios = require('axios')
const clientId=process.env.MIXER_CLIENT_ID

async function search() {
  let promise=await axios({
    method:"get",
    url: "https://mixer.com/api/v1/channels",
    headers: {'client-id': clientId},
    // not needed client id may require in future update of api v2

     params:{where:'typeId:eq:130897',
     // fields: 'token','name','viewersTotal','languageId','audience','thumbnail'
     limit:1,
     order: 'viewersCurrent:DESC',
     //total or current
    }

  });
  return promise.data
}

 search().then(console.log)

async function getDetails() {
  let promise=await axios({
    method:"get",
    url: "https://mixer.com/api/v1/channels/Monstercat",
    headers: {'client-id': clientId},
    // headers: {'Client-ID': clientId, 'Authorization':'Bearer'+' '+accessToken},

     params:{}

  });
  return promise.data
}

// getDetails().then(console.log)
