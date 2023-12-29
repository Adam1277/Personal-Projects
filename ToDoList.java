import java.util.Scanner;

class Node{
    String task;
    Node next;

    Node(String task){
        this.task = task;
    }
}

public class ToDoList {
    //Features of a linkedlist to-do list
    //Need to have a insert and delete function
    //Needs to have a search function
    Node head;

    public void insert(String task){
        Node node = new Node(task);

        if(head == null){//Linkedlist is empty - set the head now at this created node
            this.head = node;
        }else{
            Node currentNode = this.head;

            while(currentNode.next != null){
                currentNode = currentNode.next;
            }
            currentNode.next = node;
        }
    }

    public void print(){
        if(head == null){
            System.out.println("Nothing to print.");
            return;
        }else{
            Node currentNode = this.head;

            while(currentNode != null){
                System.out.print(currentNode.task + " | ");
                currentNode = currentNode.next;
            }
            System.out.println("");
        }
    }

    public int search(String task) {
        if (this.head == null) {
            System.out.println("Nothing to search for.");
            return -1;
        }
    
        Node currentNode = this.head;
        int index = 0;
    
        while (currentNode != null) {
            if (currentNode.task.equals(task)) {
                return index;
            }
            currentNode = currentNode.next;
            index++;
        }
        return -1;
    }
    

    public void delete(String task) {
        if (this.head == null) {
            System.out.println("Nothing to delete.");
            return;
        }
        if (this.head.task.equals(task)) {
            this.head = this.head.next;
            return;
        }
    
        Node currentNode = this.head;
        while (currentNode.next != null && !currentNode.next.task.equals(task)) {
            currentNode = currentNode.next;
        }
        if (currentNode.next == null) {
            System.out.println("Task was not found");
        }else{
            currentNode.next = currentNode.next.next;
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Welcome to the terminal to-do list");
        System.out.println("task-> new task");
        System.out.println("del-> delete task");
        System.out.println("search-> search the linkedlist");
        System.out.println("print-> print the list");
        System.out.println("exit-> leave the program");
        System.out.println("----------------------------");
        
        Scanner scanner = new Scanner(System.in);
        ToDoList todo = new ToDoList();
        while(true){
            System.out.print("Please enter a command: ");
            String Userinput = scanner.nextLine();
            if(Userinput.equalsIgnoreCase("exit")){
                break;
            }else if(Userinput.equalsIgnoreCase("task")){
                System.out.print("Please enter your task: ");
                String task = scanner.nextLine();
                todo.insert(task);
            }else if(Userinput.equalsIgnoreCase("search")){
                System.out.print("Please enter the task you would like to search for: ");
                String search = scanner.nextLine();
                System.out.println("Task at index: " + todo.search(search));
            }else if(Userinput.equalsIgnoreCase("print")){
                todo.print();
            }else if(Userinput.equalsIgnoreCase("del")){
                System.out.print("Please enter the task you would like to delete: ");
                String del = scanner.nextLine();
                todo.delete(del);
            }
        } 
        scanner.close();
    }
}
