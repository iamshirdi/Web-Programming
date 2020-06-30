//creates new collection
const Webflow = require("webflow-api")
const webflow = new Webflow({
  token: process.env.WEBFLOW_API_TOKEN
})
const TAG_COLLECTION = "5eeb5b2067d4022866786237" // new collection id here

//get predefined tags from tags.js and create tags collection
var category = require("./tags")
const lang = category.lang
const genre = category.genre
// console.log(lang,genre)

function createTagItem(name) {
  return webflow.createItem(
    {
      collectionId: TAG_COLLECTION,
      fields: {
        name: name,
        slug: name.split(' ').join('-').toLowerCase(),
        _archived: false,
        _draft: false
      }
    },
    { live: true }
  )
}

async function publishSite() {
  return webflow
    .publishSite({
      siteId: "5eb403f88cf2c6351e1455a0",
      domains: ["music-test-81c209.webflow.io", "abbas.live", "www.abbas.live"]
    })
}

async function main() {
  const genreItems = lang.concat(genre)
  console.log("check if all collection items present", genreItems.length)

  genreItems.map(async item => {
    // CSV: console.log(item + ',' + item.split(' ').join('-').toLowerCase())
    await createTagItem(item)
  })
  // Not needed since {live: true} when creating items
  // await publishSite()
}

main()

// check if all tags are loaded or not into collection
async function check() {
  const itemsMap = await webflow.items({ collectionId: TAG_COLLECTION })
  const logged = itemsMap["items"].map(item => item["name"])

  const genreItems = lang.concat(genre)
  console.log(genreItems.length)
  console.log(logged.length)

  let notLogged = genreItems.filter(x => !logged.includes(x))

  console.log(notLogged)
  return notLogged
}
// check()
