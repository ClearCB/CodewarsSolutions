function sum (numbers) {

    let numbersLen = numbers.length;
    let count = 0;

    for (let i = 0; i < numbersLen; i++) {

        count += numbers[i];

    }
    
    return count;
}