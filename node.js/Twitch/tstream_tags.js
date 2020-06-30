//stream tags
// https://www.twitch.tv/directory/all/tags
require('dotenv').config();

const axios = require('axios');
const TwitchClient = require("twitch").default

//require('util').inspect.defaultOptions.depth = null


const clientId = process.env.TWITCH_CLIENT_ID
const secret = process.env.TWITCH_CLIENT_SECRET
const accessToken = process.env.TWITCH_ACCESS_TOKEN

// tags address get from json
const tagsJson = require("./tagAddresses");
console.log(tagsJson);


const lang=['German','Chinese','Russian','French','Portugese','Turkish',
'Swedish','Korean','English'];
const genre=['Electronic Music','Music Production','Dance Music',
'Hip Hop Music','Pop Music','DJ','Anime','Radio','Musician',
'Alternative Music','Singing','Family Friendly','Rock Music','Folk Music',
'Jazz Music','Heavy Metal Music','Radio','Downtemp Music'];


async function tag(broadcast_id) {
  let promise=await axios({
  method:"get",
  url: "https://api.twitch.tv/helix/streams/tags",
  headers: {'Client-ID': clientId, 'Authorization':'Bearer'+' '+accessToken},
  params:{broadcaster_id:broadcast_id}
  });
  return promise.data.data.map(ta=>ta.localization_names['en-us'])
}
//tags get from broadcast id
// tags(502654354).then(console.log)




async function search(term) {

  const twitchClient = TwitchClient.withCredentials(clientId, accessToken)
  const streams = await twitchClient.kraken.search.searchStreams(term)

  const tags=[]
  // const broadcasts_id=streams.map(bId=>bId._data.channel._id)
  // console.log('first broad cast id',broadcasts_id[0])

  // streams.map( stream=>{ stream._data['tag']=['h1','h2']})
  // console.log(streams[0]._data.tag)

  await Promise.all( streams.map(
      async stream=>  {
        const tags=await tag(stream._data.channel._id);

//Predefined Language Tags
        if (tags.includes('English'))  {
            stream._data['lang']=tagsJson['English']
            const index = tags.indexOf('English');
            tags.splice(index, 1);
        }
// No check further if English Most common tag found
        else {
          let langFilter= tags.filter(value => lang.includes(value))
          if (langFilter.length<1){
            stream._data['lang']=tagsJson[langFilter[0]]
            const index = tags.indexOf(langFilter[0]);
            tags.splice(index, 1);
             }
             else {
               // English Automatic Tag
               stream._data['lang']=tagsJson['English']
             }
           }
//Predefined Genre Tags else empty
          stream._data['genre']=[]
          if (tags.length>-1){
          let array1=tags.filter(value => genre.includes(value))
          // console.log(array1)
          let array2=array1.map(array=>tagsJson[array])
          // console.log(array2)
          stream._data['genre']=array2

          }

          // console.log(stream);
           }))

return streams
}


//twitchClient.kraken.search.searchStreams({term,pages,limit})



async function getTwitchVideos() {
  const data=await search("music performing arts")
  return data
}

search("music performing arts")
