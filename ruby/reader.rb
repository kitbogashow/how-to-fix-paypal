# an abstract reader. Could be a file reader, mail reader, etc
class Reader
    attr_accessor :file_dir, :content
    
    def initialize(options={})
        @file_dir = options[:file_dir] || ""
    end

    def parse_content
        if @file_dir.length > 0
            begin
                file = File.open(@file_dir,"r")
                @content = file.read()
                file.close()
            rescue => exception
                puts "Error: Unable to read the file: #{@file_dir}"
            end
        end
    end

    def get_content
        return @content
    end
end