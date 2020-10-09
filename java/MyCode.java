// // package whatever; // don't place package name!

import java.io.*;
import java.util.ArrayList;

class MyCode {
	public static void main (String[] args) {
	System.out.println("Hello Java");
    BasicJava test = new BasicJava();
    test.oneTo255();
	}
}





class BasicJava {
    public void oneTo255() {
        for(int i=0; i<=255; i++){
            System.out.println(i);
        }
    }
}


