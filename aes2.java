import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.Scanner;

class aes2 {

    public static void main(String[] args) {
        try {
            // Get user input for the text to be encrypted
            Scanner scanner = new Scanner(System.in);
            System.out.println("Enter the text to be encrypted:");
            String originalText = scanner.nextLine();

            // Generate a secret key for AES
            SecretKey secretKey = generateAESKey();

            // Encrypt the text
            String encryptedText = encrypt(originalText, secretKey);
            System.out.println("Encrypted Text: " + encryptedText);

            // Decrypt the text
            String decryptedText = decrypt(encryptedText, secretKey);
            System.out.println("Decrypted Text: " + decryptedText);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static SecretKey generateAESKey() throws Exception {
        // Generate a key using AES algorithm
        KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
        keyGenerator.init(128); // 128-bit key size
        return keyGenerator.generateKey();
    }

    private static String encrypt(String text, SecretKey secretKey) throws Exception {
        // Create Cipher instance and initialize it for encryption
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);

        // Encrypt the text
        byte[] encryptedBytes = cipher.doFinal(text.getBytes());

        // Encode the encrypted bytes to base64 for better representation
        return Base64.getEncoder().encodeToString(encryptedBytes);
    }

    private static String decrypt(String encryptedText, SecretKey secretKey) throws Exception {
        // Create Cipher instance and initialize it for decryption
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.DECRYPT_MODE, secretKey);

        // Decode the base64 representation and decrypt
        byte[] encryptedBytes = Base64.getDecoder().decode(encryptedText);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);

        // Convert the decrypted bytes to string
        return new String(decryptedBytes);
    }
}
