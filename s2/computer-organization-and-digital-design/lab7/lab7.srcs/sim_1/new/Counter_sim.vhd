----------------------------------------------------------------------------------
-- Engineer: Sahithyan K.
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Counter_sim is
end Counter_sim;

architecture Behavioral of Counter_sim is

    -- Component Declaration for the Unit Under Test (UUT)
    component Counter
        Port (
            Clk : in std_logic;
            Dir : in std_logic;
            Res: in std_logic;
            Q : out std_logic_vector(2 downto 0)
        );
    end component;

    -- Signal declarations
    signal Clk : std_logic := '0';
    signal Dir : std_logic := '0';
    signal Res : std_logic := '0';
    signal Q : std_logic_vector(2 downto 0) := "000";

    constant clk_period : time := 5 ns;

begin
    -- Instantiate the Unit Under Test (UUT)
    UUT: Counter port map (
        Clk => Clk,
        Dir => Dir,
        Res => Res,
        Q => Q
    );

    -- Clock process definition
    process
    begin
        while true loop
            Clk <= '0';
            wait for clk_period/2;
            Clk <= '1';
            wait for clk_period/2;
        end loop;
        wait;
    end process;

    -- Stimulus process
    process
    begin    
        -- Reset the counter
        wait for 50ns;
        Res <= '1';
        
        -- Test Counting Up
        Dir <= '1';
        wait for 200 ns;

        -- Test Counting Down
        Dir <= '0';
        wait for 200 ns;

        -- Test Reset again
        Res <= '1';
        wait for 20 ns;
        Res <= '0';
        
        wait;
    end process;

end Behavioral;
