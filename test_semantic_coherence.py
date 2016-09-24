from semantic_coherence.semantic_coherence import index_file, index_string

sims_tc = index_file('timecube_raw.txt')
ave_tc = sum(sims_tc, 0.0) / len(sims_tc)
min_tc = min(sims_tc)

sims_ctl = index_file('control_raw.txt')
ave_ctl = sum(sims_ctl, 0.0) / len(sims_ctl)
min_ctl = min(sims_ctl)

print("ave_tc: " + str(ave_tc) + " ave_ctl: " + str(ave_ctl))
print("min_tc: " + str(min_tc) + " min_ctl: " + str(min_ctl))

index_string("""
In 1884,  meridian time personnel met
 in Washington to change Earth time.
 In 1884,  meridian time personnel met
 in Washington to change Earth time.
First words said was that only 1 day
could be used on Earth to not change
 the 1 day bible. So they applied the 1
day  and  ignored  the  other  3 days.
The bible time was wrong then and it
 proved wrong today. This a major lie
  has so much evil feed from it's wrong.
No man on Earth has no belly-button,
  it proves every believer on Earth a liar.
""")
