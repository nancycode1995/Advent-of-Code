module.exports = (class Solution extends require("./solution.js") {
    partOne() {
        return this.input.match(/\(/g || []).length;
    }

    partTwo() {
        return 0;
    }
}).instantiate(1);
