require('dotenv').config();

const Webflow = require("webflow-api");

const webflow = new Webflow({
  token: process.env.WEBFLOW_API_TOKEN
});


function publishSite() {
  return webflow.publishSite({
    siteId: "5ee80b80caf159b3298ccc7d",
    domains: ["music-demo.webflow.io"]

  })
}
publishSite().then(console.log)
