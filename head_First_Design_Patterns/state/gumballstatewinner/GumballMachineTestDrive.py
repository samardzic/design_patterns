from GumballMachine import GumballMachine
from State import State


class GumballMachineTestDrive:
    
    @staticmethod
    def main(*args) -> None:
        gumballMachine: GumballMachine = GumballMachine(10)
            
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
            
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
            
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
            
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
            
        print(gumballMachine)
        
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
        gumballMachine.insertQuarter()
        gumballMachine.turnCrank()
            
        print(gumballMachine)
        
if __name__ == "__main__":
    GumballMachineTestDrive.main()