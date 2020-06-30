const secret=require('./keys.js');

const axios = require('axios');
const TwitchClient = require("twitch").default


const clientId=secret.TWITCH_CLIENT_ID
const accessToken=secret.accessToken

console.log(clientId)

/*
const headers = {
  'Accept': 'application/vnd.twitchtv.v5+json',
  'Client-ID': clientId
}
*/

async function search(limit) {
  const twitchClient = TwitchClient.withCredentials(clientId, accessToken)

  try{
  const streams = await twitchClient.kraken.search.searchStreams("Music & Performing Arts",null,limit);
  console.log(streams.length);
  return streams
}

catch(error){
  console.log(error);
}
}


async function getTwitchVideos(limit) {
  return search( limit)
}

async function main(){
let names=await getTwitchVideos(16);
return names[0]
// return names.map(name=>name._data.channel.display_name)
}

main().then(console.log)
