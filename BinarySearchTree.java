import java.util.Stack;

class Node {
    int data;
    Node left = null;
    Node right = null;

    Node(int data){
        this.data = data;
    }
}

public class BinarySearchTree {
    Node root;
    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        tree.insert(5);
        tree.insert(10);
        tree.insert(2);
        tree.insert(30);
        tree.insert(13);

        tree.print();
    }   

    public void insert(int data){
        Node node = new Node(data);

        if(root == null){ 
            root = node;
        }else{
            Node parent = root; 
            Node current = root; 
            while(true){
                parent = current;
                if(data < current.data){ 
                    current = current.left;
                    if(current == null){
                        parent.left = node;
                        break;
                    }
                }else{
                    current = current.right;
                    if(current == null){
                        parent.right = node;
                        break;
                    }
                }
            }
        }
    }

    public void print(){
        Stack <Node> stack = new Stack<>();
        Node current = root;

        while(current != null || !stack.empty()){
            if(current != null){
                stack.push(current);
                current = current.left;
            }else{
                current = stack.pop();
                System.out.println(current.data);
                current = current.right;
            }
        }
    }

    public Node search(int number){
        Node current = root;
        while(current.data != number){
            if(number < current.data){
                current = current.left;
            }else{
                current = current.right;
            }
            if(current == null){
                return null;
            }

        }
        return current;
    }
}
