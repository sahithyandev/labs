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

entity TB_FA is
--  Port ( );
end TB_FA;

architecture Behavioral of TB_FA is
	component FA
	port (	A, B, C_in: in std_logic;
		S, C_out: out std_logic);
	end component;

signal A, B, C_in, C_out, S: std_logic;

begin
	UUT: FA port map(
		A => A,
		B => B,
		C_in => C_in,
		C_out => C_out,
		S => S);
	process
	begin
		A <= '0';
		B <= '0';
		C_in <= '0';
		wait for 100ns;

		C_in <= '1';
		wait for 100ns;

		B <= '1';
		wait for 100ns;

		C_in <= '0';
		wait for 100ns;
		A <= '1';
        wait for 100ns;
        C_in <= '1';
        wait for 100ns;
        
	wait;
	end process;

end Behavioral;
