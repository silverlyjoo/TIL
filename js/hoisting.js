// let 블록 스코프 예제

// {
//     let x = '정운지'
//     console.log(x)
//     {
//         let x = 1
//         console.log(x)
//     }
//     console.log(x)
// }
// console.log(x)



// if (x !== 1) {
//     console.log(y) // undifined
//     var y = 3
//     if (y === 3) {
//         var x = 1
//     }
//     console.log(y) // 3
// }
// if (x ===1) {
//     console.log(y) // 3
// }


ssafy()
// function ssafy() {
//     console.log('hoisting!!')
// }
let ssafy = function () {
    console.log('hoisting')
}