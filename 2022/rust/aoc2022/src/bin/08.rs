use std::{cmp::max, collections::HashMap};

fn main() {
    let lines = include_str!("../../input/08").split('\n');
    let mut grid: HashMap<(usize, usize), u32> = HashMap::new();

    for (y, l) in lines.enumerate() {
        for (x, c) in l.chars().enumerate() {
            grid.insert((x, y), c.to_digit(10).unwrap());
        }
    }

    let (p1, p2) = grid
        .iter()
        .map(|(&pos, &h)| traverse(pos, h, &grid))
        .fold((0, 0), |(p1, p2), (visible, score)| {
            (p1 + visible as usize, max(p2, score))
        });

    println!("{}", p1);
    println!("{}", p2);
}

fn traverse(
    (x, y): (usize, usize),
    height: u32,
    grid: &HashMap<(usize, usize), u32>,
) -> (bool, usize) {
    let mut invisible = true;
    let mut score = 1;

    for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)] {
        let mut x = add_as_isize(x, dx);
        let mut y = add_as_isize(y, dy);
        let mut visible = true;
        let mut smaller_trees = 0;
        while let Some(&other) = grid.get(&(x, y)) {
            smaller_trees += 1;
            if other >= height {
                visible = false;
                break;
            }
            x = add_as_isize(x, dx);
            y = add_as_isize(y, dy);
        }
        if visible {
            invisible = false;
        }
        score *= smaller_trees;
    }

    (!invisible, score)
}

fn add_as_isize(a: usize, b: isize) -> usize {
    (a as isize + b) as usize
}
