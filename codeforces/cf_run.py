#!/usr/bin/env python

import argparse
import subprocess
import time

import colorama

import codeforces

colorama.init(autoreset=True)

def main(argv=None):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('contestId', type=int,
                        help=("Id of the contest. It is not the round number. "
                              "It can be seen in contest URL."))
    
    parser.add_argument('index', type=str,
                        help=("A letter or a letter followed by a digit, that "
                              "represent a problem index in a contest."))
    
    parser.add_argument('program', type=str,
                        help="Path to executable that needs to be tested")
    
    parser.add_argument('-t', '--timeout', type=int, default=10,
                        help=("Timeout for program in seconds, -1 for no time "
                              "limit (default: 10)"))
    
    parser.add_argument('-g', '--gym', action='store_true',
                        help=("If true open gym contest instead of regular "
                              "contest. (default: false)"))
    
    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    args.timeout = None if args.timeout == -1 else args.timeout
    
    title, time_limit, memory_limit, sample_tests = codeforces.problem.get_info(
        args.contestId, args.index, gym=args.gym
    ) 

    print(title)
    print("time limit per test:", time_limit)
    print("memory limit per test:", memory_limit)
    
    print()
    
    for inp, ans in sample_tests:
        start = time.time()
    
        out = subprocess.run(
            args.program,
            input=inp.encode('utf-8'),
            capture_output=True,
            timeout=args.timeout
        ).stdout.decode('utf-8')
    
        time_used = time.time() - start
    
        print('-' * 80, '\n')
    
        print('Time: %d ms\n' % (time_used * 1000))
    
        print(colorama.Style.BRIGHT + 'Input')
        print(inp)
    
        print(colorama.Style.BRIGHT + "Participant's output")
        print(out)
    
        print(colorama.Style.BRIGHT + "Jury's answer")
        print(ans)
