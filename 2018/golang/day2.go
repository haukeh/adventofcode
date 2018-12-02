package main

import (
	"fmt"
	"github.com/haukeh/aoc2018/util"
	"strings"
)

func main() {
	input := util.ReadStringPerLine("in/day2a.txt")

	println(calculateChecksum(input))
	println(findCommonLetters(input))
}

func calculateChecksum(input []string) int {

	var doublets, triplets int

	for _, ln := range input {
		occurrences := make(map[rune]int)
		for _, char := range ln {
			occurrences[char] += 1
		}
		var d, t bool
		for _, v := range occurrences {
			switch v {
			case 2:
				d = true
			case 3:
				t = true
			}
		}
		if d {
			doublets += 1
		}
		if t {
			triplets += 1
		}
	}

	return doublets * triplets
}

func findCommonLetters(input []string) string {
	i, j := findIndexesOfCorrectBoxes(input)

	w1 := input[i]
	w2 := input[j]

	var sb strings.Builder
	for i := 0; i < len(w1); i++ {
		if w1[i] == w2[i] {
			sb.WriteRune(rune(w1[i]))
		}
	}
	return sb.String()
}

func findIndexesOfCorrectBoxes(input []string) (int, int) {
	maxItemLen := 0
	for _, e := range input {
		if len(e) > maxItemLen {
			maxItemLen = len(e)
		}
	}

	println(maxItemLen)

	for i1, w1 := range input {
		for i2, w2 := range input {
			if w2 == w1 {
				continue
			}
			diffs := 0
			r1 := []rune(w1)
			r2 := []rune(w2)
			for i := 0; i < maxItemLen && diffs < 2; i++ {
				if r1[i] != r2[i] {
					diffs++
				}
			}
			if diffs == 1 {
				return i1, i2
			}
		}
	}
	panic(fmt.Errorf("no words match"))
}
