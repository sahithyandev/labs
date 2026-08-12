----------------------------------------------------------------------------------
-- Engineer: Sahithyan K.
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity Multiplier_2 is
    port (
        A : in STD_LOGIC_VECTOR (1 downto 0);
        B : in STD_LOGIC_VECTOR (1 downto 0);
        Y : out STD_LOGIC_VECTOR (3 downto 0));
end Multiplier_2;

architecture Behavioral of Multiplier_2 is
component FA
    Port ( A : in STD_LOGIC;
           B : in STD_LOGIC;
           C_in : in STD_LOGIC;
           S : out STD_LOGIC;
           C_out : out STD_LOGIC);
end component;

signal b0a0, b0a1, b1a0, b1a1 : std_logic;
signal c_0_0, s_0_0, c_0_1, s_0_1 : std_logic;

begin
    b0a0 <= B(0) and A(0);
    Y(0) <= b0a0;
    
    b1a0 <= B(1) and A(0);
    b0a1 <= B(0) and A(1);
    FA_0_0: FA port map(
        A => b1a0,
        B => b0a1,
        C_in => '0',
        S => s_0_0,
        C_out => c_0_0
    );
    Y(1) <= s_0_0;
    
    b1a1 <= B(1) and A(1);
    FA_0_1: FA port map(
        A => c_0_0,
        B => b1a1,
        C_in => '0',
        S => s_0_1,
        C_out => c_0_1
    );
    Y(2) <= s_0_1;
    Y(3) <= c_0_1;

end Behavioral;
