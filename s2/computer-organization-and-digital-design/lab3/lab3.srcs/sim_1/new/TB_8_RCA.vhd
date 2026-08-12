----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 02/28/2025 10:14:46 PM
-- Design Name: 
-- Module Name: TB_8_RCA - Behavioral
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

entity TB_8_RCA is
--  Port ( );
end TB_8_RCA;

architecture Behavioral of TB_8_RCA is
component RCA_8 
    Port ( A0 : in STD_LOGIC;
           A1 : in STD_LOGIC;
           A2 : in STD_LOGIC;
           A3 : in STD_LOGIC;
           A4 : in STD_LOGIC;
           A5 : in STD_LOGIC;
           A6 : in STD_LOGIC;
           A7 : in STD_LOGIC;
           B0 : in STD_LOGIC;
           B1 : in STD_LOGIC;
           B2 : in STD_LOGIC;
           B3 : in STD_LOGIC;
           B4 : in STD_LOGIC;
           B5 : in STD_LOGIC;
           B6 : in STD_LOGIC;
           B7 : in STD_LOGIC;
           C_in : in STD_LOGIC;
           S0 : out STD_LOGIC;
           S1 : out STD_LOGIC;
           S2 : out STD_LOGIC;
           S3 : out STD_LOGIC;
           S4 : out STD_LOGIC;
           S5 : out STD_LOGIC;
           S6 : out STD_LOGIC;
           S7 : out STD_LOGIC;
           C_out : out STD_LOGIC);
end component;

signal  A0, A1, A2, A3, A4, A5, A6, A7,
        B0, B1, B2, B3, B4, B5, B6, B7,
        C_in,
        S0, S1, S2, S3, S4, S5, S6, S7,
        C_out: std_logic;

begin

UUT: RCA_8 port map(
    A0 => A0,
    A1 => A1,
    A2 => A2,
    A3 => A3,
    A4 => A4,
    A5 => A5,
    A6 => A6,
    A7 => A7,
    B0 => B0,
    B1 => B1,
    B2 => B2,
    B3 => B3,
    B4 => B4,
    B5 => B5,
    B6 => B6,
    B7 => B7,
   C_in => C_in,
    S0 => S0,
    S1 => S1,
    S2 => S2,
    S3 => S3,
    S4 => S4,
    S5 => S5,
    S6 => S6,
    S7 => S7,
   C_out => C_out);

process
begin

    A0 <= '1';
    A1 <= '0';
    A2 <= '0';
    A3 <= '1';
    A4 <= '1';
    A5 <= '1';
    A6 <= '1';
    A7 <= '1';
    
    
    B0 <= '1';
    B1 <= '0';
    B2 <= '1';
    B3 <= '1';
    B4 <= '0';
    B5 <= '0';
    B6 <= '0';
    B7 <= '0';
    
    C_in <= '0';
    
    wait for 10ns;

end process;


end Behavioral;
