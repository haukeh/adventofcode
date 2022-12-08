use itertools::Itertools;
use std::{collections::{HashMap, }, ops::Range};

fn main() {
    let lines = include_str!("../../input/08").split("\n").collect_vec();
    let mut grid: HashMap<(usize, usize), u32> = HashMap::new();

    for (y, l) in lines.iter().enumerate() {
        for (x, c) in l.chars().enumerate() {
            grid.insert((x, y), c.to_digit(10).unwrap());
        }
    }

    let max_y = lines.len();
    let max_x = lines.first().map(|l| l.bytes().len()).unwrap();

    let grid = grid;

    let p1 = grid
        .iter()
        .filter(|&(&pos, &h)| is_visible(pos, h, max_x, max_y, &grid))
        .collect_vec()
        .len();

    let p2 = grid
        .iter()
        .map(|(&pos, &h)| score(pos, h, max_x, max_y, &grid))
        .max()
        .unwrap();
    

    println!("{}", p1);
    println!("{}", p2);
}

fn measure(grid: &HashMap<(usize, usize), u32>, rng: impl Iterator<Item=(usize, usize)>, height: u32) -> usize {
    let mut ll = 0;
    for pos in rng {
        if let Some(&t) = grid.get(&pos) {
            ll += 1;
            if t >= height {
                break;
            }
        }
    }
    ll
}

fn score(
    (x, y): (usize, usize),
    height: u32,
    max_x: usize,
    max_y: usize,
    grid: &HashMap<(usize, usize), u32>,
) -> usize {
    println!("{:?}", (x, y));
    let res = if x == 0 || x == max_x - 1 || y == 0 || y == max_y - 1 {
        0
    } else {
        let left = measure(grid, (0..x).rev().map(|x| (x, y)), height);
        let right = measure(grid, (x + 1..max_x).map(|x| (x, y)), height);
        let top = measure(grid, (0..y).rev().map(|y| (x, y)), height);
        let bottom = measure(grid, (y + 1..max_y).map(|y| (x, y)), height);
        
        left * right * top * bottom
    };

    res
}

fn is_visible(
    (x, y): (usize, usize),
    height: u32,
    max_x: usize,
    max_y: usize,
    grid: &HashMap<(usize, usize), u32>,
) -> bool {
    let res = if x == 0 || x == max_x - 1 || y == 0 || y == max_y - 1 {
        true
    } else {
        let mut left = (0..x)
            .map(|idx| *grid.get(&(idx, y)).unwrap())
            .collect::<Vec<_>>();
        let mut right = (x + 1..max_x)
            .map(|idx| *grid.get(&(idx, y)).unwrap())
            .collect::<Vec<_>>();
        let mut top = (0..y)
            .map(|idx| *grid.get(&(x, idx)).unwrap())
            .collect::<Vec<_>>();
        let mut bottom = (y + 1..max_y)
            .map(|idx| *grid.get(&(x, idx)).unwrap())
            .collect::<Vec<_>>();

        let visible_left = left.iter().find(|&item| item >= &height).is_none();
        let visible_right = right.iter().find(|&item| item >= &height).is_none();
        let visible_top = top.iter().find(|&item| item >= &height).is_none();
        let visible_bottom = bottom.iter().find(|&item| item >= &height).is_none();

        let visible_horizontal = visible_left || visible_right;
        let visible_vertical = visible_top || visible_bottom;

        visible_horizontal || visible_vertical
    };

    res
}
