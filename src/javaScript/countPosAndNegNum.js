function countPositivesSumNegatives(input){

    if (input == null){
      return [];
    }
  
    let count_positives = 0;
    let sum_negatives = 0;
    let inputLen = input.length;
    const result = [];

    if (inputLen === 0){
      
      return result;
    }
  
    for (let i = 0; i < inputLen; i++){

        if (input[i]>0){

            count_positives += 1;
        }

        if (input[i]<0){

            sum_negatives += input[i];
        }
    }

    result.unshift(sum_negatives);
    result.unshift(count_positives);
    return result;
}