
require('dotenv').config();

const Webflow = require("webflow-api")

// Initialize the API
const webflow = new Webflow({
  token: process.env.WEBFLOW_API_TOKEN
})

const TESTS_COLLECTION = "5ee80dc47e1eb808c5f0e7e7"


  async function publishSite() {
    return await webflow.publishSite({
      siteId: "5ee80b80caf159b3298ccc7d",
      domains: ["music-demo.webflow.io"]
    }).then(console.log)
  }

  function sleep(milliseconds) {
      console.log('sleep started')
       publishSite()
      let timeStart = new Date().getTime();
      while (true) {
        let elapsedTime = new Date().getTime() - timeStart;
        if (elapsedTime > milliseconds) {
          break;
        }
      }
    }

async function main(){
// Used for testing new fields etc, works on the collection called Tests in Webflow
var i;
for (i = 0; i <90; i++) {

webflow.createItem(
    {
      collectionId: TESTS_COLLECTION,
      fields: {
        name: 'name'+i.toString(),
        slug: `name`+i.toString(),
        _archived: false,
        _draft: false,
        videoid: '0'+i.toString(),
        "video-source": "private"+i.toString(),
        // tags:('5ee92a17879c18fb659a1ef9')

        // 'multi-tags':['5ee92a17879c18fb659a1ef9', '5ee92a17bc33606d232e9366']

      }
    },
    { live: true }
  )

  if (i%30==0 & i!==0){
    try{
    await publishSite() // 1 rate everytime it calls
  }
  catch{
    console.log('Rate Limit hit wait and retry')
    sleep(90000)
    await publishSite() // 1 rate everytime it calls
  }

  while (true){
    sleep(65000)
    let rate=await webflow.items({ collectionId: '5ee80d7cf959d52f7043e07c' })
    console.log(rate)
  if (rate['_meta']['rateLimit']['remaining']>40){
      console.log('now breaked')
      break
  }
}
}

}





}
main()
