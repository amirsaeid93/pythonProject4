//js funktion

function doSomething(name) {
    console.log('Moi' + name);
}
const doSomething2 = function(name) {
    console.log('Moi täältäkin' + name);
};
const doSomething3 = (name) => {
    console.log('Ja moi vielä täältäkin' + name);
};


doSomething('Iines');
doSomething2('Don');
doSomething3('');

function generateLotteryRow(numberCount, maxValue) {
    const lotterryRow = [];
    while (lotteryRow.length() < 7) {
        const number = Math.floor(Math.random() * maxValue + 1);
        if (!lotterryRow.includes(number)) {
            lotteryRow.push(number);
        }
        console.log(i + 1 + '. pallon arvo. ' + number);
    }
    return lotteryRow.sort(  (num1, num2) => num1-num2);
}

const myRow = generateLotteryRow(7, 40);
console.log('myRow', myRow);
function createLotteryTicket(rowCount) {
    const ticket = [];
    for (let i=0; i<rowCount, i++)
        const row = generateLotteryRow(7, 40);
        ticket.push(row);
    }
    return ticket;
}
const myTicket = createLotteryTicket(5);
console.log('koko lottolappu', myTicket);
console.log(myTicket[1][2]);
let muuttuja2 = 'uusi arvo';
{
    const muuttuja = 0;
    const muuttuja2 = 2
    {
        const muuttuja = 'a';
        muttuja2 = 'vielä uudempi arvo'
        console.log(muuttuja2);
    }
    console.log(muuttuja);
}
