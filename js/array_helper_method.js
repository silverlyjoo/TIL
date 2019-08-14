// 1. forEach
// forEach 함수는 아무것도 return 하지 않는다.

// ES5 

// var colors = ['red', 'blue', 'green',]

// for (var i = 0; i < colors.length; i++) {
//     console.log(colors[i])
// }

// // ES6+

// const COLORS = ['red', 'blue', 'green',]

// COLORS.forEach(function (color) {
//     console.log(color)
// })

// COLORS.forEach(color => console.log(color))


// exercise 1-1 아래 함수에 for 를 forEach 로 바꾸시오

// function handlePosts() {
//     const posts = [
//         { id: 23, title: 'daily news'},
//         { id: 52, title: 'Code City'},
//         { id: 105, title: 'The Ruby'},
//     ]

//     for (let i=0; i < posts.length; i++) {
//         savePosts(posts[i])
//     }
// }

// function handlePosts() {
//     const posts = [
//         { id: 23, title: 'daily news'},
//         { id: 52, title: 'Code City'},
//         { id: 105, title: 'The Ruby'},
//     ]
//     posts.forEach(post => savePosts(post))
// }


// exercise 1-2 아래 코드의 images 배열 안에 있는 정보(height, width) 를 곱해 넓이를 구하여
// area 배열에 저장하는 코드를 forEach 헬퍼를 사용해 작성해보자

// const images = [
//     { height: 10, width: 30},
//     { height: 20, width: 90},
//     { height: 52, width: 32},
// ]

// const areas = []
// images.forEach(image => areas.push(image.height * image.width))

// console.log(handlePosts())
// console.log(areas)



// 2. map
// map 함수는 새로운 배열을 return 한다. 배열 요소 변형시.
// 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때 사용
// map 과 filter 는 모두 사본을 return 하며 원본 배열은 바뀌지 않는다.

// const NUMBERS = [1, 2, 3,]

// const DOUBLE_NUMBERS = NUMBERS.map(number => number * 2)

// console.log(NUMBERS)
// console.log(DOUBLE_NUMBERS)

// exercise 2-1 map 헬퍼를 사용해,
// images 배열 안의 object 들의 height 들만 저장되어 있는 heights 배열에 저장해보자

// const images = [
//     { height: '34px', width: '39px'},
//     { height: '54px', width: '90px'},
//     { height: '83px', width: '32px'},
// ]

// const heights = images.map(image => image.height)

// console.log(heights)

// exercise 2-2 map 헬퍼를 사용해 distance / time 을 저장하는 배열 speeds 를 만들어 보자.

// const trips = [
//     {distance: 34, time: 10},
//     {distance: 90, time: 50},
//     {distance: 59, time: 25},
// ]

// const speeds = trips.map(trip => trip.distance / trip.time)

// console.log(speeds)

// exercise 2-3 다음 두 배열을 객체로 결합한 comics 배열을 만들어보자.

// const brands = ["Marvel", "DC",]
// const movies = ["IronMan", "BatMan",]

// const comics = {}
// brands.map((brand, i) => comics[brand] = movies[i])

// console.log(comics)


// 3. filter
// filter 함수는 필터링 된 요소들만 배열로 return 한다.
// 배열에서 필요한 것들만 남길 때 사용한다.

// const PRODUCTS = [
//     { name: 'cucumber', type: 'vegetable' },
//     { name: 'banana', type: 'fruit' },
//     { name: 'carrot', type: 'vegetable' },
//     { name: 'apple', type: 'fruit' },
//  ]

// const fruitProducts = PRODUCTS.filter(product => product.type === 'fruit')

// console.log(fruitProducts)


// // 3-1 filter 헬퍼를 사용해서, numbers 배열 중 50보다 큰 값들만 필터링해서 filteredNumbers 에 저장하라.
// const numbers = [ 15, 25, 35, 45, 55, 65, 75, 85, 95 ]

// const filteredNumbers = numbers.filter(number => number > 50)

// console.log(filteredNumbers)


// // 3-2 users 배열에서 admin 이 true 인 user object 들만 filteredUsers 배열에 저장하라.

// const users = [
//     {id: 1, admin: true},
//     {id: 2, admin: false},
//     {id: 3, admin: false},
//     {id: 4, admin: false},
//     {id: 5, admin: true},
// ]

