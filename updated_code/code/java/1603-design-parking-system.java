package parking_system;

/**
 * @author Your Name
 * @since 2023-02-14
 */
public class ParkingSystem {

    private int big;
    private int medium;
    private int small;

    /**
     * Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
     * 
     * @param big   the number of big parking slots
     * @param medium the number of medium parking slots
     * @param small  the number of small parking slots
     */
    public ParkingSystem(int big, int medium, int small) {
        this.big = big;
        this.medium = medium;
        this.small = small;
    }

    /**
     * Checks whether there is a parking space of carType for the car that wants to get into the parking lot. 
     * carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively.
     * A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
     * 
     * @param carType the type of the car
     * @return whether there is a parking space available
     */
    public boolean addCar(int carType) {
        switch (carType) {
            case 1:
                return --big > 0;
            case 2:
                return --medium > 0;
            case 3:
                return --small > 0;
            default:
                return false;
        }
    }
}