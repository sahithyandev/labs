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

entity TB_SlowClk is
--  Port ( );
end TB_SlowClk;

architecture Behavioral of TB_SlowClk is

    component SlowClk is
        Port (
        clk_in : in std_logic;
        clk_out : out std_logic);
    end component;
    
    signal clk_base : std_logic := '0';
    signal clk_slow : std_logic;

begin
    uut: SlowClk port map(
        clk_in => clk_base,
        clk_out => clk_slow
    );

    process
    begin
        while now < 1 ms loop  -- Run for 1 ms simulation time
            clk_base <= not clk_base;
            wait for 5 ns;  -- 10 ns period (100 MHz)
        end loop;
        wait;
    end process;
end Behavioral;
