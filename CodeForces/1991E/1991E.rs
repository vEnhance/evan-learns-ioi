// Template based on https://codeforces.com/blog/entry/67391
#[allow(unused_imports)]
use std::cmp::{max, min};
use std::collections::VecDeque;
use std::io::{stdin, stdout, BufWriter, Write};

const MAX: usize = 10009;

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

fn debug<T>(value: T)
where
    T: std::fmt::Debug, // T must implement the Debug trait
{
    #[cfg(feature = "debug")]
    dbg!(value);
}

fn get_two_coloring(graph: &Vec<Vec<usize>>) -> Option<[Option<bool>; MAX]> {
    let mut two_coloring = [None; MAX];
    let mut queue: VecDeque<usize> = VecDeque::new();
    queue.push_front(1);
    two_coloring[1] = Some(true);
    while !queue.is_empty() {
        let u: usize = queue.pop_front().unwrap();
        let c1: bool = two_coloring[u].unwrap();
        for v in &graph[u] {
            if let Some(c2) = two_coloring[*v] {
                if c2 == c1 {
                    return None;
                }
            } else {
                two_coloring[*v] = Some(!c1);
                queue.push_front(*v);
            }
        }
    }
    Some(two_coloring)
}

#[allow(dead_code)]
fn main() {
    let mut scan = Scanner::default();
    let out = &mut BufWriter::new(stdout());

    let t: i32 = scan.next();
    for _test_case_counter in 0..t {
        let n: usize = scan.next();
        let m: usize = scan.next();
        let mut graph_edges: Vec<Vec<usize>> = vec![Vec::new(); MAX];
        for _edge_counter in 0..m {
            let u = scan.next::<usize>();
            let v = scan.next::<usize>();
            graph_edges[u].push(v);
            graph_edges[v].push(u);
        }
        let coloring = get_two_coloring(&graph_edges);
        debug(n);

        if let Some(coloring) = coloring {
            writeln!(out, "{}", "Bob").ok();
            out.flush().ok();

            let mut left_vertices: Vec<usize> = Vec::new();
            let mut right_vertices: Vec<usize> = Vec::new();
            {
                for v in 1..=n {
                    if coloring[v].unwrap() {
                        left_vertices.push(v);
                    } else {
                        right_vertices.push(v);
                    }
                }
            }

            for _ in 0..n {
                let c1: i8 = scan.next();
                let c2: i8 = scan.next();
                let w: usize;

                if !left_vertices.is_empty() && (c1 == 1 || c2 == 1) {
                    w = left_vertices.pop().unwrap();
                    writeln!(out, "{} 1", w).ok();
                    out.flush().ok();
                } else if !right_vertices.is_empty() && (c1 == 3 || c2 == 3) {
                    w = right_vertices.pop().unwrap();
                    writeln!(out, "{} 3", w).ok();
                    out.flush().ok();
                } else {
                    match left_vertices.pop() {
                        Some(w) => {
                            writeln!(out, "{} 2", w).ok();
                            out.flush().ok();
                        }
                        None => {
                            w = right_vertices.pop().unwrap();
                            writeln!(out, "{} 2", w).ok();
                            out.flush().ok();
                        }
                    }
                }
            }
        } else {
            writeln!(out, "{}", "Alice").ok();
            out.flush().ok();
            for _ in 0..n {
                writeln!(out, "{}", "1 2").ok();
                out.flush().ok();
                let _: i32 = scan.next();
                let _: i32 = scan.next();
            }
        }
    }
}
