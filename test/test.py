# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge

@cocotb.test()
async def test_dco_out_after_5_cycles(dut):
    """Test case where dco_out should be 1 after 5 clock cycles."""

    # Initialize the inputs
    dut._log.info("Starting test: dco_out should be 1 after 5 clock cycles")
    
    dut.clk.value = 0  # Initialize clk to 0
    dut.rst_n.value = 1  # Assert reset
    dut.ena.value = 1  # Enable DCO
    dut.dco_code.value = 0x01  # Set dco_code to 0x01

    # Set the clock period to 20 ns (50 MHz clock)
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())  # Start the clock

    # Apply reset and then de-assert after 20 ns
    await Timer(20, units="ns")
    dut.rst_n.value = 0  # Release reset after 20 ns

    # Wait for 5 clock cycles
    for _ in range(5):
        await RisingEdge(dut.clk)  # Wait for rising edge of the clock
    
    # Check if dco_out is 1 after 5 clock cycles
    await RisingEdge(dut.clk)  # Wait for the next clock cycle to ensure stability
    assert dut.dco_out.value == 1, f"Expected dco_out to be 1 after 5 clock cycles, but got {dut.dco_out.value}"

    # Log the result
    dut._log.info(f"Test passed: dco_out={dut.dco_out.value} after 5 clock cycles")

