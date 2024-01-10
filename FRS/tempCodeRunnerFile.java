import javax.swing.*;
import java.awt.*;

public class ScrollablePageExample {
    public static void main(String[] args) {
        // Create a frame
        JFrame frame = new JFrame("Scrollable Page");
        frame.setSize(400, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create a panel for the content
        JPanel contentPanel = new JPanel();
        contentPanel.setLayout(new BoxLayout(contentPanel, BoxLayout.Y_AXIS));

        // Add some content to the panel
        for (int i = 1; i <= 30; i++) {
            contentPanel.add(new JLabel("Label " + i));
        }

        // Create a scroll pane for the content panel
        JScrollPane scrollPane = new JScrollPane(contentPanel);

        // Set up the frame with the scroll pane
        frame.getContentPane().add(scrollPane, BorderLayout.CENTER);

        // Display the frame
        frame.setVisible(true);
    }
}
