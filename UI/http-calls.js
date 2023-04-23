export async function fetchArticles(queryConfig) {
  const endpoint = new URL('https://localhost:5999/news');
  endpoint.searchParams.append('keyword', queryConfig.keyword);
  endpoint.searchParams.append('beforeDate', queryConfig.datePosted);
  const response = await fetch(endpoint);
  if (!response.ok) {
    throw new Error(`Failed to fetch data from endpoint ${endpoint}. Status code: ${response.status}`);
  }
  return await response.json();
}
