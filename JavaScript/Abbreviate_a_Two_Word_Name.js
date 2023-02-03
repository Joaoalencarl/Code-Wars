/* Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this: */

function abbrevName(name){
    const words = name.split(" ");
    const firstLetter = words[0][0];
    const secondLetter = words[1][0];
    return `${firstLetter}.${secondLetter}`.toUpperCase();
  }
  