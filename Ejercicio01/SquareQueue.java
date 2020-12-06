import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class SquareQueue {
    public static void main(String[] args) {
        BlockingQueue<Integer> requests = new LinkedBlockingQueue<>();
        BlockingQueue<SquareResult> replies = new LinkedBlockingQueue<>();
        //creamos una iteracion para crearse varios procesos de Squarer
        int i=1;
        while(i<100) {
        	Squarer squarer = new Squarer(requests, replies);
            squarer.start();
            try {
                //realizamos una solicitud
            	requests.put(i);
                System.out.println(replies.take());
            } catch (InterruptedException ie) {
                ie.printStackTrace();
            }
            i++;
        }
    }
}
