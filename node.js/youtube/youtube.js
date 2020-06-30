require('dotenv').config();

const { google } = require("googleapis")

const youtube = google.youtube({
  version: "v3",
  auth: process.env.YOUTUBE_API_KEY,
})

function hasQuota() {
  return youtube.channels
    .list({
      part: "snippet",
      id: 'UC4Wf0An63EgbRiZ-Eo-fEWg',
      fields: "items(id)",
    })
    .then((res) => {
      console.log(res)

      return res
    })
    .catch((error) => {
      console.log(error)

      return error

    })
}

hasQuota()
