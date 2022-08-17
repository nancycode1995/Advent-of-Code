const directions = {
    "<": [-1, 0],
    ">": [1, 0],
    "^": [0, -1,],
    "v": [0, 1,],
};

module.exports = (class Solution extends require("./solution.js") {
    get moves() {
        return [...this.input].map(character => directions[character]);
    }

    static path(moves) {
        return [[0, 0]].concat(moves.map((sum => value => sum = sum.map((n, i) => n + value[i]))([0, 0])));
    }

    get path() {
        return Solution.path(this.moves);
    }

    static deinterlace(array) {
        return [
            array.filter((_, i) => i % 2 == 0),
            array.filter((_, i) => i % 2 == 1),
        ];
    }

    /**
     * De-interlace Santa's and Robo-Santa's paths.
     */
    get paths() {
        return Solution.deinterlace(this.moves).map(Solution.path);
    }

    /**
     * How many presents each house at each coordinate receives given a path to follow.
     */
    static occurrences(path) {
        return path.reduce((occurrences, x) => {
            occurrences[x] = (occurrences[x] || 0) + 1;
            return occurrences;
        }, {});
    }

    partOne() {
        return Object.keys(Solution.occurrences(this.path)).length;
    }

    partTwo() {
        return Object.keys(Object.assign({}, ...this.paths.map(Solution.occurrences))).length;
    }
}).instantiate(3);
