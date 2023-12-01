use std::collections::HashMap;

fn main() {
    let input_str = include_str!("input");
    part_1(input_str);
}

fn part_1(input_str: &str) {
    let mut input_list: Vec<u32> = vec![];

    let mut digits: Vec<char> = vec![];

    for character in input_str.chars() {
        if character.is_digit(10) {
            digits.push(character);
        }
        if character == '\n' {
            let mut two_digits: String = Default::default();
            let last_index;
            if digits.len() == 1 {
                last_index = 0;
            } else {
                last_index = digits.len() - 1;
            }
            two_digits.push(digits[0]);
            two_digits.push(digits[last_index]);
            input_list.push(two_digits.parse().unwrap());
            digits.clear();
        }
    }

    let mut answer = 0;
    for number in input_list {
        answer += number;
    }

    println!("{answer}");
}

fn part_2(input_str: &str) {

}
