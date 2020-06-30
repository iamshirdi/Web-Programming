//get predefined tags from tags.js
const createCsvWriter = require('csv-writer').createObjectCsvWriter;


const category = require("./tags")
const lang = category.lang
const genre = category.genre
// console.log(lang,genre)

const genreItems = lang.concat(genre)


const csvWriter = createCsvWriter({
  path: 'tags.csv',
  header: [
    {id: 'name', title: 'Name'},
    {id: 'slug', title: 'Slug'}
  ]
});

var data=[]

genreItems.map(genre=>
  {
    json={}
    json['name']=genre
    json['slug']=genre.split(' ').join('-').toLowerCase()
    data.push(json)

  }
)
// console.log(data)


csvWriter
  .writeRecords(data)
  .then(()=> console.log('The CSV file was written successfully'));
