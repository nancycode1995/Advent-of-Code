module.exports = (class Solution extends require("./solution.js") {
    partOne() {
        return this.input.match(/\(/g || []).length - this.input.match(/\)/g || []).length;
    }

    partTwo() {
        return ([...this.input].map(character => character == "(" ? 1 : -1).map((sum => value => sum += value)(0))).findIndex(n => n < 0) + 1;
    }
}).instantiate(1);
