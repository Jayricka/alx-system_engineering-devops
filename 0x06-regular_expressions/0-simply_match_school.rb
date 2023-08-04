#!/usr/bin/env ruby

def match_school(arg)
  # Define the regular expression to match "School" using Oniguruma syntax
  regex = /School/

  # Use the scan method to find all occurrences of the regex in the argument
  matches = arg.scan(regex)

  # Print the matched occurrences
  puts matches.join('')
end

# Get the first command-line argument
arg = ARGV[0]

# Call the match_school method with the provided argument
match_school(arg)

