use itertools::{Itertools};
use regex::{Regex};
use std::fs;

fn main() {
    let input = fs::read_to_string("input/05").unwrap();
    let (c, ins) = input.split("\n\n").collect_tuple().unwrap();

    let rows = c
        .rsplit('\n')
        .skip(1)
        .map(|row| row.chars().skip(1).step_by(4).collect_vec())
        .collect_vec();

    let max_len = rows.iter().map(|l| l.len()).max().unwrap();

    let mut grid: Vec<Vec<char>> = vec![Vec::new(); max_len];

    for row in rows {
        for (x, c) in row.into_iter().enumerate() {
            if !c.is_whitespace() {
                grid[x].push(c);
            }
        }
    }

    let instr = parse_instructions(ins);

    let part1 = part1(grid.clone(), &instr);
    let part2 = part2(grid, &instr);

    show(&part1);
    show(&part2);
}

fn show(grid: &Vec<Vec<char>>) {
    let s = grid.iter().map(|col| col.last().unwrap()).join("");
    println!("{}", s);
}

fn part1(mut grid: Vec<Vec<char>>, instr: &Vec<Instr>) -> Vec<Vec<char>> {
    for Instr(amount, from, to) in instr {
        for _ in 0..*amount {
            let x = grid[from - 1].pop().unwrap();
            grid[to - 1].push(x);
        }
    }
    grid
}

fn part2(mut grid: Vec<Vec<char>>, instr: &Vec<Instr>) -> Vec<Vec<char>>{
    for Instr(amount, from, to) in instr {
        let len = &grid[from-1].len();
        let mut mv = grid[from-1].drain(len-amount..).collect_vec();
        grid[to-1].append(&mut mv);
    }
    grid
}

#[derive(Debug)]
struct Instr(usize, usize, usize);

fn parse_instructions(ins: &str) -> Vec<Instr> {
    let re = Regex::new(r"^move (\d+) from (\d+) to (\d+)$").unwrap();

    ins.split('\n')
        .map(|instr| {
            let cap = re.captures(instr).unwrap();
            let amount = cap[1].parse::<usize>().unwrap();
            let from = cap[2].parse::<usize>().unwrap();
            let to = cap[3].parse::<usize>().unwrap();
            Instr(amount, from, to)
        })
        .collect_vec()
}
