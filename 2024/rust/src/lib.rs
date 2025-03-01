use std::fs::{self, File};
use std::io::{self, BufRead, BufReader};
use std::path::Path;

pub fn file_lines(filename: &str) -> io::Result<impl Iterator<Item = String>> {
    let project_dir = env!("CARGO_MANIFEST_DIR");
    let file_path = Path::new(project_dir).join(filename);
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);
    Ok(reader.lines().map(|l| l.unwrap()))
}

pub fn file_as_string(filename: &str) -> io::Result<String> {
    let project_dir = env!("CARGO_MANIFEST_DIR");
    let file_path = Path::new(project_dir).join(filename);
    return fs::read_to_string(file_path);
}
