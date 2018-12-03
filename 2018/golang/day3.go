package main

import (
	"github.com/haukeh/aoc2018/util"
	"strconv"
	"strings"
)

func main() {
	input := util.ReadStringPerLine("in/day3a.txt")

}

type rec struct {
	Num  string
	x, y int
	w, h int
}

func parseRecs(input []string) []rec {
	var res []rec
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
		res = append(res, r)
	}
	return res
}
