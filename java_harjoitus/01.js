const items = ['eka', 2, 3.3, [1, 2, 3], true];
console.log(items)

console.log(items[3]);
items[3] = 99;

console.log(items[3]);
items[9] = '10. alkion esimerkkiarvo';

console.log(items);

console.log(items[6]);

console.log(items.length);

console.log('Tulostetaan kaikkien alkioiden arvo for:lla');

for (let i=0; i<items.length; i++){
    console.log(i+1 + '. alkion arvo on ' + items[i]);
}

for (const item of items) {
    if (item !== undefined) {
    console.log(item)
    }
}

const names = ['Frank', 'Scott', 'Jasmine', 'Don']


console.log(names);
names.sort();
console.log(names);

const ages = [13, 8, 102, 46];

console.log(ages);
ages.reverse();

console.log(ages);
names.push('Iines');

names.unshift('Hessu');
console.log(names);

const lastNameInArr = names.pop();

console.log('taulukosta poistettiin', lastNameInArr);
console.log(names);

console.log(names.includes('Iines'));
console.log(names.includes('Don'));

const person = {name: "Iines", age: 34}

console.log('person olio', person);
//ominaisuuksien arvojen muuttaminen
person['age'] = 36;
//ominaisuuksien (property) lisääminen
person.name = 'Iines Ankka';
person.profession = 'student';
console.log('person päivitetty', person);
//tiettyyn ominaisuuden arvon hakeminen
console.log(person.name + ' on ' + person.age + '-vuotias.');

const person2 = {
    name: "Iines",
    age: 34,
    getInfo: function () {
        return this.name + ' on ' + this.age + '-vuotias.';
    },
}
console.log(person2.getInfo());




