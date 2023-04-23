export function getProviderClass(article) {
    if (article.provider === 'profit.ro') {
        return 'profit-ro'
    }
    
    return article.provider
}