
class Sports{

    String getName(){
        return "Generic Sports";
    }
  
    void get_number_of_team_members(){
        System.out.println( "Each team has n players in " + getName() );
    }
}

class Soccer extends Sports{
    @Override
    String getName(){
        return "Soccer Class";
    }
    @Override
    void get_number_of_team_members(){
        System.out.println( "Each team has 11 players in " + getName() );

}}

public class Overriding{
	
    public static void main(String []args){
        Sports c1 = new Sports();
        Soccer c2 = new Soccer();
        System.out.println(c1.getName());
        c1.get_number_of_team_members();
        System.out.println(c2.getName());
        c2.get_number_of_team_members();
	}
}
