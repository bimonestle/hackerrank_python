# Evil Nation A is angry and plans to launch N guided-missiles
# at the peaceful Nation B in an attempt to wipe out all of Nation B's people.
# Nation A's missile 'i' will arrive in nation B at time 'ti'.
# Missile 'i' communicates with its headquarters by unique radio signals with a
# frequency equal to 'fi'. Can you help the peaceful Nation B survive by building
# a defensive system that will stop the missiles dead in the sky?

# The only way to defend Nation B from the attacking missile is by counter attacking them
# with a hackerX missile. You have a lot of hackerX missiles and each one of them has its own radio frequency.
# An individual hackerX missile can destroy Evil Nation A’s attacking missile if the radio frequency
# of both of the missiles match. Each hackerX missile can be used an indefinite number of times.
# Its invincible and doesn't get destroyed in the collision.

# The good news is you can adjust the frequency of the hackerX missile to match
# the evil missiles' frequency. When changing the hackerX missile's initial frequency fA
# to the new defending frequency fB, you will need \|fB - fA\| units of time to do.

# If two evil missles with same frequency arrive at the same time,
# we can destroy them both with one hackerX missile.
# You can set the frequency of a hackerX missile to any value when its fired.

# What is the minimum number of hackerX missiles you must launch to keep Nation B safe?

# Input Format:
# The first line contains a single integer N denoting the number of missiles.
# This is followed by N lines each containing two integers ti and fi denoting the time & frequency of the ith missile.

# Output Format:
# A single integer denoting the minimum number of hackerX missiles you need to defend the nation.

# SAMPLE INPUT #00
# 4
# 1 1
# 2 2
# 3 1
# 5 1
# Output: 1

# EXPLANATION #00
# A HackerX missile is launched at t = 1 with a frequency f = 1, and destroys the first missile.
# It re-tunes its frequency to f = 2 in 1 unit of time, and destroys the missile that is going to hit Nation B at t = 2.
# It re-tunes its frequency back to 1 in 1 unit of time and destroys the missile that is going to hit the nation at t = 3.
# It is relaunched at t = 5 with f = 1 and destroys the missile that is going to hit nation B at t = 5.
# Hence, you need only 1 HackerX to protect nation B.

# SAMPLE INPUT #01
# 4
# 1 1
# 2 3
# 3 1
# 5 1
# Output: 2

# EXPLANATION #01
# Destroy 1 missile at t = 1, f = 1. now at t = 2, there is a missile with frequency 3.
# The launched missile takes 2 units of time to destroy this, hence we need a new hackerX missile to destroy this one.
# The first hackerX missile can destroy the 3rd missile which has the same frequency as itself.
# The same hackerX missile destroys the missile that is hitting its city at t = 5. Thus, we need atleast 2 hackerX missiles.

# ANOTHER TEST CASE
# 20
# 5		    687			AX
# 49		338			BX
# 129		535			CX
# 130		831			DX
# 140		841			DX
# 142		591			AX
# 144		581			E
# 271		594			A
# 271		970			D
# 287		495			CX
# 294		191			BX
# 333		150			FX
# 488		643			CX
# 755		816			FX
# 816		341			C
# 848		779			F
# 880		276			B
# Output: 6

def missileDefend(missiles):
    hackerX = missiles[0:1]
    newFreq = 0
    newTime = 0
    for missile in missiles[1:]:
        for idx in range(len(missile)):
            if idx % 2 != 0:
                freq = missile[1]
                time = missile[0]
                
                for xMissile in hackerX:
                    for kdx in range(len(xMissile)):
                        xTime = xMissile[0]
                        xFreq = xMissile[1]
                        if kdx %2 != 0:
                            newFreq = freq - xFreq
                            if newFreq < 0:
                                newFreq * -1
                            newTime = newFreq + xTime
                            print(newTime) # debugging
                            if newTime > time:
                                hackerX.append(missile)
                                
    print(hackerX) # debugging
    return len(hackerX)