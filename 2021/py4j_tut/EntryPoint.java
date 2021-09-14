import py4j.GatewayServer;

public class EntryPoint{

    private YourJavaClass yourJavaObj;

    public EntryPoint(){
        yourJavaObj = new YourJavaClass();

    }

    public YourJavaClass getYourJavaClass (){
        return yourJavaObj;
    }

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new EntryPoint(), 25536);
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }
}
