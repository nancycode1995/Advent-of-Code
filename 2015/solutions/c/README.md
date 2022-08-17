# Advent of Code 2015 in C

Here are my complete solutions for year 2015 of Advent of Code written in C. ^.^

## How to run it

You can calculate the answers to both parts of all days in order like this:
```bash
make test
```

If you want to calculate the answers to both parts of a particular day (say, day 15) you can do so like this:
```bash
make test DAY=15
```

You can even calculate the answer only to a particular part (say, part 2) of a particular day (say, day 7) like this:
```bash
make test DAY=7 PART=2
```

The above invocations will always test calculated answers against the known answers found in `../../answers/`.
