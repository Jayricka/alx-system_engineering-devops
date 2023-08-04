#!/usr/bin/env ruby

def extract_transaction_info(log)
  # Define the regular expression pattern to extract the required information
  regex = /\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/

  # Use the scan method to find all occurrences of the regex in the log
  matches = log.scan(regex)

  # Print the matched occurrences in the desired format
  matches.each do |match|
    sender = match[0]
    receiver = match[1]
    flags = match[2]

    puts "#{sender},#{receiver},#{flags}"
  end
end

# Get the log content from the first command-line argument
log = ARGV[0]

# Call the extract_transaction_info method with the provided log
extract_transaction_info(log)

