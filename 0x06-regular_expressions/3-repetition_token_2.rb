#!/usr/bin/env ruby

def match_repetition_token(arg)
  # Define the regular expression to match the repetition token
  regex = /hbt*n/

  # Use the scan method to find all occurrences of the regex in the argument
  matches = arg.scan(regex)

  # Print the matched occurrences
  puts matches.join('')
end

# Get the first command-line argument
arg = ARGV[0]

# Call the match_repetition_token method with the provided argument
match_repetition_token(arg)

