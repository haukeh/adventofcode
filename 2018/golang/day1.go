package main

import (
	"github.com/haukeh/aoc2018/util"
	"strconv"
)

func main() {
	input := util.ReadStringPerLine("in/day1a.txt")

	println(calculateFrequency(input))
	println(calculateFirstDuplicate(input))
}

func calculateFirstDuplicate(input []string) int {
	seen := map[int]struct{}{
		0: {},
	}
	freq := 0
	for {
		for _, s := range input {
			n, _ := strconv.Atoi(s)
			freq += n
			if _, ok := seen[freq]; ok {
				return freq
			}
			seen[freq] = struct{}{}
		}
	}
}

func calculateFrequency(input []string) int {
	freq := 0
	for _, s := range input {
		n, _ := strconv.Atoi(s)
		freq += n
	}
	return freq
}
