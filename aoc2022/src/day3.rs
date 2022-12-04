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