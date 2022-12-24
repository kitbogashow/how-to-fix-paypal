// I hate this.

public class Line {
    private String word;
    private float conf;
    public Line(String word, float conf) {
        this.word = word;
        this.conf = conf;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public float getConf() {
        return conf;
    }

    public void setConf(float conf) {
        this.conf = conf;
    }
}
