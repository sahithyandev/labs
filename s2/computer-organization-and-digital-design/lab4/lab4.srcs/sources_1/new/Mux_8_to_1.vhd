----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 03/04/2025 02:11:40 PM
-- Design Name: 
-- Module Name: Mux_8_to_1 - Behavioral
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

entity Mux_8_to_1 is
    Port ( EN : in STD_LOGIC;
           S : in STD_LOGIC_VECTOR (2 downto 0);
           D : in STD_LOGIC_VECTOR (7 downto 0);
           Y : out STD_LOGIC);
end Mux_8_to_1;

architecture Behavioral of Mux_8_to_1 is

    component Decoder_3_to_8
        Port ( EN : in STD_LOGIC;
       I : in STD_LOGIC_VECTOR (2 downto 0);
       Y : out STD_LOGIC_VECTOR (7 downto 0));
    end component;
    
    signal decoder_out : std_logic_vector (7 downto 0);
    
    begin
        decoder: Decoder_3_to_8 port map
            (
                EN => EN,
                I => S,
                Y => decoder_out
            );
        Y <= (D(0) and decoder_out(0)) or
             (D(1) and decoder_out(1)) or
             (D(2) and decoder_out(2)) or
             (D(3) and decoder_out(3)) or
             (D(4) and decoder_out(4)) or
             (D(5) and decoder_out(5)) or
             (D(6) and decoder_out(6)) or
             (D(7) and decoder_out(7));
end Behavioral;
