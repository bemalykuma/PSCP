"""Saitama"""
import math
def saitama(push, situp, up_down, run):
    """saitama"""
    push_hr_per_day = math.ceil(push / int(input()))
    situp_hr_per_day = math.ceil(situp / int(input()))
    run_hr_per_day = math.ceil(run / int(input()))
    up_down_hr_per_day = math.ceil(up_down / int(input()))
    mx = push_hr_per_day
    if situp_hr_per_day > mx:
        mx = situp_hr_per_day
    if run_hr_per_day > mx:
        mx = run_hr_per_day
    if up_down_hr_per_day > mx:
        mx = up_down_hr_per_day
    print(mx)
saitama(int(input()), int(input()), int(input()), int(input()))
