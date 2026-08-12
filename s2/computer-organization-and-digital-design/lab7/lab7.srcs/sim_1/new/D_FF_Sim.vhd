----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 04/01/2025 01:42:35 PM
-- Design Name: 
-- Module Name: D_FF_Sim - Behavioral
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

entity D_FF_Sim is
--  Port ( );
end D_FF_Sim;

architecture Behavioral of D_FF_Sim is
    
    component D_FF is
        Port(
        D : in std_logic;
        Res : in std_logic;
        Clk: in std_logic;
        Q : out std_logic;
        Qbar : out std_logic);
    end component;

    signal D, Res, Clk, Q, Qbar : std_logic;
    constant clk_period : time := 30 ns;
begin

    UUT: D_FF port map(
        D => D,
        Res => Res,
        Clk => Clk,
        Q => Q,
        Qbar => Qbar
    );
    
    clk_process : process
    begin
        while true loop
            Clk <= '0';
            wait for clk_period/2;
            Clk <= '1';
            wait for clk_period/2;
        end loop;
        wait;
    end process;
    
    process begin
        Res <= '0';
        D <= '1';
        wait for 150ns;
        
        D <= '0';
        wait for 100ns;        
        
        wait;
    
    end process;


end Behavioral;
