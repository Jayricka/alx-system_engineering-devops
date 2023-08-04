#!/usr/bin/env ruby

def match_phone_number(arg)
  # Define the regular expression to match a 10-digit phone number
  regex = /^[0-9]{10}$/

  # Use the match method to check if the entire string matches the regex
  match = arg.match(regex)

  # Print the match result
  puts match ? match[0] : ""
end

# Get the first command-line argument
arg = ARGV[0]

# Call the match_phone_number method with the provided argument
match_phone_number(arg)

