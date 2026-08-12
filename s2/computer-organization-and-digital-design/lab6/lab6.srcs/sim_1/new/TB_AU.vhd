library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity TB_AU is
end TB_AU;

architecture Behavioral of TB_AU is
    component AU
        Port (
            A       : in std_logic_vector(3 downto 0);
            RegSel  : in std_logic;
            Clk     : in std_logic;
            S       : out std_logic_vector(3 downto 0);
            Zero    : out std_logic;
            Carry   : out std_logic
        );
    end component;
    
    signal A_tb      : std_logic_vector(3 downto 0) := "0000";
    signal RegSel_tb : std_logic := '0';
    signal Clk_tb    : std_logic := '0';
    signal S_tb      : std_logic_vector(3 downto 0) := "0000";
    signal Zero_tb   : std_logic  := '0';
    signal Carry_tb  : std_logic := '0';
    
    begin
    
    UUT: AU
        port map (
            A       => A_tb,
            RegSel  => RegSel_tb,
            Clk     => Clk_tb,
            S       => S_tb,
            Zero    => Zero_tb,
            Carry   => Carry_tb
        );
    process begin
    Clk_tb <= not Clk_tb;
    wait for 2ns;
    end process;
    
    process
    begin
        -- Test Case 1: Load Register A with 3
        A_tb <= "0011";  -- A = 3
        RegSel_tb <= '0'; -- Select Register A
        wait for 100ns;
        
        -- Test Case 2: Load Register B with 5
        A_tb <= "0101";  -- A = 5
        RegSel_tb <= '1'; -- Select Register B
        wait for 100ns;
        
        -- Test Case 3: Perform Addition (3 + 5)
        wait for 100ns; -- Wait for addition result
        
        -- Test Case 5: Load Register A and B with 0, Expect Zero flag = 1
        A_tb <= "0000";
        RegSel_tb <= '0';
        wait for 100ns;
        A_tb <= "0000";
        RegSel_tb <= '1';
        wait for 100ns;
        
        -- Stop simulation
        wait;
    end process;
    
end Behavioral;
