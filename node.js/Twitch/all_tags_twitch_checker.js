require('dotenv').config();

const axios = require("axios")
const TwitchClient = require("twitch").default

const clientId = process.env.TWITCH_CLIENT_ID
const secret = process.env.TWITCH_CLIENT_SECRET
const accessToken = process.env.TWITCH_ACCESS_TOKEN

// HTTP 400 !?
// TODO: Fix this, currenly accessToken is copied from manual POST in Postman
// Axios post written as axios.post(url[, data[, config]])
async function getAuthToken() {
  params = {
    client_id: clientId,
    client_secret: secret,
    grant_type: "client_credentials",
  }

  let res = await axios.post("https://id.twitch.tv/oauth2/token",null, {params})

  console.log(res.data)
}


// tags address get from json
const tagsJson = require("./tagAddresses");
// console.log(tagsJson);


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



async function search(term, limit) {
  const twitchClient = TwitchClient.withCredentials(clientId, accessToken)
  const streams = await twitchClient.kraken.search.searchStreams(term)
  // const streams = await twitchClient.kraken.search.searchStreams({ term: term, limit: limit })

  let tags=[]
    tags=await tag(244731172);
    console.log(tags)
    stream={}
    stream._data={}
  //Predefined Language Tags
        if (tags.includes('English'))  {
          console.log(1)
            stream._data['lang']=[tagsJson['English']] //must be array
            const index = tags.indexOf('English');
            tags.splice(index, 1);
        }
  // No check further if English Most common tag found
        else {
          let langFilter= tags.filter(value => lang.includes(value))
          console.log('----',langFilter)

          if (langFilter.length>0){
            console.log(2)

            stream._data['lang']=[tagsJson[langFilter[0]]]
            const index = tags.indexOf(langFilter[0]);
            tags.splice(index, 1);
             }
             else {
               console.log(3)

               // English Automatic Tag
               stream._data['lang']=[tagsJson['English']]
             }
           }
  //Predefined Genre Tags else empty
          stream._data['genre']=[]
          if (tags.length>0){
          let array1=tags.filter(value => genre.includes(value))
          // console.log(array1)
          let array2=array1.map(array=>tagsJson[array])
          // console.log(array2)
          stream._data['genre']=array2
          console.log(stream._data['lang'],stream._data['genre'])
          console.log('-------')

          }
          // console.log(stream);
}

async function getTwitchVideos(limit) {
  return search("music performing arts", limit)
}

getTwitchVideos(4)
