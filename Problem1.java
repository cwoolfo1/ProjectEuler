public class Problem1 {
    public static void main (String[] args){
        int[] myArray = new int[999];
        // creates array with 999 spots
        int i = 0;
        int x = 1;
        while (i<=998) {
            myArray[i] = x;
            i++;
            x++;
        }
        // assign a number to each cell in the array starting with one and increasing by one as it goes from cell to cell
        int y = 0;
        int number = 0;
        while (y<=998){
            if (myArray[y]%3 == 0 || myArray[y]%5 == 0) {
                number += myArray[y];
            }
            y++;

        }
    // determines if the number in a cell is a multiple of three or five
        // If it is a number of three or five then the value of that cell is added to the variable : number

        System.out.println("The sum of all multiples of 5 or 3 under 1000 is "+number);
        // prints the sum of every multiple of three or five under 1000
    }
}
