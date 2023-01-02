#!/bin/env ruby

bad_words = %w{cancel refund call helpdesk}
invoice = File.read('../invoices.txt')

puts "found %d different bad words" % bad_words.count { |word| invoice.include?(word) }
