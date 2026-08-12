------------------------------------------------------------------------------
-- Engineer: Sahithyan K.
------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;
-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity TB_Multiplier_2 is
-- Port ( );
end TB_Multiplier_2;

architecture Behavioral of TB_Multiplier_2 is
component Multiplier_2 is
    Port(
        A: IN STD_LOGIC_VECTOR(1 downto 0);
        B: IN STD_LOGIC_VECTOR(1 downto 0);
        Y: OUT STD_LOGIC_VECTOR(3 downto 0)
    );
end component;

signal A,B : STD_LOGIC_VECTOR(1 downto 0);
signal Y : STD_LOGIC_VECTOR(3 downto 0);

begin
    UUT : Multiplier_2 PORT MAP (
        A => A,
        B => B,
        Y => Y
    );
    process
    begin
        A<="00";
        B<="00";
        wait for 100ns;
        B<="01";
        wait for 100ns;
        A<="01";
        wait for 100ns;
        B<="11";
        wait for 100ns;
        A<="11";
        wait for 100ns;
        B<="10";
        wait for 100ns;
        A<="10";
        wait;
    end process;
end Behavioral;