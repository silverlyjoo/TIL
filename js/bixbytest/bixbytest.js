const http = require('http')

let url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101'

// let response = http.getUrl(url, {
//     format: 'xmljs'
// })

const Http = new XMLHttpRequest

Http.open("GET", url)


// console.log(response)