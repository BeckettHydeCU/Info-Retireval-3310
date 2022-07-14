const SitemapGenerator = require('sitemap-generator');

//NOTES:
// https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
//h ttps://www.npmjs.com/package/sitemap-generator

//TO USE:
// run using node sitemapGenerator.js


// create generator
const generator = SitemapGenerator('http://karpathy.github.io/', {
  stripQuerystring: false
});

// register event listeners
generator.on('done', () => {
  // sitemaps created
});

// start the crawler
generator.start();
