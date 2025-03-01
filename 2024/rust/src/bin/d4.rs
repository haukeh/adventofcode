use std::collections::HashMap;

use aoc2024::file_lines;

fn main() -> anyhow::Result<()> {
    let lines = file_lines("input/d4.txt")?;

    let grid: HashMap<(i64, i64), char> = lines
        .enumerate()
        .flat_map(|(y, line)| {
            let chars: Vec<_> = line.chars().collect();
            chars
                .into_iter()
                .enumerate()
                .map(move |(x, v)| ((x as i64, y as i64), v))
        })
        .collect();

    let (mut p1, mut p2) = (0, 0);

    for (&pos, &c) in &grid {
        if c == 'X' {
            p1 += find_xmas(pos, &grid);
        }
        if c == 'A' {
            p2 += find_x_mas(pos, &grid);
        }
    }

    println!("{}", p1);
    println!("{}", p2);

    Ok(())
}

fn find_x_mas(pos: (i64, i64), grid: &HashMap<(i64, i64), char>) -> usize {
    let (x, y) = pos;

    let tr = grid.get(&(x + 1, y + 1));
    let br = grid.get(&(x + 1, y - 1));
    let bl = grid.get(&(x - 1, y - 1));
    let tl = grid.get(&(x - 1, y + 1));

    match (tr, bl, tl, br) {
        (Some('S'), Some('M'), Some('M'), Some('S')) => 1,
        (Some('M'), Some('S'), Some('S'), Some('M')) => 1,
        (Some('S'), Some('M'), Some('S'), Some('M')) => 1,
        (Some('M'), Some('S'), Some('M'), Some('S')) => 1,
        _ => 0,
    }
}

fn find_xmas(pos: (i64, i64), grid: &HashMap<(i64, i64), char>) -> usize {
    let directions = [
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ];
 
    let mut found = 0;
    for (dx, dy) in directions {
        if is_valid(pos, dx, dy, grid) {
            found += 1;
        }
    }

    found
}

fn is_valid(pos: (i64, i64), dx: i64, dy: i64, grid: &HashMap<(i64, i64), char>) -> bool {
    let (mut x, mut y) = pos;
    
    for next in ['M', 'A', 'S'] {
        x += dx;
        y += dy;
        
        if grid.get(&(x, y)) != Some(&next) {
            return false;
        }
    }

    return true;
}
