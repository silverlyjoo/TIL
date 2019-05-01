
// non blocking

// const nothing = () => {
//     console.log('hello')
// }
// console.log('start sleeping')
// setTimeout(nothing, 3000)
// console.log('end of program')


// act like python code - blocking

// const logEnd = () => {
//     console.log('end of program')
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000)


function first() {
    console.log('first')
}
function second() {
    console.log('second')
}
function third() {
    console.log('third')
}

first()
setTimeout(second, 0)
third()

