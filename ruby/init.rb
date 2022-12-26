# Main driver of the application
require_relative "./reader.rb"
require_relative "./paypalSusMailFilter.rb"

file_reader = Reader.new(:file_dir => "../invoices.txt")
file_reader.parse_content()

contents = file_reader.get_content()

# converting file content into an array
mails = contents.split("\n")

scam_detector = PayPalMailSusFilter.new(:list_of_mails => mails)

scam_detector.find_suspicious_mails()

sus_emails = scam_detector.get_suspicious_mails()

for email in sus_emails do
    puts "#{email}"
end
