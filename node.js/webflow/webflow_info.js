const Webflow = require('webflow-api')
const webflow = new Webflow({ token: '4dd904ee11ed8a42d6381e1a8ba677f94871d8375197e76232e6c8675bbef23f' });
 //
 // webflow.info().then(info => console.log(info))

// const sites = webflow.sites();
// sites.then(s => console.log(s));

//
// const collections = webflow.collections({ siteId: '5ee80b80caf159b3298ccc7d'})
// collections.then(c => console.log(c));

// const collection = webflow.collection({ collectionId: '5ee80d7cf959d52f7043e07c' });
//
// collection.then(c => console.log(c));
//
// async function main(){
// const collection=await webflow.collection({ collectionId: '5ee80dc47e1eb808c5f0e7e7' });
// console.log(collection['fields'])
// }
// main()

// Promise <[ Item ]>
// webflow.items({ collectionId: '5ee80d7cf959d52f7043e07c' }, { limit: 10 }).then(console.log);

// items.then(i => console.log(i['items']))


async function main(){
let rate=await webflow.items({ collectionId: '5ee80d7cf959d52f7043e07c' })
console.log(rate['_meta']['rateLimit']['remaining'])
}
main()

// webflow.info().then(info => console.log(info))
