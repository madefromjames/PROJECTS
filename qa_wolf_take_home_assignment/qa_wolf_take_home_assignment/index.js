// EDIT THIS FILE TO COMPLETE ASSIGNMENT QUESTION 1
const { chromium } = require("playwright");
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

async function saveHackerNewsArticles() {
  // launch browser
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  // go to Hacker News
  await page.goto("https://news.ycombinator.com/newest");

  // Extract titles and URLs of the top 10 articles
  const articles = await page.$$eval('td.title .titleline a', links => 
    links.slice(0, 10).map(link => ({
      title: link.innerText,
      url: link.href
    }))
  );

  // Define CSV writer
  const csvWriter = createCsvWriter({
    path: 'top-10-aricles.csv',
    header: [
      { id: 'title', title: 'Title' },
      { id: 'url', title: 'URL' }
    ]
  });

  // Write articles to CSV
  await csvWriter.writeRecords(articles)
    .then(() => {
      console.log('The CSV file was written successfully');
    });

  await browser.close();
}

(async () => {
  await saveHackerNewsArticles();
})();
