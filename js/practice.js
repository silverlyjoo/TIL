var _ = require('lodash');

let list = ['짜장면', '짬뽕', '볶음밥', ]
let pick = _.sample(list)
let menu = {
    짜장면: 'http://goos.wiki/images/thumb/9/93/%EC%A7%9C%EC%9E%A5%EB%A9%B4.jpg/360px-%EC%A7%9C%EC%9E%A5%EB%A9%B4.jpg',
    짬뽕: 'http://pds27.egloos.com/pds/201510/26/41/d0021441_562d9a57b1383.jpg',
    볶음밥: 'http://recipe1.ezmember.co.kr/cache/recipe/2015/06/18/58d359a9ac359adbc4c7fa2603f2e504.jpg',
}


let numbers = _.range(1, 46)
let lottery = _.sampleSize(numbers, 6).sort()



let getMin = (a, b) => {
    if (a > b) {
        return b
    }
    return a
}




let getMinFromArray = nums => {
    let min = Infinity
    for (num of nums) {
        if (min > num) {
            min = num
        }
    }
    return min
}



// console.log(`오늘의 메뉴는 ${pick}입니다.`)
// console.log(menu[pick])

// console.log(`행운의 번호: ${lottery}`)

// console.log(getMin(3, 1))

ssafy = [1, 2, 3, 4, 5,]



console.log(getMinFromArray(ssafy))