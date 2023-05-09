export async function fetchArticles(queryConfig) {
  const endpoint = getEndpoint();
  console.log(`${endpoint}/news`)
  const apiURL = new URL(`${endpoint}/news`);
  apiURL.searchParams.append('keyword', queryConfig.keyword);
  apiURL.searchParams.append('beforeDate', queryConfig.datePosted);
  const response = await fetch(apiURL);
  if (!response.ok) {
    throw new Error(`Failed to fetch data from endpoint ${apiURL}. Status code: ${response.status}`);
  }
  return await response.json();
}

function getEndpoint() {
  let apiURL;
  if (window.location.host.includes('127.0.0.1')) {
    apiURL = 'http://localhost:5998'
  }

  // TODO
  // handle for other environments

  return apiURL;
}