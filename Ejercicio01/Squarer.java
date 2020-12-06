import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

class Squarer {
    
    private final BlockingQueue<Integer> in;
    private final BlockingQueue<SquareResult> out;

    public Squarer(BlockingQueue<Integer> requests, BlockingQueue<SquareResult> replies) {
        this.in = requests;
        this.out = replies;
    }
    
    /**
     * La funcion start nos inicia creando un hilo el cual lo va ejecutar en un proceso
     */
    public void start() {
        new Thread(new Runnable() {
            public void run() {
                while (!Thread.interrupted()) {
                    try {
                        //esperamos una solicitud, sino llega alguna se mantiene bloqueado
                        int x = in.take();
                        //Al recibir algun valor primero la identificamos que no sea un valor de pare
                        //para eso empleamos una condicion de identificacion
                        if(x!=42) {
                        	//si el numero es muy diferente al valor de pare se sigue el proceso
                            int y = x * x;
                            out.put(new SquareResult(x, y));
                        }else {
                        	//si el valor de bloqueo es detectado el hilo se interrumpe
                        	Thread.interrupted();
                        }
                    } catch (InterruptedException ie) {
                        //se para todo proceso
                    	break;
                    }
                }
            }
        }).start();
    }
}

class SquareResult {
    private final int input;
    private final int output;
    
    public SquareResult(int input, int output) {
        this.input = input;
        this.output = output;
    }
    
    @Override public String toString() {
        return input + "^2 = " + output;
    }
}