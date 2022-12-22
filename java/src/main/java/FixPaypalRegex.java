import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;

public class FixPaypalRegex {

    public static void main(String[] args) {
        BufferedReader reader;

        try {
            reader = new BufferedReader(new FileReader("invoices.txt"));
            String line = reader.readLine();

            while (line != null) {
                if (Pattern.compile("([0-9]{3,}|call|contact|\\\\+1)").matcher(line).find()){
                    System.out.println("ඞ sus thing found: " + line);
                }
                line = reader.readLine();
            }

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
