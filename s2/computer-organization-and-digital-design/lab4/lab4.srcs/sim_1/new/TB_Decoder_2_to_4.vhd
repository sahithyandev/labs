----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 03/04/2025 01:25:57 PM
-- Design Name: 
-- Module Name: TB_Decoder_2_to_4 - Behavioral
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

entity TB_Decoder_2_to_4 is
--  Port ( );
end TB_Decoder_2_to_4;

architecture Behavioral of TB_Decoder_2_to_4 is

component Decoder_2_to_4
    Port (
        EN : in std_logic;
        I : in  STD_LOGIC_VECTOR (1 downto 0);
        Y : out STD_LOGIC_VECTOR (3 downto 0)
    );
end component;

    signal EN: std_logic := '0';
    signal I : STD_LOGIC_VECTOR (1 downto 0) := (others => '0');
    signal Y : STD_LOGIC_VECTOR (3 downto 0);

begin
    uut: Decoder_2_to_4
        port map(
            EN => EN,
            I => I,
            Y => Y
        );
     process begin
     
        I <= "00"; wait for 100ns;
        I <= "01"; wait for 100ns;
        I <= "10"; wait for 100ns;
        I <= "11"; wait for 100ns;
        
        EN <= '1';
        I <= "00"; wait for 100ns;
        I <= "01"; wait for 100ns;
        I <= "10"; wait for 100ns;
        I <= "11"; wait for 100ns;
     end process;


end Behavioral;
