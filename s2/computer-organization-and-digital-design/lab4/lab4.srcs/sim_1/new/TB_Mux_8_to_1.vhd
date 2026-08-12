library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity TB_Mux_8_to_1 is
end TB_Mux_8_to_1;

architecture Behavioral of TB_Mux_8_to_1 is
    component Mux_8_to_1
        Port (
            EN : in STD_LOGIC;
            S : in STD_LOGIC_VECTOR (2 downto 0);
            D : in STD_LOGIC_VECTOR (7 downto 0);
            Y : out STD_LOGIC
        );
    end component;

    signal EN : STD_LOGIC := '0';
    signal S : STD_LOGIC_VECTOR (2 downto 0) := (others => '0');
    signal D : STD_LOGIC_VECTOR (7 downto 0) := (others => '0');

    -- Output signal
    signal Y : STD_LOGIC;

begin
    uut: Mux_8_to_1
        Port Map (
            EN => EN,
            S => S,
            D => D,
            Y => Y
        );

    process
    begin
        EN <= '1';

        D <= "10101010";
        S <= "000"; wait for 10 ns;

        S <= "001"; wait for 10 ns;

        S <= "010"; wait for 10 ns;

        S <= "011"; wait for 10 ns;

        S <= "100"; wait for 10 ns;

    end process;
 end Behavioral;