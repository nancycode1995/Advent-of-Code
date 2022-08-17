class Region {
    constructor(a, b) {
        this.a = a;
        this.b = b;
    }

    /**
     * Iterate over all combinations of coordinates within the region
     */
    iterate() {
        function *combos(min, max) {
            if (min.length > 0 && max.length > 0)
                for (let i = min[0]; i <= max[0]; i++)
                    for (const rest of combos(min.slice(1), max.slice(1)))
                        yield [i].concat(rest);
            else
                yield [];
        }
        return combos(this.a, this.b);
    }
}

class Instruction {
    /**
     * Construct the instruction given the coordinates of the coordinates of the region that it affects.
     */
    constructor(a, b) {
        this.region = new Region(a, b);
    }

    /**
     * Parse a string designating an instruction.
     */
    static fromString(string) {
        const instructionTypes = {
            "turn on": InstructionTurnOn,
            "turn off": InstructionTurnOff,
            "toggle": InstructionToggle,
        };
        let [left, right] = string.split(/\s+through\s+/g);
        const b = right.split(",").map(x => parseInt(x));
        left = left.split(/\s+/g);
        right = left.pop();
        const opcode = left.join(" ");
        const a = right.split(",").map(x => parseInt(x));
        return new instructionTypes[opcode](a, b);
    }

    /**
     * Apply the instruction to the entire range.
     */
    execute(grid) {
        for (const x of this.region.iterate())
            grid.set(x, this.operate(grid.get(x)));
    }

    /**
     * Return the new light state given the old one.
     */
    operate(state) {}
}

class InstructionTurnOn extends Instruction {
    operate(state) {
        return typeof state == "boolean" ? true : state + 1;
    }
}

class InstructionTurnOff extends Instruction {
    operate(state) {
        return typeof state == "boolean" ? false : Math.max(0, state - 1);
    }
}

class InstructionToggle extends Instruction {
    operate(state) {
        return typeof state == "boolean" ? !state : state + 2;
    }
}

class Grid {
    constructor(fill, dimensions, values) {
        this.dimensions = dimensions;
        const size = dimensions.reduce((a, b) => a * b, 1);
        this.values = values || new Array(size).fill(fill);
    }

    index(coordinates) {
        const bases = [1].concat(this.dimensions).map((product => value => product = product * value)(1));
        return coordinates.reduce((a, b, i) => a + b * bases[i], 0);
    }

    get(coordinates) {
        return this.values[this.index(coordinates)];
    }

    set(coordinates, value) {
        this.values[this.index(coordinates)] = value;
    }
}

module.exports = (class Solution extends require("./solution.js") {
    get instructions() {
        return this.lines.map(Instruction.fromString);
    }

    partOne() {
        const grid = new Grid(false, [1000, 1000]);
        this.instructions.forEach(instruction => instruction.execute(grid));
        return grid.values.filter(x => x).length;
    }

    partTwo() {
        const grid = new Grid(0, [1000, 1000]);
        this.instructions.forEach(instruction => instruction.execute(grid));
        return grid.values.reduce((a, b) => a + b, 0);
    }
}).instantiate(6);
