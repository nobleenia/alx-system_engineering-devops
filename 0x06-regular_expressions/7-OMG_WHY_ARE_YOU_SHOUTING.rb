#!/usr/bin/env ruby
# Regular expression matching only capital letters

puts ARGV[0].scan(/[A-Z]/).join
