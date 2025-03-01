use aoc2024::file_lines;
use itertools::Itertools;

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
        .filter(|&report| {
            check_report(report)
                || (0..report.len()).any(|n| {
                    let mut r = report.clone();
                    r.remove(n);
                    check_report(&r)
                })
        })
        .count();

    println!("{}", p1);
    println!("{}", p2);

    Ok(())
}

fn check_report(report: &[usize]) -> bool {
    let pairs: Vec<(&usize, &usize)> = report.iter().tuple_windows().collect();
    return (pairs.iter().all(|(a, b)| a > b) || pairs.iter().all(|(a, b)| a < b))
        && pairs.iter().all(|(&a, &b)| has_allowed_diff(a, b));
}

fn has_allowed_diff(a: usize, b: usize) -> bool {
    let diff = a.abs_diff(b);
    return diff >= 1 && diff <= 3;
}
