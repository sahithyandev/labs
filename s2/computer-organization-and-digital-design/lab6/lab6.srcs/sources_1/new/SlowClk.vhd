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

entity SlowClk is
    Port (
        clk_in : in std_logic;
        clk_out : out std_logic);
end SlowClk;

architecture Behavioral of SlowClk is

signal clk_count : integer := 1;
signal clk_status : std_logic := '0';

begin
    process (clk_in) begin
        if (rising_edge(clk_in)) then
            clk_count <= clk_count + 1;
            if (clk_count = 10) then
                clk_status <= not(clk_status);
                clk_out <= clk_status;
                clk_count <= 1;
            end if;
        end if;
    end process;
    
end Behavioral;
