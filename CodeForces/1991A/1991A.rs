use std::cmp::max;
use std::io::{stdin, stdout, BufWriter, Write};

#[derive(Default)]
struct Scanner {
    buffer: Vec<String>,
}
impl Scanner {
    fn next<T: std::str::FromStr>(&mut self) -> T {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse().ok().expect("oh no failed to parse");
            }
            let mut input = String::new();
            stdin().read_line(&mut input).expect("eep i failed to read");
            self.buffer = input.split_whitespace().rev().map(String::from).collect();
        }
    }
}

#[allow(dead_code)]
fn main() {
    let mut scan = Scanner::default();
    let out = &mut BufWriter::new(stdout());
    let t: i32 = scan.next();

    for _t in 0..t {
        let n: i32 = scan.next();
        let mut record: i32 = scan.next();
        for _i in 0..((n - 1) / 2) {
            let _unused: i32 = scan.next();
            record = max(scan.next(), record);
        }
        writeln!(out, "{}", record).ok();
    }
}
