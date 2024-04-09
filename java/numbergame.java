import java.util.Random;
import java.util.Scanner;

public class GuessTheNumberGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int minRange = 1;
        int maxRange = 100;
        int attempts = 0;
        int randomNumber = random.nextInt(maxRange - minRange + 1) + minRange;
        boolean guessedCorrectly = false;

        System.out.println("Welcome to the Number Game from the codsoft!");
        System.out.println("I have chosen a number between " + minRange + " and " + maxRange + ". Can you guess it?");

        while (!guessedCorrectly) {
            System.out.print("Enter your guess: ");
            int userGuess = scanner.nextInt();
            attempts++;

            if (userGuess < randomNumber) {
                System.out.println("Too low! Try again.");
            } else if (userGuess > randomNumber) {
                System.out.println("Too high! Try again.");
            } else {
                System.out.println("Congrats! You guessed the number " + randomNumber + " correctly in " + attempts + " attempts.");
                guessedCorrectly = true;
            }
        }

        scanner.close();
    }
}