const fs = require("fs");

function readFile(path) {
    try {
        return fs.readFileSync(path, "utf8");
    } catch (error) {
        console.error(`Unable to open file "${path}"!`);
        process.exit(1);
    }
}

module.exports = class Solution {
    constructor(input, answerOne, answerTwo) {
        this.input = input;
        this.answerOne = answerOne;
        this.answerTwo = answerTwo;
    }

    static fromPaths(pathInput, pathAnswerOne, pathAnswerTwo) {
        return new this(readFile(pathInput), readFile(pathAnswerOne), readFile(pathAnswerTwo));
    }

    static instantiate(day) {
        const pathInput = `../../inputs/${day}.txt`;
        const pathAnswerOne = `../../answers/${day}.1.txt`;
        const pathAnswerTwo = `../../answers/${day}.2.txt`;
        return this.fromPaths(pathInput, pathAnswerOne, pathAnswerTwo);
    }

    /**
     * Return the answer to part one of this day's solution.
     */
    partOne() {}

    /**
     * Return the answer to part one of this day's solution.
     */
    partTwo() {}

    /**
     * Perform a test of part one and print the result to console.
     */
    runOne() {
        console.log("Solving part one...");
        const answer = this.partOne();
        if (answer == this.answerOne) {
            console.log(`Result: ${answer} (CORRECT)`);
        } else {
            console.log(`Result: ${answer} (INCORRECT; should be ${this.answerOne})`);
        }
    }

    /**
     * Perform a test of part two and print the result to console.
     */
    runTwo() {
        console.log("Solving part two...");
        const answer = this.partTwo();
        if (answer == this.answerTwo) {
            console.log(`Result: ${answer} (CORRECT)`);
        } else {
            console.log(`Result: ${answer} (INCORRECT; should be ${this.answerTwo})`);
        }
    }

    /**
     * Perform a test of both parts and print the results to console.
     */
    run() {
        this.runOne();
        this.runTwo();
    }
}
