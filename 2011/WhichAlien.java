package cc1jr;

import java.util.Scanner;

public class WhichAlien {

	public static void main(String[] args) {
		
		//*********************
		//Author: aarchi05
		//2011 J1 - Which Alien
		//*********************
		
		Scanner s = new Scanner(System.in);
		
		System.out.println("How many antennas?");
		int antennas = s.nextInt();
		
		System.out.println("How many eyes?");
		int eyes = s.nextInt();
		
		if (antennas >= 3 && eyes <= 4) {
			System.out.println("TroyMartian");
		}
		
		if (antennas <= 6 && eyes >= 2) {
			System.out.println("VladSaturnian");
		}
		
		if (antennas <= 2 && eyes <= 3) {
			System.out.println("GraemeMercurian");
		}
		

	}

}
