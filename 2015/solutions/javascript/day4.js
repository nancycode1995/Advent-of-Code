const crypto = require("crypto")

module.exports = (class Solution extends require("./solution.js") {
    findIndexOfHashMatching(predicate) {
        for (let i = 0;; i++)
            if (predicate(crypto.createHash("md5").update(this.input + i).digest("hex")))
                return i;
    }

    getSeed(startsWith) {
        return this.findIndexOfHashMatching(hash => hash.startsWith(startsWith))
    }

    partOne() {
        return this.getSeed("00000");
    }

    partTwo() {
        return this.getSeed("000000");
    }
}).instantiate(4);
