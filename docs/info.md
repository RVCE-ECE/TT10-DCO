Credits : We gratefully acknowledge the COE in Integrated Circuits and Systems (ICAS) and Department of ECE. Our special thanks to Dr K S Geetha (Vice Principal) and, Dr. K N Subramanya (principal) for their constant support and encouragement to do TAPEOUT in Tiny Tapeout 10 .

## How it works

The tt_um_mac module is a Multiply-Accumulate (MAC) unit designed for high-performance digital signal processing and embedded system applications. This module integrates a Dadda multiplier and a Kogge-Stone adder to achieve efficient and fast computations. The MAC unit performs a sequence of multiplication and accumulation operations, which are essential in various digital signal processing tasks, such as filtering and convolution. Functional Description Input and Output Ports • Inputs: o ui_in (8-bit): Dedicated input for the first operand. o uio_in (8-bit): Input/Output interface for the second operand. o clk (1-bit): Clock signal to synchronize all operations. o rst_n (1-bit): Active-low reset signal to initialize the internal state of the MAC unit. • Outputs: o uo_out (8-bit): Output that holds the final accumulated result. o uio_oe (8-bit): Output enable signal, set to 0 indicating the uio is used as input. o uio_out (8-bit): Unused output path in the current context. Internal Architecturee

## How it works

he tt_um_mac module is a Multiply-Accumulate (MAC) unit designed for high-performance digital signal processing and embedded system applications. This module integrates a Dadda multiplier and a Kogge-Stone adder to achieve efficient and fast computations. The MAC unit performs a sequ

## How to test

Explain how to use your project wwwd

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
