----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 03/25/2025 03:13:45 PM
-- Design Name: 
-- Module Name: TB_Decoder_1_to_2 - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
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

entity TB_Decoder_1_to_2 is
--  Port ( );
end TB_Decoder_1_to_2;

architecture Behavioral of TB_Decoder_1_to_2 is

component Decoder_1_to_2
    Port( A : in std_logic;
          B : out std_logic_vector(1 downto 0)
    );
end component;

signal A :std_logic;
signal B : std_logic_vector(1 downto 0);

begin

    uut: Decoder_1_to_2 port map(
            A => A,
            B => B
        );
    process begin
        A <= '0';
        wait for 100ns;
        
        A <= '1';
        wait for 100ns;
    end process;

end Behavioral;
