module.exports = (class Solution extends require("./solution.js") {
    partOne() {
        return this.lines.filter(string => {
            // has three vowels
            return (string.match(/[aeiou]/gi) || []).length >= 3;
        }).filter(string => {
            // has letter that appears twice in a row
            return string.match(/(.)\1/g);
        }).filter(string => {
            // does not contain certain strings
            return string.match(/(ab|cd|pq|xy)/g) == null;
        }).length;
    }

    partTwo() {
        return this.lines.filter(string => {
            // has three vowels
            return string.match(/(..).*\1/g);
        }).filter(string => {
            // has letter that repeats after a previous letter
            return string.match(/(.).\1/g);
        }).length;
    }
}).instantiate(5);
