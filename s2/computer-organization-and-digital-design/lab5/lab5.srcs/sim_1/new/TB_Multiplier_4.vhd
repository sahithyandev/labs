---------------------------------------------------------------------------
-- Engineer: Sahithyan K.
---------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;
-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;
entity TB_Mulitlplier_4 is
-- Port ( );
end TB_Mulitlplier_4;

architecture Behavioral of TB_Mulitlplier_4 is

component Multiplier_4 is
    Port( A: IN STD_LOGIC_VECTOR(3 downto 0);
    B: IN STD_LOGIC_VECTOR(3 downto 0);
    Y: OUT STD_LOGIC_VECTOR(7 downto 0)
    );
end component;

signal A,B : STD_LOGIC_VECTOR(3 downto 0);
signal Y : STD_LOGIC_VECTOR(7 downto 0);

begin
    UUT : Multiplier_4 PORT MAP (
    A => A,
    B => B,
    Y => Y
    );
    process
    begin
        A<="1010";
        B<="1001";
        wait for 100ns;
        A<="0011";
        wait for 100ns;
        B<="0001";
        wait for 100ns;
        A<="0111";
        wait for 100ns;
        B<="0110";
        wait for 100ns;
        A<="0011";
        wait for 100ns;
        A<="1101";
        wait for 100ns;
        B<="1010";
        wait for 100ns;
        A<="1111";
        wait for 100ns;
        B<="1001";
        wait;
    end process;
end Behavioral;