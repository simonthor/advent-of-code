use std::io::{BufReader, BufRead};
use std::fs::File;


pub fn a() {
    // Read file, convert each line from string to int32, and store in vector
    // Create vector of vectors
    let mut numbers: Vec<i32> = vec![0];
    let file = File::open("data/day1.txt").unwrap();
    let reader = BufReader::new(file);
    let mut i = 0;
    for line in reader.lines() {
        // If line is empty, add one to i and continue
        let line_content = line.unwrap();
        if line_content.is_empty() {
            i += 1;
            numbers.push(0);
            continue;
        }
        // Convert line to int32 and add to vector
        let number: i32 = line_content.parse().unwrap();
        numbers[i] += number;
    }
    let max_value = numbers.iter().max();
    match max_value {
        Some(max) => println!( "The maximum value is: {} calories", max),
        None      => println!( "Vector is empty" ),
    }
}


pub fn b() {
    // Read file, convert each line from string to int32, and store in vector
    // Create vector of vectors
    let mut numbers: Vec<i32> = vec![0];
    let file = File::open("data/day1.txt").unwrap();
    let reader = BufReader::new(file);
    let mut i = 0;
    for line in reader.lines() {
        // If line is empty, add one to i and continue
        let line_content = line.unwrap();
        if line_content.is_empty() {
            i += 1;
            numbers.push(0);
            continue;
        }
        // Convert line to int32 and add to vector
        let number: i32 = line_content.parse().unwrap();
        numbers[i] += number;
    }
    numbers.sort();
    let len = numbers.len();
    println!("The sum of the top 3 elf calories are {}", numbers[len - 1] + numbers[len - 2] + numbers[len - 3])
}