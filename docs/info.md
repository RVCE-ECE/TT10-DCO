> ## 📌 Credits  
>  
> We sincerely acknowledge the **Center of Excellence in Integrated Circuits and Systems (CoE-ICAS)** and the **Department of Electronics and Communication Engineering, RV College of Engineering, Bengaluru**, for their invaluable support in providing us with the necessary knowledge and training.  
> 
> We extend our special gratitude to **Dr. H V Ravish Aradhya (HoD, ECE)**, **Dr. K S Geetha (Vice Principal)** and **Dr. K N Subramanya (Principal)** for their continuous encouragement and support, enabling us to achieve **TAPEOUT** in **Tiny Tapeout 10**.  
>  
> We are also deeply grateful to **Mahaa Santeep G (RVCE Alumni)** for his mentorship and invaluable guidance throughout the completion of this project.  
  
## How it works

The tt_um_dco module is a digitally controlled oscillator (DCO) that generates a frequency-adjustable clock signal based on an 8-bit control input (ui_in). The control input determines the oscillation period using a priority-based selection, where the highest active bit sets the period between 3 and 50 clock cycles. A fast clock is derived from the main clock (clk) using a 4-bit divider, toggling every four cycles. A counter increments on each clock edge, and when it reaches the selected period, dco_out toggles, generating the output waveform. The reset (rst_n) initializes the oscillator, and unused outputs are assigned zero to prevent warnings.

## How to test

To verify the functionality of the tt_um_dco module, a testbench (tb) has been provided. The testbench simulates different input scenarios and observes the output behavior of the tt_um_dco module to ensure that it works correctly.

The testbench will output the results of the simulation, including the values of the inputs and the resulting output for each test case. Monitor the output in the console or waveform viewer to ensure the tt_um_mac module behaves as expected.

## External hardware

During the simulation, you can monitor the console or waveform outputs for detailed step-by-step results. The testbench uses $monitor to display real-time updates of the inputs and the resulting output.
