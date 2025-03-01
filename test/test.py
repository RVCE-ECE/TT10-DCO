# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
from cocotb.triggers import Timer
from cocotb.regression import TestFactory

@cocotb.test()
async def test_dco(dut):
    # Start of the test
    dut._log.info("Starting DCO Test")
    
    # Manually set clk to 0 before starting the clock
    dut.clk.value = 0
    dut.rst_n.value = 0  # Assert reset
    dut.ena.value = 1    # Enable the DCO
    
    # Set initial values for inputs
    dut.ui_in.value = 0x00
    dut.uio_in.value = 0x00
    
    # Wait for a couple of clock cycles to simulate reset
    await Timer(20, units="ns")
    
    # Set the clock period to 20 ns (50 MHz)
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())  # Start the clock
    
    # De-assert reset after 20 ns (simulate reset completion)
    dut.rst_n.value = 1
    await Timer(10, units="ns")  # Wait for a short time
    
    # Testing different dco_code values and checking uo_out
    test_values = [
        (0x01, 0x00),  # Test dco_code = 0x01, expect uo_out to be 0x00
        (0x02, 0x00),  # Test dco_code = 0x02, expect uo_out to be 0x00
        (0x04, 0x00),  # Test dco_code = 0x04, expect uo_out to be 0x00
        (0x08, 0x00),  # Test dco_code = 0x08, expect uo_out to be 0x00
        (0x10, 0x00),  # Test dco_code = 0x10, expect uo_out to be 0x00
        (0x20, 0x00),  # Test dco_code = 0x20, expect uo_out to be 0x00
        (0x40, 0x00),  # Test dco_code = 0x40, expect uo_out to be 0x00
        (0x80, 0x00),  # Test dco_code = 0x80, expect uo_out to be 0x00
    ]
    
    # Run through each test case and assert the expected value of uo_out
    for dco_code, expected_uo_out in test_values:
        dut.ui_in.value = dco_code
        await Timer(40, units="ns")  # Wait for a couple of clock cycles
        assert dut.uo_out.value == expected_uo_out, f"Failed for dco_code={hex(dco_code)}. Expected uo_out={hex(expected_uo_out)} but got {hex(dut.uo_out.value)}"
    
    # Additional random tests (if needed)
    for _ in range(5):
        random_dco_code = random.randint(0, 255)  # Generate a random 8-bit DCO code
        dut.ui_in.value = random_dco_code
        await Timer(40, units="ns")  # Wait for a couple of clock cycles
        
        # Check the output and validate the expected output (adjust as needed)
        expected_uo_out = (random_dco_code % 2)  # Just an example, modify as per your design expectations
        assert dut.uo_out.value == expected_uo_out, f"Failed for random dco_code={hex(random_dco_code)}. Expected uo_out={hex(expected_uo_out)} but got {hex(dut.uo_out.value)}"
    
    # End of the test
    dut._log.info("DCO Test completed successfully")

# Create a test factory to run the test
test_factory = TestFactory(test_dco)

# Add simulation options (if necessary)
test_factory.add_option("-sv")  # For SystemVerilog support

# Run the test
test_factory.generate_tests()
