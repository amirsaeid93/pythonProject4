const targetElem= document.querySelector('#output');
targetElem.innerHTML = '<p>Moi</p>';

const startYear = parseInt(prompt('Alkuvuosi?'));
const endYear = parseInt(prompt('Loppuvuosi?'));

const ulElem = document.createElement('ul');
targetElem.append(ulElem);



for(let i=startYear; i<=endYear; i++) {
    console.log('vuodet jota pitäisi kokeilla karkausvuodeksi ovat:', i);
    if (i % 4 === 0 && i % 100 !== 0 || i % 400 === 0) {
        console.log('Karkausvuodet ovat:', i);
        const newLi = document.createElement('li');
        newLi.innerText = `Karkausvuodet ovat: ${i}`;
        ulElem.append(newLi)
    }
}