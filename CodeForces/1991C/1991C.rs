// {{{ vEnhance's Rust competitive programming template
// I/O scanner from https://codeforces.com/blog/entry/67391
// vim: fdm=marker foldlevel=0

#[allow(unused_imports)]
use std::cmp::{max, min};
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
fn join<T, U>(v: U) -> String
where
    U: AsRef<[T]>,
    T: std::string::ToString,
{
    v.as_ref()
        .iter()
        .map(|elm| elm.to_string())
        .collect::<Vec<String>>()
        .join(" ")
}

// Copy of dbg! macro, but only when stomp is used and the flag debug is passed
// So we don't waste time printing to stderr when submitting to online judge
#[macro_export]
macro_rules! debug {
    () => {
        #[cfg(feature = "debug")]
        std::eprintln!("[{}:{}:{}]", std::file!(), std::line!(), std::column!())
    };
    ($val:expr $(,)?) => {
        #[cfg(feature = "debug")]
        match $val {
            tmp => {
                std::eprintln!("[{}:{}:{}] {} = {:#?}",
                    std::file!(), std::line!(), std::column!(), std::stringify!($val), &tmp);
                tmp
            }
        }
    };
    ($($val:expr),+ $(,)?) => {
        #[cfg(feature = "debug")]
        ($(std::dbg!($val)),+,)
    };
}
/* }}} */

#[allow(dead_code)]
fn main() {
    let mut scan = Scanner::default();
    let out = &mut BufWriter::new(stdout());

    let t: i64 = scan.next();
    #[allow(unused_labels)]
    'test_case_loop: for _test_case_number in 0..t {
        let n: usize = scan.next();
        let mut a: Vec<i64> = (0..n).map(|_| scan.next()).collect();
        let mut m: i64 = a[0];
        if n == 1 {
            writeln!(out, "{}", 1).ok();
            writeln!(out, "{}", a[0]).ok();
            continue 'test_case_loop;
        }
        for i in 1..n {
            if a[i] % 2 != a[0] % 2 {
                writeln!(out, "{}", -1).ok();
                continue 'test_case_loop;
            }
            m = max(a[i], m);
        }

        let mut ans: Vec<i64> = Vec::new();
        let mut k = 0;
        while m > 0 {
            let offset = (m + 1) / 2;
            ans.push(offset);
            m = 0;
            for ai in a.iter_mut() {
                *ai = (*ai - offset).abs();
                m = max(*ai, m);
            }
            k += 1;
            assert!(k <= 40);
        }
        writeln!(out, "{}", k).ok();
        writeln!(out, "{}", join(&ans)).ok();
    }
}
