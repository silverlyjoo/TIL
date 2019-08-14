// m부터 n까지 난수 생성
const rand = function (m, n) {
    return m + Math.floor((n - m + 1)*Math.random())
}

// 주사위 그림 무작위 반환
const randFace = function () {
    return ["crown", "anchor", "heart", "spade", "club", "diamond"][rand(0, 5)]
}

let flag = true
let rounds = 0

while (flag) {

    // 시작 조건
    let funds = 50
    let round = 0
    
    while (funds > 0 && funds < 100) {
    
        round++
        console.log(`round : ${round} |`)
        console.log(`\tstarting funds: ${funds}p`)
    
        // 돈을 건다 
        let bets = {
            crown: 0,
            anchor: 0,
            heart: 0,
            spade: 0,
            club: 0,
            diamond: 0,
        }
        
        let totalBet = rand(1, funds);
        
        if (totalBet === 7) {
            // 판돈이 7일경우 하트에 올인
            totalBet = funds;
            bets.heart = totalBet
        } else {
            // 판돈 나누기
    
            let remaining = totalBet
            do {
                let bet = rand(1, remaining)
                let face = randFace()
                bets[face] = bets[face] + bet
                remaining = remaining - bet
            } while(remaining > 0)
        }
        funds = funds - totalBet
    
        console.log('\tbets: ' + Object.keys(bets).map(face => `${face}: ${bets[face]} pence`).join(', ') + ` (total: ${totalBet} pence)`)
        console.log(`\ttotalbettings : ${totalBet}`)
        // 주사위 3번 던지기
        const hand = []
        for (let roll = 0; roll < 3; roll++) {
            hand.push(randFace())
        }
    
        console.log(`\thand: ${hand.join(',')}`)
    
        let winnings = 0
    
        for(let die=0; die < hand.length; die++) {
            let face = hand[die]
            if (bets[face]> 0) winnings = winnings + bets[face]
        }
        funds = funds + winnings
        console.log(`\twinnings: ${winnings}`)
    }
    console.log(`\tending funds: ${funds}`)

    if (funds === 100) {
        flag = false
    }
    rounds++
}

console.log(`totalRoundsToWin: ${rounds}`)



