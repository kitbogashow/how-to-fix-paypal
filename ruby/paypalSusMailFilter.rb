class PayPalMailSusFilter
    attr_accessor :list_of_mails, :flagged_mails

    def initialize(options={})
        @list_of_mails = options[:list_of_mails] || ""
        @flagged_mails = Array.new
    end

    def find_suspicious_mails
        for mail in @list_of_mails do
            if mail.match(/[0-9]{3,}|call|contact|\+1/)
                @flagged_mails.push(mail)
            end
        end
    end

    def get_suspicious_mails
        return @flagged_mails
    end
end