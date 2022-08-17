#!/usr/bin/env node

const days = [...Array(25).keys()].map(i => require(`./day${i + 1}.js`));

function run(day, part) {
    console.log("Welcome to Nancy's Advent of Code 2015 solutions! :-)");
    if (day) {
        if (1 <= day && day <= 25) {
            const solution = days[day - 1];
            if (part) {
                if (part == 1)
                    solution.runOne();
                else if (part == 2)
                    solution.runTwo();
                else {
                    console.error(`There is no such part ${part}!`);
                    process.exit(1)
                }
            } else
                solution.run();
        } else {
            console.error(`There is no such day ${day}!`);
            process.exit(1)
        }
    } else
        days.forEach((day, i) => {
            console.log(`Day ${i + 1}:`);
            day.run();
        });
}

function main(cmd, ...args) {
    if (args.length > 2) {
        console.error(`Usage: ${cmd} [day] [part]`);
        process.exit(1);
    } else
        run(...args);
}

if (require.main === module) {
    main(...process.argv.slice(1));
}

console.log("Test!");
