package main

import (
	"github.com/haukeh/aoc2018/util"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"time"
)

type shift struct {
	date    time.Time
	actions map[int]action
}

type action int

const (
	FallAsleep action = iota
	WakeUp
)

var guardPattern = regexp.MustCompile(`#[0-9]+`)

func main() {
	lines := util.ReadStringPerLine("in/day4a.txt")

	sort.Strings(lines)

	println(lines)

	shiftsPerGuard := make(map[string][]shift)

	var currentGuard string
	var currentShift shift

	for _, r := range lines {
		guardId := guardPattern.FindString(r)

		if guardId != "" {
			shiftsPerGuard[currentGuard] = append(shiftsPerGuard[currentGuard], currentShift)
			currentGuard = guardId
			currentShift = shift{
				actions: make(map[int]action),
			}
		} else {
			date, _ := time.Parse("2006-01-02 15:04", r[1:17])
			if strings.Contains(r, "falls asleep") {
				currentShift.date = date
				currentShift.actions[date.Minute()] = FallAsleep
			} else if strings.Contains(r, "wakes up") {
				currentShift.date = date
				currentShift.actions[date.Minute()] = WakeUp
			}
		}
	}

	minutes := make(map[string]map[int]int)
	guards := make(map[string]int)

	for guard, shifts := range shiftsPerGuard {
		totalTimeAsleep := 0
		for _, s := range shifts {
			asleep := false
			for i := 0; i < 60; i++ {
				if status, ok := s.actions[i]; ok {
					asleep = status == FallAsleep
				}
				if asleep {
					if minutes[guard] == nil {
						minutes[guard] = make(map[int]int)
					}
					minutes[guard][i] += 1
					totalTimeAsleep += 1
				}
			}
		}

		guards[guard] = totalTimeAsleep
	}

	var currMax int
	var sleepyGuard string
	for g, mins := range guards {
		if mins > currMax {
			currMax = mins
			sleepyGuard = g
		}
	}

	sleepyGuardShifts := minutes[sleepyGuard]
	var maxMinute, topTimes int
	for minute, timesAsleep := range sleepyGuardShifts {
		if timesAsleep > topTimes {
			topTimes = timesAsleep
			maxMinute = minute
		}
	}

	g, _ := strconv.Atoi(sleepyGuard[1:])

	println(g)
	println(maxMinute)
	println(g * maxMinute)
}
