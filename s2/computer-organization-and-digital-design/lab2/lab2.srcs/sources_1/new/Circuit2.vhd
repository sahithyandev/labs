library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Circuit2 is
    Port ( g0 : in STD_LOGIC;
           g1 : in STD_LOGIC;
           g2 : in STD_LOGIC;
           g : inout STD_LOGIC;
           a : inout STD_LOGIC;
           r : out STD_LOGIC);
end circuit2;

architecture Behavioral of Circuit2 is

begin
    g <= (g0 AND g1 AND g2);    
    a<= not(g) and ((g0 AND g1) OR (g0 AND g2) OR (g1 AND g2));
    r <= not(g) and not(a);

end Behavioral;