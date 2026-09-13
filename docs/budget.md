# Budget review — 13 September 2026

**Result: the selected new-parts build does not fit the S-tier allowance. This is a transparent planning estimate, not a funding-ready shopping cart.** No order has been placed. The personal contribution is capped at EUR 50; the procurement target is EUR 222 including delivery and fees. The current selection does not meet that target.

## New funding constraint

Target: S tier, request at most USD 200, subject to approval. Total delivered cost ceiling: EUR 222. Personal contribution ceiling: EUR 50. These are limits, not verified prices. The actual grant conversion and fees determine whether the full EUR 222 can be afforded. A cheaper compatible BOM and revised CAD remain necessary; the existing BOM is retained as the v0.2 cost evidence, not relabelled with invented prices.

## Cost summary

| Group | EUR |
|---|---:|
| Raspberry Pi 5, 4 GB | 129.90 |
| Official 7-inch Touch Display 2 | 64.50 |
| Perixx keyboard with touchpad, reference variant | 39.99 |
| SanDisk Ultra 64 GB | 19.90 |
| Official 27 W supply, cable included | 12.40 |
| Official Active Cooler | 5.90 |
| **Electronics subtotal** | **272.59** |
| PETG, full 1 kg spool allowance | 25.00 |
| v0.2 fasteners, hinge axes, washers and standoffs allowance | 20.00 |
| Integral printed hinges | 0.00 extra; included in filament |
| Additional display cable/power lead allowance | 10.00 |
| Pads, feet, and strain relief allowance | 4.00 |
| USB microSD reader allowance | 5.00 |
| Shipping and destination-tax adjustment allowance | 20.00 |
| Contingency | 15.00 |
| **Planning total** | **371.59** |

The [ECB reference rate for 11 September 2026](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) was **1 EUR = 1.1592 USD**. On that reference basis:

- EUR 371.59 × 1.1592 = **USD 430.75**.
- The [S-tier cap of USD 200](https://stardance.hackclub.com/resources/tiers) corresponds to approximately **EUR 172.53**.
- Estimated gap: **USD 230.75**, or about **EUR 199.06**. Actual payment conversion and fees may differ.

Even the Pi and selected display alone total **EUR 194.40**, approximately **USD 225.35**, before storage, input, power, printing, or delivery. This rules out funding this exact all-new selection solely with USD 200 at these quotes. It does not prove that no cheaper used-parts design could exist.

## Price evidence and limitations

| Item | Evidence | Qualification |
|---|---|---|
| Pi 5 / 4 GB | [Elecom](https://www.elecom.sk/raspberry-pi-5-4-gb-2/): EUR 129.90 | Retail reference, not a locked delivered quote |
| Cheaper Pi listing checked | [BerryBase](https://www.berrybase.de/raspberry-pi-5-4gb-ram): EUR 118.50 | Unavailable when checked; excluded from purchase estimate |
| Display | [BerryBase](https://www.berrybase.de/raspberry-pi-touch-display-2?c=320): EUR 64.50 | 7-inch model, stock shown when checked |
| Keyboard | [Perixx](https://eu.perixx.com/products/periboard-510h): EUR 39.99 | Page selected Spanish; English US is the desired variant, with its price/stock still to confirm |
| Card | [BerryBase microSD listing](https://www.berrybase.de/multimedia-office/speicherkarten-usb-sticks/microsd-karten): EUR 19.90 | SanDisk Ultra 64 GB, EAN 619659200541 |
| Supply | [BerryBase](https://www.berrybase.de/detail/019234a5bfb57193899acec14a1eebd6): EUR 12.40 | Official 27 W EU model; cable included |
| Cooler | [BerryBase](https://www.berrybase.de/raspberry-pi-active-cooler-luefter-fuer-raspberry-pi-5): EUR 5.90 | Official Pi 5 Active Cooler |

Displayed prices include the seller's stated VAT. Delivery to Slovakia, destination VAT, availability, keyboard variants, and payment fees must be rechecked at checkout. The estimate is not a claim to be the cheapest possible selection. Small hardware and material amounts are explicitly **allowances**, not sourced offers.

The additional ribbon allowance is separate from the display's included bench cable. There is no separate HDMI cable, USB-C cable, battery, mouse, or paid operating system in this budget. Only the printer is confirmed owned. A computer for card writing and basic tools must be available or borrowed; purchasing tools is not covered by this estimate.

Enclosure revision v0.2 replaces bought hinges with integral printed hinges and two M4 axes. The former EUR 8 fastener and EUR 12 hinge allowances are combined into a EUR 20 hardware allowance; the total estimate is unchanged. Exact installed fasteners are listed in README and CAD/v0.2/ASSEMBLY.md. This is not a verified hardware-kit price, and optional spares are not included. Recheck filament usage after slicing the larger enclosure.

## What would make USD 200 feasible?

This remains an unresolved procurement/design task. It requires confirmed lower delivered prices or supplied components, and probably a cheaper display and input arrangement. Used or donated parts must be genuinely available and acceptable under the funding rules; none are assumed here. Replacing the display or keyboard also requires updating the enclosure, wiring, and tests.

The requested Pi 5 **4 GB** and **64 GB** storage have been preserved. Silently substituting a Pi 4, a 2 GB board, or a 32 GB card would not meet the stated requirements. Simply labeling a larger bill “S tier” also does not solve the shortfall. A higher tier requires the corresponding project merit and review, not merely a higher price.

Before submission, replace every allowance with an actual part/quantity and delivered quote, resolve the keyboard variant, verify the total in USD including fees, and document how any remaining difference is funded. The builder has authorized a personal contribution of at most EUR 50. Do not order if the actual usable grant plus EUR 50 cannot cover all costs.
