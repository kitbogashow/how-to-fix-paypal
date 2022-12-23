import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.lang.Float;

public class Score_text {
    public static void main(String[] args) {
        try{
            File file = new File("words.csv");
            Scanner reader = new Scanner(file);
            ArrayList<Line> sus_words = new ArrayList<Line>();
            while (reader.hasNextLine()) {
                String currentLine = reader.nextLine();
                String[] currentValues = currentLine.split(",");
                try{
                    sus_words.add(new Line(currentValues[0], Float.parseFloat(currentValues[1])));
                } catch (NumberFormatException e) {
                    System.out.println ("Not a float");
                } catch (ArrayIndexOutOfBoundsException e) {
                    System.out.println ("Missing Value");
                }
            }

            try{
                reader = new Scanner(new File("invoices.txt"));

                int currentLineNumber = 0;
                while (reader.hasNextLine()) {
                    String currentLine = reader.nextLine();
                    currentLineNumber++;
                    float line_total_score = 0;
                    for(int i = 0; i<sus_words.size(); i++) {
                        if(currentLine.toLowerCase().contains(sus_words.get(i).getWord().toLowerCase())) {
                            line_total_score += sus_words.get(i).getConf();
                        }
                    }
                    System.out.println("Line" + (currentLineNumber+1) + ": " + line_total_score);
                }

            } catch (FileNotFoundException e) {
                System.out.println("invoices.txt not found");
                e.printStackTrace();
            }
        } catch (FileNotFoundException e) {
            System.out.println("words.csv not found");
            e.printStackTrace();
        }
    }
}

// Why did i do this? This is terrible!
