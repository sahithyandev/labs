library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Circuit2Sim is

end Circuit2Sim;

architecture Behavioral of Circuit2Sim is
COMPONENT Circuit2
 PORT( g0, g1, g2 : IN STD_LOGIC;
 g, a, r : OUT STD_LOGIC);
 END COMPONENT;
 
 
SIGNAL g0, g1, g2 : std_logic;
SIGNAL g, a, r : std_logic;
  
begin
UUT: Circuit2 PORT MAP(
    g0 => g0,
    g1 => g1,
    g2 => g2,
    g => g,
    a => a,
    r => r
 );
 
 process
  begin
  g0 <= '0'; -- set initial values
  g1 <= '0';
  g2 <= '0';
  
  WAIT FOR 100 ns; -- after 100 ns change inputs
  g2 <= '1';
  
  WAIT FOR 100 ns; --change again
  g1 <= '1';
  g2 <= '0';
  
  WAIT FOR 100 ns; --change again
  g2 <= '1';
  
  WAIT FOR 100 ns; --change again
  g0 <= '1';
  g1 <= '0';
  g2 <= '0';
  
  WAIT FOR 100 ns; --change again
   g2 <= '1';
  
   WAIT FOR 100 ns; --change again
   g1 <= '1';
   g2 <= '0';
  
   WAIT FOR 100 ns; --change again
   g2 <= '1';
  
   WAIT; -- will wait forever
   end process;

end Behavioral;