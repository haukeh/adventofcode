package main

import (
	"github.com/haukeh/aoc2018/util"
	"strconv"
	"strings"
)

func main() {
	input := util.ReadStringPerLine("in/day3a.txt")
	rectangles := parseRecs(input)
	grid := make(map[point]int, 1000)

	for _, rec := range rectangles {
		for x := rec.x; x < rec.x+rec.w; x++ {
			for y := rec.y; y < rec.y+rec.h; y++ {
				grid[point{x: x, y: y}] += 1
			}
		}
	}
	var multi int
	for _, v := range grid {
		if v > 1 {
			multi++
		}
	}

	println(multi)

	for _, rec := range rectangles {
		isOnly := true
		for x := rec.x; x < rec.x+rec.w && isOnly; x++ {
			for y := rec.y; y < rec.y+rec.h && isOnly; y++ {
				if grid[point{x: x, y: y}] != 1 {
					isOnly = false
				}
			}
		}
		if isOnly {
			println(rec.Num)
		}
	}
}

type point struct {
	x, y int
}

type rec struct {
	Num  string
	x, y int
	w, h int
}

func parseRecs(input []string) []rec {
	var recs []rec
	for _, ln := range input {
		splits := strings.FieldsFunc(ln, func(r rune) bool {
			return r == '@' || r == ':'
		})
		n := strings.Trim(splits[0], " ")
		coords := strings.Split(strings.Trim(splits[1], " "), ",")
		x, _ := strconv.Atoi(coords[0])
		y, _ := strconv.Atoi(coords[1])
		dims := strings.Split(strings.Trim(splits[2], " "), "x")
		w, _ := strconv.Atoi(dims[0])
		h, _ := strconv.Atoi(dims[1])
		r := rec{
			Num: n,
			x:   x,
			y:   y,
			w:   w,
			h:   h,
		}
		recs = append(recs, r)
	}
	return recs
}
