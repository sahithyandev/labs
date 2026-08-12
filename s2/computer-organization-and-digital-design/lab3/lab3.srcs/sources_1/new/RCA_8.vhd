----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 02/28/2025 10:06:33 PM
-- Design Name: 
-- Module Name: RCA_8 - Behavioral
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

entity RCA_8 is
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
end RCA_8;

architecture Behavioral of RCA_8 is
component RCA_4
    port ( A0 : in STD_LOGIC;
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
signal RCA_4_0_C_out : std_logic;

begin
 RCA_4_0: RCA_4 port map (
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
       C_out => RCA_4_0_C_out);

 RCA_4_1: RCA_4 port map (
       A0 => A4,
       A1 => A5,
       A2 => A6,
       A3 => A7,
       B0 => B4,
       B1 => B5,
       B2 => B6,
       B3 => B7,
       C_in => RCA_4_0_C_out,
       S0 => S4,
       S1 => S5,
       S2 => S6,
       S3 => S7,
       C_out => C_out);

end Behavioral;