// const filteredUsers = users.filter(user => user.admin)

// console.log(filteredUsers)

// 4. reduce

/*
    - map 은 배열의 각 요소를 변영한다면, reduce 는 배열 자체를 변형.
    - 배열을 `값 하나` 로 줄이는 동작.(ex. 배열의 평균, 배열의 합)
    - reduce 의 첫번째 매개변수는 `누적값(전 단계의 결과)` 이다.
    - 두 번째 매개변수는 현재 배열 요소, 현재 인덱스, 배열 자체 순으로 돌린다.
*/

// // 4-1 총합
// const SSAFY = [3, 9, 2, 7,]
// const sum = SSAFY.reduce((total, x) => total + x, 0)
// console.log(sum)


// // 4-2 평균
// const avg = SSAFY.reduce((total, x) => total + x , 0) / SSAFY.length
// console.log(avg)

// // 4-3 초기값 생략
// const sum_2 = SSAFY.reduce((total, x) => total + x)
// console.log(sum_2)


// 5. find
/*
    - 찾은 요소 1가지만 return 한다.
    - 조건에 맞는 인덱스가 아니라 요소 자체를 원할때 사용.
    - 배열 검색 헬퍼들 : find, indexOf, lastIndexOf, findIndex, some, every
*/


// const USERS = [
//     {name: 'Thor'},
//     {name: 'Steve Rogers'},
//     {name: 'Tony Stark'},
// ]

// const ironMan = USERS.find(user => user.name === 'Tony Stark')

// // ES5
// for (var i = 0; i < USERS.length; i++) {
//     if (USERS[i].name == 'Tony Stark') {
//         user = USERS[i]
//         break
//     }
// }

// console.log(ironMan)

// // 5-1 users 중에 admin 권한을 가진 요소를 찾아서 admin 에 저장하자.
// const PEOPLE = [
//     { id: 1, admin: false },
//     { id: 2, admin: false },
//     { id: 3, admin: true },
//  ]

// const admin = PEOPLE.find(person => person.admin === true)


// // 5-2 accounts 중에서 잔액이 12 인 object 를 account 에 저장하자.
// const ACCOUNTS = [
//     { balance: -10 },
//     { balance: 12 },
//     { balance: 0 }
// ]

// const account = ACCOUNTS.find(acc => acc.balance === 12)

// console.log(admin, account)


// 6. some, every

/*
    - 기존처럼 대상 배열에서 특정 요소를 뽑거나 배열을 return 하지 않고, 조건에 대해 boolean 값을 return
    - some : 조건에 맞는 요소를 찾으면 즉시 검색을 멈추고 true / 찾지 못하면 false
    - every : 해당 배열의 모든 요소가 조건에 맞아야 true / 그렇지 않다면 false
    - 즉, every 는 조건에 맞지 않는 요소를 찾아야만 검색을 멈추고 false 를 return
*/

// const arr = [1, 2, 3, 4, 5,]
// arr.some(x => x%2 === 0)

// // 6-1 컴퓨터의 램이 16보다 큰 요소가 있는지를 some 과 every 비교
// const COMPUTERS = [
//     { name: 'macbook', ram: 16 },
//     { name: 'gram', ram: 8 },
//     { name: 'series9', ram: 32 },
// ]

// const everyComputer = COMPUTERS.every(computer => computer.ram >= 16)

// const someComputer = COMPUTERS.some(computer => computer.ram >= 16)

// console.log(everyComputer, someComputer)


// 6-2 USERS 배열에서 모두가 hasSubmitted 인지 아닌지를 hasSubmitted 에 저장하라
const USERS = [
    { id: 21, hasSubmitted: true },
    { id: 33, hasSubmitted: false },
    { id: 712, hasSubmitted: true},
]

const hasSubmitted = USERS.every(submit => submit.hasSubmitted)




// 6-3 REQUESTS 배열에서 각 요청들 중 status 가 pending 인 요청이 있으면, inProgress 변수에 true 를 저장하라.
const REQUESTS = [
    { url: '/photos', status: 'complete' },
    { url: '/albums', status: 'pending' },
    { url: '/users', status: 'failed' },
]

const inProgress = REQUESTS.some(progress => progress.status === 'pending')

console.log(hasSubmitted, inProgress)