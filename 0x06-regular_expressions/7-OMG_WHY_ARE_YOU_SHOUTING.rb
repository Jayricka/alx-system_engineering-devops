#!/usr/bin/env ruby

def match_capital_letters(arg)
  # Define the regular expression to match only capital letters
  regex = /[A-Z]/

  # Use the scan method to find all occurrences of capital letters in the argument
  matches = arg.scan(regex)

  # Join the matched capital letters to form a single string
  result = matches.join('')

  # Print the result (matched capital letters)
  puts result
end

# Get the first command-line argument
arg = ARGV[0]

# Call the match_capital_letters method with the provided argument
match_capital_letters(arg)

