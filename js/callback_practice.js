
// 배열로 이루어진 숫자들을 모두 더하는 함수


var numbers = [1, 2, 3, 4, 5,]

const numbersAddEach = numbers => {
    let sum = 0
    for ( const number of numbers ) {
        sum += number
    }
    return sum
}


// 배열 숫자들 빼는 함수

const numbersSubEach = numbers => {
    let subs = 0
    for ( const number of numbers ) {
        subs -= number
    }
    return subs
}


// 배열 숫자들 곱하는 함수

const numbersMulEach = numbers => {
    let muls = 1
    for ( const number of numbers ) {
        muls *= number
    }
    return muls
}


console.log(numbersAddEach(numbers))
console.log(numbersSubEach(numbers))
console.log(numbersMulEach(numbers))


// const numbersEach = (numbers, callback) => {
//     let acc
//     for ( const number of numbers) {
//         acc = callback(number, 0)
//     }
//     return acc
// }

// // 더한다
// const addEach = (number, acc = 0) => {
//     return acc + number
// }

// // 뺀다
// const subEach = (number, acc = 0) => {
//     return acc - number
// }

// // 곱한다
// const mulEach = (number, acc = 1) => {
//     return acc * number
// }

// console.log(numbersEach(numbers, addEach))
// console.log(numbersEach(numbers, subEach))
// console.log(numbersEach(numbers, mulEach))


const NUMBERS = [1, 2, 3, 4, 5, 6]

const numbersEach = (numbers, callback) => {
    let acc
    for (let i = 0; i < numbers.length; i++){
        number = numbers[i]
        acc = callback(number, acc)
    }
    return acc
}

numbersEach(NUMBERS, (number, acc=0) => acc + number)
numbersEach(NUMBERS, (number, acc=0) => acc - number)
numbersEach(NUMBERS, (number, acc=1) => acc * number)
console.log(numbersEach(NUMBERS, (number, acc=0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc=0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc=1) => acc * number))