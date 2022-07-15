const SitemapGenerator = require('sitemap-generator');

//NOTES:
// https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
//h ttps://www.npmjs.com/package/sitemap-generator

//TO USE:
// run using node sitemapGenerator.js


// create generator
const generator = SitemapGenerator('https://www.colorado.edu/', {
  maxDepth: 2,
  maxEntriesPerFile: 1000,
  stripQuerystring: false
});

// register event listeners
generator.on('done', () => {
  // sitemaps created
});

generator.on('error', (error) => {
  console.log(error);
});

// start the crawler
generator.start();
