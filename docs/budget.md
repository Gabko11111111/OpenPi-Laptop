# OpenPi v0.3 budget — EUR 250 ceiling

Updated 14 September 2026 using the 13 September price checks. **This is a revised planning BOM, not a verified checkout quotation or a funding-ready guarantee.** A total of EUR 250 is achieved by selecting a smaller HDMI screen and a small wireless keyboard, and assigning the remaining unquoted costs explicit allowances. Do not treat allowances as purchased or confirmed offers.

## Funding

- Target request: **S tier, USD 200 maximum**, subject to reviewer approval.
- Total spending ceiling: **EUR 250**, including delivery, VAT and payment charges.
- At the previously recorded reference rate of EUR 1 = USD 1.1592, USD 200 is approximately EUR 172.53. The expected contribution is approximately **EUR 77.47**, not EUR 50. The builder accepted the EUR 250 plan after this difference was explained.
- These conversion figures are illustrative, not a live grant-card conversion quote. Confirm the actual usable grant and personal contribution before ordering. A lower grant does not authorize a larger personal contribution automatically.
- No grant request or purchase has been submitted by this revision.

## Itemized estimate

| Part | EUR | Evidence |
|---|---:|---|
| Raspberry Pi 5 | 129.90 | Observed retailer price |
| Elecom HDMI LCD code 17259 | 29.99 | Live browser price; 9 in stock |
| PROLECH / BLOW mini KS-6; code 84-256- | 7.39 | Live browser sale price; in stock |
| Goodram M1AA 64 GB | 16.39 | Live browser price; delivery up to 7 days |
| Official Raspberry Pi 27 W USB-C supply | 12.95 | Observed retailer price |
| Official Raspberry Pi 5 Active Cooler | 6.50 | Live browser price; in stock |
| 3DPower Basic PETG Light Green | 13.90 | Search listing reference; live verification pending |
| Enclosure v0.3 fastener set | 10.00 | Unverified purchasing allowance |
| Integral printed hinges | 0.00 | Included elsewhere |
| Display cables | 6.00 | Unverified purchasing allowance |
| Pads and feet | 1.00 | Unverified purchasing allowance |
| USB microSDXC reader | 3.00 | Unverified purchasing allowance |
| Delivery | 12.00 | Unverified combined allowance |
| Reserve | 0.98 | Planning reserve |
| **Planning total** | **250.00** | **Includes estimates; not a delivered quote** |

## Evidence and changes

The Pi 5 **4 GB** and **64 GB storage** remain. The official 7-inch DSI screen is replaced by Elecom code **17259**, a **5-inch 800 × 480 HDMI** panel. Treat it as a video display controlled through the keyboard's touchpad: its old XPT2046 touch software is not validated for Pi 5. The seller image shows a separate small USB power connector; confirm the delivered board uses micro-USB 5 V power before buying cables. A rigid Pi 3 HDMI adapter is not suitable for the Pi 5 connector spacing.

The Perixx wired keyboard is replaced by Pabex code **84-256-**, a PROLECH/BLOW mini KS-6 candidate. Its live price was EUR 7.39. Confirm exact model, included USB receiver, battery, charging cable, Linux input operation and physical housing/rim dimensions. USB charging must not be described as wired keyboard data. Its factory battery powers only the keyboard; the computer remains wall-powered.

The new case is v0.3 with a **196 × 190 mm main body**, underside retention and printed hinges. It is not the old v0.2 case with a changed price label. The CAD uses nominal unmeasured keyboard and display envelopes; physical retention, power-switch access and cable bends remain to verify.

## Source links

- [Raspberry Pi 5](https://www.elecom.sk/raspberry-pi-5-4-gb-2/): EUR 129.90; Observed retailer price.
- [Elecom HDMI LCD code 17259](https://www.elecom.sk/5-0-palcovy-dotykovy-lcd-displej-hdmi-800x480-pre-raspberry-pi-3b--xpt2046-rezistivny/): EUR 29.99; Live browser price; 9 in stock.
- [PROLECH / BLOW mini KS-6; code 84-256-](https://www.pabex.sk/bezdrotova-klavesnica-s-touchpadom-84-256-/): EUR 7.39; Live browser sale price; in stock.
- [Goodram M1AA 64 GB](https://www.pabex.sk/pamatova-karta-64gb-tgd-m1aa0640r12/): EUR 16.39; Live browser price; delivery up to 7 days.
- [Official Raspberry Pi 27 W USB-C supply](https://www.elecom.sk/raspberry-pi-27w-usb-c-napajaci-zdroj--eu--biely-2/): EUR 12.95; Observed retailer price.
- [Official Raspberry Pi 5 Active Cooler](https://www.elecom.sk/raspberry-pi-5-active-cooler-2/): EUR 6.50; Live browser price; in stock.
- [3DPower Basic PETG Light Green](https://www.filamenthouse.sk/p/3dpower-basic-petg-svetlozelena-light-green-1kg): EUR 13.90; Search listing reference; live verification pending.

## Mandatory checks before ordering or submitting

1. Obtain a combined delivered quotation for the exact selections. The **EUR 12 shipping allowance is not confirmed** across all stores.
2. Quote the full packs needed for all fasteners, pads, reader and both display cables. Do not count only the fraction used if a larger pack must be purchased. The EUR 10 fastener allowance may prove insufficient.
3. Verify filament stock and price directly: EUR 13.90 is a search-listing reference, not a completed live store check. The older EUR 12.30 transition-filament offer was unavailable and is not used.
4. Slice the case, coupons and supports. One 1 kg spool is budgeted. Main CAD solid volume is approximately 629 cm³, equivalent to approximately 799 g at 1.27 g/cm³ if fully solid; this is not a slicer prediction and excludes supports and mistakes. Keep all printing within the spool or find savings for more material.
5. Confirm display power and the real keyboard variant before printing. Do not install old vendor OS images on the Pi 5 to force touch support; HDMI video plus the keyboard touchpad is the baseline.
6. Only proceed if the final total including fees is at most EUR 250 and the actual grant/personal split is accepted. There is only EUR 0.98 of reserve, so the estimate is fragile.

The previous EUR 371.59 selection and its evidence are retained in `archive/BOM-v02.csv` and `archive/budget-v02.md`. The old EUR 222 ceiling/EUR 50 contribution are superseded by this accepted EUR 250 plan. Basic tools and a computer for writing the card must be available or borrowed; buying tools is not covered.
