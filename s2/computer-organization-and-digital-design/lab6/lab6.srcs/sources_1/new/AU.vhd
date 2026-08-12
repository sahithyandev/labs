----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 03/25/2025 01:45:25 PM
-- Design Name: 
-- Module Name: AU - Behavioral
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

entity AU is
    Port (
        A : in std_logic_vector(3 downto 0);
        RegSel : in std_logic;
        Clk : in std_logic;
        S : out std_logic_vector(3 downto 0);
        Zero : out std_logic;
        Carry : out std_logic);
end AU;

architecture Behavioral of AU is

component Decoder_1_to_2
    port (A : in std_logic;
          B : out std_logic_vector(1 downto 0));
end component;

component SlowClk
    Port (
    clk_in : in std_logic;
    clk_out : out std_logic);
end component;
          
component Reg
    port (
          D  : in std_logic_vector (3 downto 0);
          En : in std_logic;
          Clk : in std_logic;
          Q : out std_logic_vector (3 downto 0)
    );
end component;

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

signal RCA_S, RegAOutput, RegBOutput : std_logic_vector(3 downto 0) := "0000";
signal RegSelDecoderOutput : std_logic_vector(1 downto 0) := "00";
signal SlowClkSignal : std_logic := '0';

begin
    RegSelDecoder : Decoder_1_to_2 port map(
                        A => RegSel,
                        B => RegSelDecoderOutput
                    );
    InternalClock : SlowClk port map(
                        clk_in => Clk,
                        clk_out => SlowClkSignal
                    );
    RegA : Reg port map(
                D => A,
                En => RegSelDecoderOutput(0),
                Clk => SlowClkSignal,
                Q => RegAOutput
           );
    RegB : Reg port map(
                   D => A,
                   En => RegSelDecoderOutput(1),
                   Clk => SlowClkSignal,
                   Q => RegBOutput
              );
    RCA_4_0: RCA_4 port map (
            A0 => RegAOutput(0),
            A1 => RegAOutput(1),
            A2 => RegAOutput(2),
            A3 => RegAOutput(3),
            B0 => RegBOutput(0),
            B1 => RegBOutput(1),
            B2 => RegBOutput(2),
            B3 => RegBOutput(3),
            C_in => '0',
            S0 => RCA_S(0),
            S1 => RCA_S(1),
            S2 => RCA_S(2),
            S3 => RCA_S(3),
            C_out => Carry);
    S <= RCA_S;
    Zero <= not (RCA_S(0) OR RCA_S(1) OR RCA_S(2) OR RCA_S(3));
end Behavioral;
