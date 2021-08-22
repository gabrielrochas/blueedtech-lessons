var contacts = [
  {
      "firstName": "Akira",
      "lastName": "Laine",
      "number": "0543236543",
      "likes": ["Pizza", "Coding", "Brownie Points"]
  },
  {
      "firstName": "Harry",
      "lastName": "Potter",
      "number": "0994372684",
      "likes": ["Hogwarts", "Magic", "Hagrid"]
  },
  {
      "firstName": "Sherlock",
      "lastName": "Holmes",
      "number": "0487345643",
      "likes": ["Intriguing Cases", "Violin"]
  },
  {
      "firstName": "Kristian",
      "lastName": "Vos",
      "number": "unknown",
      "likes": ["JavaScript", "Gaming", "Foxes"]
  }
];

function checkName(name, prop) {
  contacts.forEach(contact => {
    let check;
    if(name != contact.firstName) {
      check = 'No such contact';
    }
    else if(!contact.hasOwnProperty(prop)) {
      check = 'No such property';
    }
    else {
      return 'contact.prop'
    }
    return check;
  });
}

console.log(checkName('Kristian', 'lastName'))