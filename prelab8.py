# Danny Wu
# Physics 264L - Prelab 8

"""
1) Use your measured data set for the width of the pulses to calculate the average pulse
width. Estimate its uncertainty. What can we do with this average pulse width to correct
the measured time between pulses?
"""
widths = []
with open('pulse width.txt') as file:
	for line in file:
		line = line.strip("\n")
		number = float(line)
		widths.append(number)

# Average Pulse Width
total_sum = 0
num_widths = 0
for num in widths:
	total_sum += number
	num_widths += 1

average_pulse_width = total_sum / num_widths
print(average_pulse_width)						# 4.004409171075868e-08

# Estimate its uncertainty.
total_sum = 0
for num in widths:
	total_sum += (num - average_pulse_width)**2

pulse_width_uncertainty = total_sum / num_widths
print(pulse_width_uncertainty) 					# 3.7910052910052747e-16

# Since we know the average pulse width, in our data of the time between pulses,
# we can assume that events less than our average pulse width apart are due to
# muons decaying inside the detector rather two different muons entering the 
# detector one after another.


"""
2) Use your measured data set for time intervals between pulses and extract two separate
data sets.

"""
btwn = []
count = 0
threshold_time = 40e-6
decay_set = []
two_muons_set = []
total_time = 0
with open('distance btwn pulse.txt') as file:
	for line in file:
		line = line.strip("\n")
		number = float(line)
		# If time < 30ns, ignore
		if number <= 30e-9:
			continue
		if number >= threshold_time:
			two_muons_set.append(number)
		else:
			decay_set.append(number)
		total_time += number
		btwn.append(number)

"""
3) Calculate the muon rate (the average number of muon entering the detector per second).
Estimate its uncertainty. Using the calculated muon rate, estimate the probability that a
second muon will enter the detector within 40 µs after the first one. For a given number of
muons (the number of muons that were detected during the experiment) estimate how many
of them could have entered the detector within 40 µs time interval after the previous one.
"""
num_muons = len(decay_set) + len(two_muons_set)
print(num_muons)
muon_rate = num_muons / total_time
print(muon_rate)							# 94.6508702174772

inv_muon_rate = 1 / muon_rate 				# avg num seconds btwn muon
total_sum = 0
for num in decay_set:
	total_sum += (num - inv_muon_rate)**2
for num in two_muons_set:
	total_sum += (num - inv_muon_rate)**2
uncertainty_num_seconds_btwn_muon = total_sum / num_muons

# f = 1/x ==> df = sqrt((-1/x^2*dx))
uncertainty = uncertainty_num_seconds_btwn_muon / (inv_muon_rate)**2
print(uncertainty)							# 1.0003434537830336