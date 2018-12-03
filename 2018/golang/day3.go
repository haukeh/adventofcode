package main

import (
	"fmt"
	"github.com/haukeh/aoc2018/util"
	"log"
	"time"
)

type point struct {
	x, y int
}

type rec struct {
	num string
	point
	w, h int
}

func main() {
	start := time.Now()

	input := util.ReadStringPerLine("in/day3a.txt")
	rectangles := parseRecs(input)
	grid := make(map[point]int, 500000)
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
			println(rec.num)
		}
	}

	log.Printf("Runtime: %s", time.Since(start))
}

func parseRecs(input []string) []rec {
	var recs []rec
	for _, ln := range input {
		var r rec
		_, err := fmt.Sscanf(ln, "%s @ %d,%d: %dx%d", &r.num, &r.x, &r.y, &r.w, &r.h)
		if err != nil {
			log.Fatal(err)
		}
		recs = append(recs, r)
	}
	return recs
}
