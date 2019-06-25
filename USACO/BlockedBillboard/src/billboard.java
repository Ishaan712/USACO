import java.io.*;
import java.util.*;


public class billboard {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("billboard.in"));
        PrintWriter printer = new PrintWriter(new BufferedWriter(new FileWriter("billboard.out")));

        StringTokenizer locations = new StringTokenizer(reader.readLine());
        int x1 = Integer.parseInt(locations.nextToken());
        int y1 = Integer.parseInt(locations.nextToken());
        int x2 = Integer.parseInt(locations.nextToken());
        int y2 = Integer.parseInt(locations.nextToken());


        locations = new StringTokenizer(reader.readLine());
        int x3 = Integer.parseInt(locations.nextToken());
        int y3 = Integer.parseInt(locations.nextToken());
        int x4 = Integer.parseInt(locations.nextToken());
        int y4 = Integer.parseInt(locations.nextToken());


        locations = new StringTokenizer(reader.readLine());
        int x5 = Integer.parseInt(locations.nextToken());
        int y5 = Integer.parseInt(locations.nextToken());
        int x6 = Integer.parseInt(locations.nextToken());
        int y6 = Integer.parseInt(locations.nextToken());

        int combinedArea = visibleAreaOfTwoBillbaords(x1, y1, x2, y2, x5, y5, x6, y6) + visibleAreaOfTwoBillbaords(x3, y3, x4, y4, x5, y5, x6, y6);

        printer.println(combinedArea);
        printer.close();
    }

    public static int areaOfARectangle(int x1, int y1, int x2, int y2) {
        return (x2-x1)*(y2-y1);
    }

    public static int visibleAreaOfTwoBillbaords(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4){

        int visibleAreaOfTwoBillbaords = areaOfARectangle(x1, y1, x2, y2);

        int leftbottomx = Math.max(x1, x3);
        int leftbottomy = Math.max(y1, y3);

        int toprightx = Math.min(x2, x4);
        int toprighty = Math.min(y2, y4);

        if(leftbottomx < toprightx && leftbottomy < toprighty){
            visibleAreaOfTwoBillbaords -= areaOfARectangle(leftbottomx, leftbottomy, toprightx, toprighty);
        }

        return visibleAreaOfTwoBillbaords;

    }
}