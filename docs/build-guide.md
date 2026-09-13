# Planned build and test guide

These steps describe future work. The prototype has not been built. Finish the detailed design and resolve the budget before ordering.

## 1. Finish the design

1. Confirm Pi 5 **4 GB**, **64 GB** card, and the exact keyboard variant. Resolve conflicting keyboard heights with the supplier and record its cable exit and outer edge dimensions.
2. Use the designed v0.2 printed hinges and M4 axes described in [the enclosure assembly guide](../CAD/v0.2/ASSEMBLY.md). Test the small hinge coupons before the full print; holding friction and strength remain unmeasured.
3. Complete mounts from manufacturer drawings, port openings, ventilation, and cable routing. Use cardboard envelopes when real parts are unavailable.
4. Check the v0.2 underside rails, pads, tightening stops and 2 mm retaining lip against the exact keyboard housing. Adjust support height if the physical rim differs from the assumed envelope.
5. Follow the exact screw list and nominal engagement calculations in the enclosure assembly guide. Verify printed clearances and actual hardware before tightening. Keep metal clear of electronics.
6. Confirm delivered prices and obtain funding review before purchasing on the assumption of reimbursement.

## 2. Prepare after parts arrive

1. Work on a clear table, with the power supply unplugged. Gather the parts, small screwdriver, ruler/calipers, and a computer with a microSD reader. Borrow tools if possible; only the printer is confirmed owned.
2. Photograph and measure each part. Compare it with the CAD and revise any differences before printing.
3. Follow the [official Touch Display 2 instructions](https://www.raspberrypi.com/documentation/accessories/touch-display-2.html) for pin identification and ribbon orientation. Ask an adult to check the first power-lead connection with you.

## 3. Bench test

1. Get Raspberry Pi Imager from the [official software page](https://www.raspberrypi.com/software/). Select Pi 5, the current Raspberry Pi OS desktop image, and the 64 GB microSD. Writing erases the selected card; check the destination carefully. Keep passwords out of recordings.
2. Let writing and verification finish. Eject the card and insert it into the Pi.
3. Install the Active Cooler with its supplied pads and fasteners. Connect it to the Pi's dedicated fan socket.
4. With power disconnected, fit the supplied Pi 5 compatible display cable exactly as the manufacturer shows. Open and close the latches gently; never force a ribbon.
5. Attach the display power lead to the documented 5 V/GND pins. Verify polarity before powering anything.
6. Plug the intact keyboard into USB-A. Support the board and display on stable nonconductive surfaces.
7. Connect the official USB-C supply last. Complete first boot and OS setup.
8. Use the desktop display settings to select landscape orientation and check that touch coordinates match. Labels depend on the OS version.
9. Type a sentence; test every key, pointer movement, left/right click, and scrolling. Optional gestures require real Linux testing.
10. Shut down through the desktop and wait for completion before unplugging or changing wiring.

## 4. Print and assemble

1. Print small test pieces for keyboard retention, nut capture, hinges, and fit clearances. Adjust the design from measured results.
2. Start with the filament manufacturer's PETG settings and the QIDI material profile. Slice each revised shell individually; check supports, brim, print volume, and material use.
3. Remove sharp edges and debris. Test fasteners in empty printed parts before installing electronics.
4. Mount the Pi on insulating supports using suitable M2.5 hardware. No screw or case surface may contact underside electronics.
5. Seat the intact keyboard against the upper retaining lip. Install padded internal supports and tighten the underside-accessed screws evenly to their designed stops. Do not drill or screw into the keyboard.
6. Route the full keyboard cable in loose loops, away from the fan and hinge. Do not cut or sharply fold it.
7. Mount the display using its intended fixing points; do not clamp the active glass. Check allowed screw engagement before tightening.
8. Install the final hinges, stops, and strain relief. Leave an adequate service loop for the display ribbon and power lead. Ordinary FFC is not automatically suitable for repeated hinge movement.
9. With power off, move the lid slowly through its range. Resolve pinches and contact before continuing.
10. Close the base from below. Keep feet and fasteners clear of vents and verify access to power and external ports.
11. Repeat the bench tests in the enclosure. Record results below.

## 5. Test record

Project targets below are not manufacturer guarantees. Add date, setup, evidence, and actual results after each test.

| Check | Planned pass condition | Result |
|---|---|---|
| Startup | Five consecutive boots to desktop without storage errors | Not tested |
| Keyboard | Keys and modifiers work; NumLock behavior documented | Not tested |
| Touchpad | Pointer, clicks, and supported scrolling work | Not tested |
| Display | Readable landscape picture and matching touch coordinates | Not tested |
| Power | No undervoltage warning under normal use and sustained load | Not tested |
| Cooling | Log ambient/CPU temperatures over 30 minutes of load; target CPU below 80°C and no throttling | Not tested |
| Retention | No keyboard rocking or lift while typing normally | Not tested |
| Lid | 50 slow cycles without pinching, dropout, or loosening; initial check only, not a lifetime rating | Not tested |
| Closed fit | Keys and display do not touch; lid rests on stops | Not tested |
| Service | Components accessible without destructive disassembly | Not tested |

## 6. Record the finished build

1. Update the BOM with actual quantities and paid prices.
2. Export final editable CAD, STEP, and tested printable STL files.
3. Add real inside/outside photos and a demo showing boot, typing, touchpad use, and enclosure details.
4. Record failures and fixes, not just successes. Keep real photos separate from the AI concept.
5. Follow the current Stardance submission prompts. S tier remains a reviewer decision.
