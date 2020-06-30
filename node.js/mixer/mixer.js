require('dotenv').config();

const axios = require('axios')
const clientId=process.env.MIXER_CLIENT_ID

async function getMixerVideos(limit) {
  let promise=await axios({
    method:"get",
    url: "https://mixer.com/api/v1/channels",
    headers: {'client-id': clientId},
    // not needed client id may require in future update of api v2
    // 548832
     params:{where:'typeId:eq:130897',
     // fields: 'token','name','viewersTotal','languageId','audience','thumbnail'
     limit:limit,
     order: 'viewersCurrent:DESC',
     //total or current
    }

  });
  return promise.data
}



exports.getMixerVideos = getMixerVideos
