A small Python script I made that changes the number of rows in frames for a FamiTracker file
(This is mostly for ripping GB/GBC, where when you use GBSImport, the ftm file has 256 rows per frame, which doesn't fit the tracks that you rip)

**How to use:**
1. Rip your track via GBSImport
2. Open the FamiTracker file and take note of where each bar/beat/how much you wanna chop up your song end (for instance, a bar in your song might end at `7F`, and the next bar starts at `80`. Since those numbers are hexadecimal, you want to note down `7F` as 127)
3. Save the file as txt (File > Export text)
4. Run `Python ft_resize.py "Path to the txt file (you can drag and drop in cmd)" (the number you wrote down, in the example, 127)`
5. Import the resized file in FamiTracker (File > Import text)

Note that this just helps with making the raw ripped data easier to manage, but at the end of the day, you're dealing with raw GB/GBC music data
