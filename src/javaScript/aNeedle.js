function findNeedle(haystack) {

    let message = "found the needle at position ";
    let haystackLen = haystack.length;
    
    for (let i = 0; i < haystackLen; i++){
    
        if (haystack[i] == "needle"){

            return (message + i.toString());
          }
    }
  }
  