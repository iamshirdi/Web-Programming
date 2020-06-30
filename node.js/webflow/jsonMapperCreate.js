// gets address of new collection and creates map in json file
require('dotenv').config();

const Webflow = require("webflow-api")

const webflow = new Webflow({
  token: process.env.WEBFLOW_API_TOKEN
})
const TAG_COLLECTION = "5eea74d64c280b56703b5034" // new collection id here

// file system module to perform file operations
const fs = require("fs")

// id of each name as JSON Data

const filter = {}
async function getAddress() {
  const itemsMap = await webflow.items({ collectionId: TAG_COLLECTION })
  // console.log(itemsMap)
  itemsMap["items"].map(item => {
    filter[item["name"]] = item["_id"]
  })
  console.log(filter)

  var jsonContent = JSON.stringify(filter)
  console.log(jsonContent)

  // Write to file
  fs.writeFile("tagAddresses.json", jsonContent, "utf8", function(err) {
    if (err) {
      console.log("An error occured while writing JSON Object to File.")
      return console.log(err)
    }

    console.log("JSON file has been saved.")
  })
}
getAddress()
