use std::io::{BufReader, BufRead};
use std::fs::File;


pub fn a() {
    // Read file, convert each line from string to int32, and store in vector
    let file = File::open("data/day2.txt").unwrap();
    let reader = BufReader::new(file);
    let mut score = 0;
    for line in reader.lines() {
        let line_content = line.unwrap();
        match line_content.as_str() {
            "A X" => score += 3+1,
            "A Y" => score += 6+2,
            "A Z" => score += 0+3,
            "B X" => score += 0+1,
            "B Y" => score += 3+2,
            "B Z" => score += 6+3,
            "C X" => score += 6+1,
            "C Y" => score += 0+2,
            "C Z" => score += 3+3,
            &_ => println!("Invalid line"),
        }
    }
    println!("Your score is {}", score);
}

pub fn b() {
    // Read file, convert each line from string to int32, and store in vector
    let file = File::open("data/day2.txt").unwrap();
    let reader = BufReader::new(file);
    let mut score = 0;
    for line in reader.lines() {
        let line_content = line.unwrap();
        match line_content.as_str() {
            "A X" => score += 3+0,
            "A Y" => score += 1+3,
            "A Z" => score += 2+6,
            "B X" => score += 1+0,
            "B Y" => score += 2+3,
            "B Z" => score += 3+6,
            "C X" => score += 2+0,
            "C Y" => score += 3+3,
            "C Z" => score += 1+6,
            &_ => println!("Invalid line"),
        }
    }
    println!("Your score is {}", score);
}