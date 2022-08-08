package test01.EX01;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B {
	private int a=10;

	public int getA() {
		return a;
	}

	public void setA(int a) {
		this.a = a;
	}
	
	public void click() { 
		try {
			String z1= " User";
			String z2 = "E:\\JAVA_STUDY\\IDE_STD\\test01\\src\\test01\\EX01\\test_bat.bat".concat(z1);
			System.out.println(z2);
		    Process p = Runtime.getRuntime().exec(z2);
		    
		    BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
		    String line = null;
		    
		    while ((line = br.readLine()) != null) {
		      System.out.println(line);
		    }
		  } catch (Exception e) {
		    System.err.println(e);
		  }
		
	}
	
}
