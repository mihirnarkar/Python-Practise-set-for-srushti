import java.util.Scanner;

class House{
    String house_name="Enter name";
    double house_price=0;
}

class SampleQueSolution{
    public static void main(String[] args) {

        House house1 = new House();
        house1.house_name = "Kandivali";
        house1.house_price = 100;

        House house2 = new House();
        house2.house_name = "Lalbaugh";
        house2.house_price = 200;

        House house3 = new House();
        house3.house_name = "Panvel";
        house3.house_price = 20;

        System.out.println("Welcome to the House Price Checker!");

        System.out.println("Availaible houses: ");
        System.out.println("1. "+house1.house_name+" - "+house1.house_price);
        System.out.println("2. "+house2.house_name+" - "+house2.house_price);
        System.out.println("3. "+house3.house_name+" - "+house3.house_price);

        boolean boobs = true;
        while(boobs){
            System.out.println("Check house price: Enter 1");
            System.out.println("Exit the program: Enter 2");

            Scanner sc = new Scanner(System.in);
            int userChoice = sc.nextInt();

            if(userChoice == 1){
                System.out.println("Enter house name: ");
                String userHouse = sc.next(); // Kandivali 
                
                if(userHouse.equals(house1.house_name)){
                    System.out.println("Price : "+house1.house_price);
                }
                else if(userHouse.equals(house2.house_name)){
                     System.out.println("Price : "+house2.house_price);
                }
                else if(userHouse.equals(house3.house_name)){
                    System.out.println("Price: "+house3.house_price);
                }else{
                    System.out.println("Invalid house name go find room in kandivali village");
                }


            }
            else if(userChoice == 2){
                System.out.println("Exiting.....");
                boobs = false;
            }else{
                System.out.println("Invalid number");
            }
        }
    }
}



