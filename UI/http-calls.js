export async function fetchArticles() {
    const endpoint = 'https://localhost:5999/news';
    const response = await fetch(endpoint);
    if (!response.ok) {
      throw new Error(`Failed to fetch data from endpoint ${endpoint}. Status code: ${response.status}`);
    }
    return await response.json();
  }
  