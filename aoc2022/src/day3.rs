use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::HashSet;


pub fn a() {
    let file = File::open("data/day3.txt").unwrap();
    let reader = BufReader::new(file);
    let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let mut score = 0;
    for line in reader.lines() {
        let line_content = line.unwrap();

        let mut line_vec = line_content.chars().collect::<Vec<char>>();
        // Get first half of line_vec
        let first_half = line_vec.split_off(line_vec.len()/2);
        // Get second half of line_vec
        let second_half = line_vec;
        let compartment1 = HashSet::<_>::from_iter(first_half);
        let compartment2 = HashSet::<_>::from_iter(second_half);
        // Check overlap of compartments
        let overlap = compartment1.intersection(&compartment2).into_iter().collect::<String>();
        // get index of overlap in alphabet
        let point = alphabet.find(&overlap).unwrap()+1;
        score += point;
        println!("Letter: {}, Point: {}", overlap, point);
    }
    
    println!("The score is {}", score);
}


pub fn b() {
    let file = File::open("data/day3.txt").expect("File not found");
    let lines: Vec<String> = BufReader::new(file)
        .lines()
        .map(|l| l.expect("Could not read line"))
        .collect();

    let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let mut score = 0;
    for i in (0..lines.len()).step_by(3) {
        let elf1 = HashSet::<_>::from_iter(lines[i].chars().collect::<Vec<char>>());
        let elf2 = HashSet::<_>::from_iter(lines[i+1].chars().collect::<Vec<char>>());
        let elf3 = HashSet::<_>::from_iter(lines[i+2].chars().collect::<Vec<char>>());
        
        let intersection = (&((&elf1) & (&elf2))) & (&elf3);
        let overlap = intersection.into_iter().collect::<String>();
        let point = alphabet.find(&overlap).unwrap()+1;
        score += point;
    }
    
    println!("The score is {}", score);
}