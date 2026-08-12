----------------------------------------------------------------------------------
-- Engineer: Sahithyan K.
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

entity Counter is
    Port (Clk : in std_logic;
          Dir : in std_logic;
          Res: in std_logic;
          Q : out std_logic_vector(2 downto 0));
end Counter;

architecture Behavioral of Counter is
    component SlowClk is
        Port (
            clk_in : in std_logic;
            clk_out : out std_logic);
    end component;
    component D_FF is
        Port(
            D : in std_logic;
            Res : in std_logic;
            Clk: in std_logic;
            Q : out std_logic;
            Qbar : out std_logic);
    end component;
    
    signal D0, D1, D2 : std_logic := '0';
    signal Q0, Q1, Q2 : std_logic := '0';
    signal Q0bar, Q1bar, Q2bar : std_logic := '0';
    signal Slow_Clk_out : std_logic := '0';

begin
     Slow_Clk0 : SlowClk port map (
         Clk_in => Clk,
         Clk_out => Slow_Clk_out);
     
     D_FF0: D_FF port map(
        D => D0,
        Res => Res,
        Clk => Slow_Clk_out,
        Q => Q0,
        Qbar => Q0bar
     );
     D_FF1: D_FF port map(
         D => D1,
         Res => Res,
         Clk => Slow_Clk_out,
         Q => Q1,
         Qbar => Q1bar
      );
      D_FF2: D_FF port map(
          D => D2,
          Res => Res,
          Clk => Slow_Clk_out,
          Q => Q2,
          Qbar => Q2bar
       );
       D0 <= (not(Dir) and not(Q2)) or (Dir and Q1) or (not(Q2) and Q1);
       D1 <= (Dir and Q2) or (Q2 and Q0) or (not(Dir) and Q0);
       D2 <= (Dir and not(Q0)) or (not(Dir) and Q1) or (Q1 and not(Q0));
       
       Q(0) <= Q0;
       Q(1) <= Q1;
       Q(2) <= Q2;


end Behavioral;
