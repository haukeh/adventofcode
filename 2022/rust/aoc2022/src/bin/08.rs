use itertools::Itertools;
use std::collections::HashMap;

fn main() {
    let lines = include_str!("../../input/08_t").split("\n").collect_vec();
    let mut grid: HashMap<(usize, usize), u32> = HashMap::new();

    for (y, l) in lines.iter().enumerate() {
        for (x, c) in l.chars().enumerate() {
            grid.insert((x, y), c.to_digit(10).unwrap());
        }
    }

    let max_y = lines.len();
    let max_x = grid.keys().map(|(x, _)| *x).max().unwrap();

    let grid = grid;

    println!("{:?}", grid);

    let visible = grid
        .iter()
        .filter(|&(&pos, &h)| is_visible(pos, h, max_x, max_y, &grid))
        .collect_vec();

    println!("{:?}", visible.len());
}

fn is_visible(
    (x, y): (usize, usize),
    height: u32,
    max_x: usize,
    max_y: usize,
    grid: &HashMap<(usize, usize), u32>,
) -> bool {
    if x == 0 || x == max_x || y == 0 || y == max_y {
        println!("({},{}) ({}) is visible", x, y, height);
        return true;
    }
    for xx in 0..max_x {
        if *grid.get(&(xx, y)).unwrap() > height {
            println!("({},{}) ({}) is not visible", x, y, height);
            return false;
        }
    }
    for yy in 0..max_y {
        if *grid.get(&(x, yy)).unwrap() > height {
            println!("({},{}) ({}) is not visible", x, y, height);
            return false;
        }
    }

    println!("({},{}) ({}) is visible", x, y, height);
    true
}
