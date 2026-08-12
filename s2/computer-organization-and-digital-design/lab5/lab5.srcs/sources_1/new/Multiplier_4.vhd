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

entity Multiplier_4 is
    Port (
        A : in STD_LOGIC_VECTOR (3 downto 0);
        B : in STD_LOGIC_VECTOR (3 downto 0);
        Y : out STD_LOGIC_VECTOR (7 downto 0));
end Multiplier_4;

architecture Behavioral of Multiplier_4 is

component FA
    Port ( A : in STD_LOGIC;
           B : in STD_LOGIC;
           C_in : in STD_LOGIC;
           S : out STD_LOGIC;
           C_out : out STD_LOGIC);
end component;

signal b0a0, b0a1, b0a2, b0a3 : std_logic;
signal b1a0, b1a1, b1a2, b1a3 : std_logic;
signal b2a0, b2a1, b2a2, b2a3 : std_logic;
signal b3a0, b3a1, b3a2, b3a3 : std_logic;

signal s_0_0, c_0_0 : std_logic;
signal s_0_1, c_0_1 : std_logic;
signal s_0_2, c_0_2 : std_logic;
signal s_1_0, c_1_0 : std_logic;
signal s_1_1, c_1_1 : std_logic;
signal s_1_2, c_1_2 : std_logic;
signal s_2_0, c_2_0 : std_logic;
signal s_2_1, c_2_1 : std_logic;
signal s_2_2, c_2_2 : std_logic;
signal s_3_0, c_3_0 : std_logic;
signal s_3_1, c_3_1 : std_logic;
signal s_3_2, c_3_2 : std_logic;


begin
    FA_0_0: FA port map(
        A => b1a0,
        B => b0a1,
        C_in => '0',
        S => s_0_0,
        C_out => c_0_0
    );
    FA_0_1: FA port map(
        A => b2a0,
        B => b1a1,
        C_in => c_0_0,
        S => s_0_1,
        C_out => c_0_1
    );
    FA_0_2: FA port map(
        A => b3a0,
        B => b2a1,
        C_in => c_0_1,
        S => s_0_2,
        C_out => c_0_2
    );

    FA_1_0: FA port map(
        A => s_0_1,
        B => b0a2,
        C_in => c_0_0,
        S => s_1_0,
        C_out => c_1_0
    );
    FA_1_1: FA port map(
        A => s_0_2,
        B => b1a2,
        C_in => c_0_1,
        S => s_1_1,
        C_out => c_1_1
    );
    FA_1_2: FA port map(
        A => b3a1,
        B => b2a2,
        C_in => c_0_2,
        S => s_1_2,
        C_out => c_1_2
    );
    
    FA_2_0: FA port map(
        A => s_1_1,
        B => b0a3,
        C_in => c_1_0,
        S => s_2_0,
        C_out => c_2_0
    );
    FA_2_1: FA port map(
        A => s_1_2,
        B => b1a3,
        C_in => c_1_1,
        S => s_2_1,
        C_out => c_2_1
    );
    FA_2_2: FA port map(
        A => b3a2,
        B => b2a3,
        C_in => c_1_2,
        S => s_2_2,
        C_out => c_2_2
    );
    
    FA_3_0: FA port map(
        A => c_2_0,
        B => s_2_1,
        C_in => '0',
        S => s_3_0,
        C_out => c_3_0
    );
    FA_3_1: FA port map(
        A => c_2_1,
        B => s_2_2,
        C_in => c_3_0,
        S => s_3_1,
        C_out => c_3_1
    );
    FA_3_2: FA port map(
        A => b3a3,
        B => c_2_2,
        C_in => c_3_1,
        S => s_3_2,
        C_out => c_3_2
    );
    
    b0a0 <= B(0) and A(0);
    b0a1 <= B(0) and A(1);
    b0a2 <= B(0) and A(2);
    b0a3 <= B(0) and A(3);
    
    b1a0 <= B(1) and A(0);
    b1a1 <= B(1) and A(1);
    b1a2 <= B(1) and A(2);
    b1a3 <= B(1) and A(3);
    
    b2a0 <= B(2) and A(0);
    b2a1 <= B(2) and A(1);
    b2a2 <= B(2) and A(2);
    b2a3 <= B(2) and A(3);
    
    b3a0 <= B(3) and A(0);
    b3a1 <= B(3) and A(1);
    b3a2 <= B(3) and A(2);
    b3a3 <= B(3) and A(3);
    
    Y(0) <= b0a0;
    Y(1) <= s_0_0;
    Y(2) <= s_1_0;
    Y(3) <= s_2_0;
    Y(4) <= s_3_0;
    Y(5) <= s_3_1;
    Y(6) <= s_3_2;
    Y(7) <= c_3_2;

end Behavioral;
