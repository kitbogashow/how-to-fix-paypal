import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Pattern;

public class FixPaypalRegex {
    private static final Pattern PATTERN = Pattern.compile("[0-9]{3,}|call|contact|\\\\+1");
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new FileReader("invoices.txt"))) {
            reader.lines().forEach(line -> {
                if (PATTERN.matcher(line).find()){
                    System.out.println("ඞ sus thing found: " + line);
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
