package SDL_Project;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.Color;
import java.awt.event.ActionEvent;

public class Main extends JFrame {
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public static void main(String[] args) {
		JFrame frame = new JFrame("Button Click Game");
		frame.getContentPane().setBackground(Color.PINK);
		
		JLabel WelcomeLabel = new JLabel("Welcome to the Button Click Game");
		WelcomeLabel.setBounds(50, 0, 200, 30);
				
		JLabel label = new JLabel();
		label.setBounds(50, 50, 150, 30);
		
		JButton b1 = new JButton("A");
		b1.setBounds(50, 100, 130, 30);
		b1.setBackground(Color.YELLOW);
		frame.add(b1);
		b1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
						label.setText("Button A is clicked");
						label.setOpaque(true);
						label.setBackground(Color.YELLOW);
		}
		});
		
		JButton b2 = new JButton("B");
		b2.setBounds(50, 150, 130, 30);
		b2.setBackground(Color.GREEN);
		frame.add(b2);
		b2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
						label.setText("Button B is clicked");
						label.setOpaque(true);
						label.setBackground(Color.GREEN);
		}
		});
		
		JButton b3 = new JButton("C");
		b3.setBounds(50, 200, 130, 30);
		b3.setBackground(Color.CYAN);
		frame.add(b3);
		b3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
						label.setText("Button C is clicked");
						label.setOpaque(true);
						label.setBackground(Color.CYAN);
			}
		});
		
		frame.add(WelcomeLabel);
		frame.add(label);
		frame.setSize(300, 300);
		frame.setLayout(null);
		frame.setVisible(true);
}
}