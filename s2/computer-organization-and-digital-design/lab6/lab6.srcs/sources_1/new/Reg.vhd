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

entity Reg is
    Port (
        D  : in std_logic_vector (3 downto 0);
        En : in std_logic;
        Clk : in std_logic;
        Q : out std_logic_vector (3 downto 0));
end Reg;

architecture Behavioral of Reg is

begin
    process (Clk) begin
         if (rising_edge(Clk)) then -- respond when clock rises
             if En = '1' then -- Enable should be set
                Q <= D;
             end if;
         end if;
    end process;

end Behavioral;
