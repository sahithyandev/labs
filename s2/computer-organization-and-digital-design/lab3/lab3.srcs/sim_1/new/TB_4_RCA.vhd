----------------------------------------------------------------------------------
-- Company:
-- Engineer:
--
-- Create Date: 02/24/2025 05:11:01 PM
-- Design Name:
-- Module Name: TB_HA - Behavioral
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

entity TB_4_RCA is
--  Port ( );
end TB_4_RCA;

architecture Behavioral of TB_4_RCA  is
        component RCA_4
    Port ( A0 : in STD_LOGIC;
               A1 : in STD_LOGIC;
               A2 : in STD_LOGIC;
               A3 : in STD_LOGIC;
               B0 : in STD_LOGIC;
               B1 : in STD_LOGIC;
               B2 : in STD_LOGIC;
               B3 : in STD_LOGIC;
               C_in : in STD_LOGIC;
               S0 : out STD_LOGIC;
               S1 : out STD_LOGIC;
               S2 : out STD_LOGIC;
               S3 : out STD_LOGIC;
               C_out : out STD_LOGIC);
        end component;

signal  A0, A1, A2, A3,
        B0, B1, B2, B3,
        C_in,
        S0, S1, S2, S3,
        C_out: std_logic;

begin
        UUT: RCA_4 port map(
               A0 => A0,
               A1 => A1,
               A2 => A2,
               A3 => A3,
               B0 => B0,
               B1 => B1,
               B2 => B2,
               B3 => B3,
               C_in => C_in,
               S0 => S0,
               S1 => S1,
               S2 => S2,
               S3 => S3,
               C_out => C_out);
        process
        begin
                
                A0 <= '1';
                A1 <= '0';
                A2 <= '0';
                A3 <= '1';
                
                B0 <= '1';
                B1 <= '0';
                B2 <= '1';
                B3 <= '1';
                C_in <= '0';
                wait for 10ns;
        wait;
        end process;

end Behavioral;