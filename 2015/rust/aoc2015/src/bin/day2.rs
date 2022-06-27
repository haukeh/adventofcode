use std::cmp::min;
use std::fs::read_to_string;

#[derive(Debug)]
struct Rect {
    l: usize,
    w: usize,
    h: usize,
}

impl Rect {
    fn calculate_surface(&self) -> usize {
        let s1 = self.l * self.w;
        let s2 = self.w * self.h;
        let s3 = self.h * self.l;
        return 2 * s1 + 2 * s2 + 2 * s3 + min(s1, min(s2, s3));
    }

    fn calculate_min_perimeter(&self) -> usize {
        let s1 = self.l * 2 + self.w * 2;
        let s2 = self.w * 2 + self.h * 2;
        let s3 = self.h * 2 + self.l * 2;
        return min(s1, min(s2, s3));
    }

    fn calculate_volume(&self) -> usize {
        return self.l * self.w * self.h;
    }
}

fn main() {
    let input = read_to_string("input/d2.txt").unwrap();

    let recs: Vec<Rect> = input.lines()
        .map(|l| l.split('x').collect())
        .into_iter()
        .map(extract_rect)
        .collect();

    let part1: usize =
        recs.iter().map(|r| r.calculate_surface())
            .sum();

    let part2: usize = recs.iter().map(|r| r.calculate_min_perimeter() + r.calculate_volume()).sum();

    println!("{}", part1);
    println!("{}", part2);
}

fn extract_rect(row: Vec<&str>) -> Rect {
    match row[..] {
        [l, w, h] => Rect {
            l: l.parse::<usize>().unwrap(),
            w: w.parse::<usize>().unwrap(),
            h: h.parse::<usize>().unwrap(),
        },
        _ => panic!("Invalid row format")
    }
}
