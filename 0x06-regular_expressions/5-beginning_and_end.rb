#!/usr/bin/env ruby

def match_beginning_and_end(arg)
  # Define the regular expression to match the required pattern
  regex = /^h.n$/

  # Use the match method to check if the entire string matches the regex
  match = arg.match(regex)

  # Print the match result
  puts match ? match[0] : ""
end

# Get the first command-line argument
arg = ARGV[0]

# Call the match_beginning_and_end method with the provided argument
match_beginning_and_end(arg)

