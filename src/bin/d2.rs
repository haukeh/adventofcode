use aoc2024::file_lines;

enum Ordering {
    ASC,
    DESC,
}

fn main() -> anyhow::Result<()> {
    let lines = file_lines("input/d2.txt")?;

    let reports: Vec<_> = lines
        .map(|line| {
            line.split(' ')
                .map(|n| n.parse::<usize>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect();

    let p1 = reports
        .iter()
        .filter(|&report| check_report(report))
        .count();

    let p2 = reports
        .iter()
        .filter(|report| {
            let combinations: Vec<_> = (0..report.len())
                .map(|n| {
                    report[..n]
                        .iter()
                        .chain(report[n + 1..].iter())
                        .map(|&n| n)
                        .collect::<Vec<_>>()
                })
                .collect();

            check_report(report) || combinations.iter().filter(|&r| check_report(r)).count() > 0
        })
        .count();

    println!("{}", p1);
    println!("{}", p2);

    Ok(())
}

fn check_report(report: &[usize]) -> bool {
    let mut iter = report.iter().peekable();
    let mut ordering: Option<Ordering> = None;

    while let Some(current) = iter.next() {
        if let Some(&next) = iter.peek() {
            match ordering {
                Some(Ordering::ASC) => {
                    if next < current || !allowed_diff(*current, *next) {
                        return false;
                    }
                }
                Some(Ordering::DESC) => {
                    if next > current || !allowed_diff(*current, *next) {
                        return false;
                    }
                }
                None => {
                    ordering = if next > current {
                        Some(Ordering::ASC)
                    } else {
                        Some(Ordering::DESC)
                    };
                    if !allowed_diff(*current, *next) {
                        return false;
                    }
                }
            }
        }
    }

    return true;
}

fn allowed_diff(a: usize, b: usize) -> bool {
    let diff = a.abs_diff(b);
    return diff >= 1 && diff <= 3;
}
