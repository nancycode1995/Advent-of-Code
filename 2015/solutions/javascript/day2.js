class Present {
    constructor(length, width, height) {
        this.length = parseInt(length);
        this.width = parseInt(width);
        this.height = parseInt(height);
    }

    static fromString(string) {
        return new this(...string.trim().split(/x/g));
    }

    get dimensions() {
        return [this.length, this.width, this.height];
    }

    get sides() {
        return this.dimensions.flatMap((x, i) => this.dimensions.slice(i + 1).map(y => [x, y]));
    }

    get surfaceAreas() {
        return this.sides.map(side => side.reduce((a, b) => a * b, 1));
    }

    get perimeters() {
        return this.sides.map(side => 2 * side.reduce((a, b) => a + b, 0));
    }

    get volume() {
        return this.dimensions.reduce((a, b) => a * b, 1);
    }

    get requiredPaper() {
        const surfaceAreas = this.surfaceAreas;
        const smallest = Math.min(...surfaceAreas);
        return 2 * surfaceAreas.reduce((a, b) => a + b, 0) + smallest;
    }

    get requiredRibbon() {
        const smallest = Math.min(...this.perimeters);
        return smallest + this.volume;
    }
}

module.exports = (class Solution extends require("./solution.js") {
    get presents() {
        return this.lines.map(line => Present.fromString(line));
    }

    partOne() {
        return this.presents.map(present => present.requiredPaper).reduce((a, b) => a + b, 0)
    }

    partTwo() {
        return this.presents.map(present => present.requiredRibbon).reduce((a, b) => a + b, 0)
    }
}).instantiate(2);
