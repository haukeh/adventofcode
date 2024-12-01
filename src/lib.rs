use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;

pub fn file_lines(filename: &str) -> io::Result<impl Iterator<Item = String>> {
    let project_dir = env!("CARGO_MANIFEST_DIR");
    let file_path = Path::new(project_dir).join(filename);
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);
    Ok(reader.lines().map(|l| l.unwrap()))
}
