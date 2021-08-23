function rangeOfNumbers(startNum, endNum) {
  if (endNum < 1) {
    return [];
  } else {
    const arr = rangeOfNumbers(startNum, endNum - 1);
    if (endNum >= startNum) {
      arr.push(endNum);
    }
    return arr;
  }
}

console.log(rangeOfNumbers(5, 6));
