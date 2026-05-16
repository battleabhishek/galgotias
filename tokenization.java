//breaking of text "this is class of nlp"."this is intresting" in words sentence reger twitter.
package sem4.nlp;

public class tokenization {
    public static void main(String[] args) {
        String text = "this is class of nlp. this is intresting";
        String[] tokens = text.split(" ");
        for (String token : tokens) {
            System.out.println(token);
        }
    }
}


